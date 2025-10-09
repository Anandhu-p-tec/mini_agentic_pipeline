# src/graph_pipeline.py
from langgraph.graph import StateGraph, END
from src.retriever import Retriever
from src.reasoner import Reasoner
from src.actor_csv import CSVActor
from src.utils import log_step

class AgenticGraph:
    def __init__(self):
        self.retriever = Retriever()
        self.reasoner = Reasoner()
        self.actor = CSVActor()

        self.graph = StateGraph(self.node_schema)

        # Define nodes
        self.graph.add_node("retriever", self.retriever_node)
        self.graph.add_node("reasoner", self.reasoner_node)
        self.graph.add_node("actor", self.actor_node)

        # Define flow
        self.graph.add_edge("retriever", "reasoner")
        self.graph.add_conditional_edges("reasoner", self.route_decision)
        self.graph.add_edge("actor", END)

        self.executor = self.graph.compile()

    def node_schema(self):
        return {
            "query": str,
            "context": str,
            "decision": str,
            "result": str
        }

    def retriever_node(self, state):
        log_step("Graph", "Running Retriever")
        docs = self.retriever.retrieve(state["query"])
        state["context"] = " ".join([d.page_content for d in docs])
        return state

    def reasoner_node(self, state):
        log_step("Graph", "Running Reasoner")
        state["decision"] = self.reasoner.decide(state["query"], state["context"])
        return state

    def route_decision(self, state):
        """Route based on decision output"""
        decision = state["decision"]
        if "CSV" in decision or "tool" in decision.lower():
            return "actor"
        return END

    def actor_node(self, state):
        log_step("Graph", "Running Actor")
        words = state["query"].lower().split()
        item = words[-1]
        tool_result = self.actor.lookup(item)
        state["result"] = state["decision"] + "\n\n" + tool_result
        return state

    def run(self, query: str):
        initial_state = {"query": query, "context": "", "decision": "", "result": ""}
        final_state = self.executor.invoke(initial_state)
        return final_state.get("result") or final_state.get("decision")

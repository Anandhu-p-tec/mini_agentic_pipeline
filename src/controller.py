from src.retriever import Retriever
from src.reasoner import Reasoner
from src.actor_csv import CSVActor
from src.utils import log_step

class Controller:
    def __init__(self):
        self.retriever = Retriever()
        self.reasoner = Reasoner()
        self.actor = CSVActor()

    def handle_query(self, query):
        log_step("Controller", f"Handling query: {query}")

        # Step 1: Retrieve KB docs
        docs = self.retriever.retrieve(query)
        context = " ".join([d.page_content for d in docs])

        # Step 2: Reason
        decision = self.reasoner.decide(query, context)

        # Step 3: Tool usage if mentioned
        if "CSV" in decision or "tool" in decision.lower():
            # assume user asks about prices
            words = query.lower().split()
            item = words[-1]  # simple heuristic: last word
            tool_result = self.actor.lookup(item)
            return decision + "\n\n" + tool_result

        return decision

import google.generativeai as genai
from src.utils import GEMINI_API_KEY, log_step

class Reasoner:
    def __init__(self, prompt_file="src/prompts/prompt_v1.txt"):
        genai.configure(api_key=GEMINI_API_KEY)
        self.model = genai.GenerativeModel("gemini-2.0-flash")

        with open(prompt_file, "r") as f:
            self.base_prompt = f.read()

    def decide(self, query, context):
        log_step("Reasoner", f"Deciding action for: {query}")

        user_input = f"""
        Query: {query}
        Context: {context}
        Decide: Should I answer using KB only, or call CSV tool?
        Provide reasoning + final answer.
        """

        response = self.model.generate_content(
            f"{self.base_prompt}\n\n{user_input}"
        )

        decision = response.text
        log_step("Reasoner", f"Decision: {decision}")
        return decision

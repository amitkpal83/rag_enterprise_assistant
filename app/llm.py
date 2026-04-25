from langchain.chat_models import ChatOpenAI
from tenacity import retry, stop_after_attempt, wait_exponential

class LLMService:
    def __init__(self):
        self.model = ChatOpenAI(model="gpt-4o-mini", temperature=0)

    @retry(stop=stop_after_attempt(3), wait=wait_exponential())
    def generate(self, prompt):
        return self.model.invoke(prompt).content

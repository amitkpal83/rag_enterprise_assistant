from app.cache import Cache
from app.llm import LLMService
from app.evaluator import Evaluator
from app.retriever import Retriever

class RAGPipeline:
    def __init__(self, vectorstore):
        self.cache = Cache()
        self.llm = LLMService()
        self.evaluator = Evaluator()
        self.retriever = Retriever(vectorstore)

    def query(self, question):
        cached = self.cache.get(question)
        if cached:
            return {"answer": cached, "cached": True}

        docs = self.retriever.retrieve(question)
        context = "\n".join([d.page_content for d in docs])

        prompt = f"Answer from context:\n{context}\nQuestion:{question}"

        answer = self.llm.generate(prompt)
        eval_result = self.evaluator.evaluate(answer, context)

        self.cache.set(question, answer)

        return {"answer": answer, "evaluation": eval_result, "cached": False}

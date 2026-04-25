class Evaluator:
    def evaluate(self, answer, context):
        grounded = context.split("\n")[0] in answer
        return {"grounded": grounded, "score": 1 if grounded else 0}

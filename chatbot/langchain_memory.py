import langchain

class LangChainMemory:
    def __init__(self):
        self.langchain = langchain.LangChain()

    def compress(self, context):
        """Compress context using LangChain."""
        return self.langchain.compress(context)

    def vectorize(self, processed_context):
        """Vectorize processed context using LangChain."""
        return self.langchain.vectorize(processed_context)
import pinecone

class PineconeStore:
    def __init__(self, pinecone_api_key):
        self.pinecone_api_key = pinecone_api_key
        self.init_pinecone()

    def init_pinecone(self):
        pinecone.deinit()
        pinecone.init(api_key=self.pinecone_api_key)
        self.pinecone_namespace = "client_data"
        self.pinecone_vector_size = 300
        pinecone.create_namespace(namespace=self.pinecone_namespace, metric="cosine", vector_size=self.pinecone_vector_size)

    def save_context(self, client_id, vectorized_context):
        pinecone.upsert(upserts={str(client_id): vectorized_context}, namespace=self.pinecone_namespace)

    def close(self):
        pinecone.deinit()
import faiss
from langchain.docstore.document import Document
from langchain.vectorstores import FAISS
# Using a mock embeddings class for demonstration without external API keys, 
# but in production this would be GoogleGenerativeAIEmbeddings.
from langchain.embeddings.base import Embeddings

class MockEmbeddings(Embeddings):
    def embed_documents(self, texts):
        return [[0.1] * 384 for _ in texts]
    def embed_query(self, text):
        return [0.1] * 384

docs = [
    Document(page_content="ShopNow Return Policy: You can return any item within 30 days of delivery. Returns are free for Prime members. Non-prime members pay a $5 restocking fee.", metadata={"source": "policy"}),
    Document(page_content="Payment Issues: If your card was charged twice, please wait 24 hours as the pending charge usually drops. If it persists, contact support.", metadata={"source": "faq"}),
    Document(page_content="Delivery Complaints: If your package is marked as delivered but you cannot find it, please check with neighbors. After 48 hours, we can process a replacement.", metadata={"source": "faq"}),
]

vector_store = FAISS.from_documents(docs, MockEmbeddings())

def query_rag(query: str) -> str:
    # Performs semantic search over the FAISS vector database
    results = vector_store.similarity_search(query, k=1)
    if results:
        return results[0].page_content
    return "No relevant policy found."

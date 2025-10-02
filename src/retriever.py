from langchain_community.document_loaders import DirectoryLoader, TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from src.utils import log_step

class Retriever:
    def __init__(self, kb_path="kb_docs/"):
        loader = DirectoryLoader(kb_path, loader_cls=TextLoader)
        documents = loader.load()

        splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
        docs = splitter.split_documents(documents)

        embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
        self.vectordb = FAISS.from_documents(docs, embeddings)
        log_step("Retriever", "Knowledge base indexed with embeddings.")

    def retrieve(self, query, k=3):
        hits = self.vectordb.similarity_search(query, k=k)
        log_step("Retriever", f"Top {k} docs retrieved for query: {query}")
        return hits

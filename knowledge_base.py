import os
from langchain_community.document_loaders import DirectoryLoader, TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_chroma import Chroma

DATA_PATH = "data/"
DB_PATH = "chroma_db/"

def create_vector_db():
    print("Loadining files...")
    loader = DirectoryLoader(DATA_PATH, glob="*.txt", loader_cls=TextLoader)
    documents = loader.load()

    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    texts = text_splitter.split_documents(documents)

    print("Creating embeddings, vectors...")
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

    print(f"Saving {len(texts)} fragmentd to database in {DB_PATH}...")
    db = Chroma.from_documents(texts, embeddings, persist_directory=DB_PATH)
    
    print("DONE! Database was created.")

if __name__ == "__main__":
    create_vector_db()
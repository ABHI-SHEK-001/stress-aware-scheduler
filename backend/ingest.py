import os
from dotenv import load_dotenv
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter

load_dotenv()  # make sure API key is loaded

def ingest_data(data_dir: str, index_path: str):
    print(f"🔍 ingest_data called with data_dir={data_dir} index_path={index_path}")
    
    # List files in data_dir
    try:
        files = os.listdir(data_dir)
    except Exception as e:
        print(f"❌ Error listing directory {data_dir}: {e}")
        return

    txt_files = [f for f in files if f.endswith(".txt")]
    print(f"📂 Found these .txt files: {txt_files}")

    all_docs = []
    for filename in txt_files:
        filepath = os.path.join(data_dir, filename)
        print(f"📄 Loading file: {filepath}")
        loader = TextLoader(filepath)
        docs = loader.load()
        all_docs.extend(docs)

    if not all_docs:
        print("⚠️ No documents loaded—make sure your .txt files aren’t empty.")
        return

    # Split into chunks
    splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    chunks = splitter.split_documents(all_docs)
    print(f"🔪 Split into {len(chunks)} chunks")

    # Create embeddings & index
    if not chunks:
        print("⚠️ No chunks were created. Make sure your input files have enough content.")
        return

    embeddings = HuggingFaceEmbeddings()
    vector_store = FAISS.from_documents(chunks, embeddings)
    vector_store.save_local(index_path)
    print(f"✅ Ingested {len(chunks)} chunks into FAISS at {index_path}")

if __name__ == "__main__":
    # Adjust the path if necessary to point at your data folder
    ingest_data(data_dir=os.path.join("..", "data"), index_path="faiss_index")

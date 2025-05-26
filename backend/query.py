import os
from textblob import TextBlob
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.text_splitter import CharacterTextSplitter

def search_faiss_index(query: str, index_path: str = "faiss_index", k: int = 3):
    # Load embeddings
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")


    # Load FAISS index
    vector_store = FAISS.load_local(index_path, embeddings, allow_dangerous_deserialization=True)


    # Perform similarity search
    results = vector_store.similarity_search(query, k=k)
    
    print(f"\n🔎 Top {k} Results for: \"{query}\"")
    for i, res in enumerate(results):
        content = res.page_content.strip()
        sentiment = TextBlob(content).sentiment.polarity

        if sentiment > 0.1:
            label = "🙂 Positive"
        elif sentiment < -0.1:
            label = "🙁 Negative"
        else:
            label = "😐 Neutral"

        print(f"\nResult {i+1}:")
        print(content)
        print(f"🧠 Sentiment: {label} (score: {sentiment:.2f})")
        print("-" * 40)


if __name__ == "__main__":
    user_query = input("💬 Ask a question about your meeting notes or chats:\n> ")
    search_faiss_index(user_query)

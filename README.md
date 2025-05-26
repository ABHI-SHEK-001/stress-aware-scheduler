# 🧠 StressAware Scheduler

An AI-powered, emotionally intelligent scheduling assistant that helps teams reschedule meetings based on stress levels and urgency — with future Ethereum integration for trustless and decentralized workplace coordination.

https://stress-aware-scheduler-fbaux7cmhxdtmtveqrad9f.streamlit.app

---

## 🚀 Features

- 🎤 **Voice Input** using OpenAI Whisper
- 🧠 **Sentiment Detection** with TextBlob
- 🔍 **Contextual Awareness** with FAISS + HuggingFace Embeddings (RAG)
- 📂 **.txt File Upload** to compare with past conflicts
- 🤖 **Urgency Scoring** based on emotional polarity
- ⏱️ **Auto Scheduler (MVP)** suggests rescheduling based on stress
- 🌐 **Streamlit Web Interface**

---

## 💡 Use Case

Scheduling isn't just about time — it's about **mental bandwidth**. StressAware Scheduler helps:

- Reduce back-to-back high-stress meetings  
- Identify patterns in historical conflicts  
- Suggest stress-informed reschedules  
- Enable emotionally intelligent coordination in DAOs or remote teams

---

## ✨ Demo Steps

1. 🎤 Speak or type your meeting request (e.g. "Move 3PM meeting, team is exhausted")
2. 🧠 AI analyzes sentiment & urgency
3. 📚 Context-aware search finds similar past issues
4. 📅 Suggests smart rescheduling options (or keeps it if stress is low)

---

## 🛠️ Tech Stack

- **Streamlit** – UI
- **Python**
- **OpenAI Whisper** – Voice to text
- **LangChain** – RAG pipeline
- **FAISS** – Vector similarity search
- **HuggingFace Transformers** – Sentence embeddings
- **TextBlob** – Sentiment analysis
- **dotenv** – Environment management

---

## ⛓️ Ethereum Track (ETHIndia Alignment)

In future iterations, we plan to bring scheduling on-chain by integrating:

- ✅ **Decentralized Identity (DID)** for user authentication
- 📜 **On-chain logs** of meeting changes for transparency
- 📊 **Anonymized wellness metrics** stored immutably
- 🗳️ **Token-gated or DAO-native scheduling logic**

This would make StressAware Scheduler a human-first tool for the **future of decentralized work**.

---

## 🐛 Known Issues

- Whisper API sometimes struggles with low audio quality
- FAISS index must be rebuilt on each new .txt upload (future fix: persistent store)
- Auto scheduler is currently rule-based (AI-powered logic in progress)

---

## 📦 Installation & Usage

```bash
# 1. Clone the repo
git clone https://github.com/your-username/stressaware-scheduler.git
cd stressaware-scheduler

# 2. Install dependencies
pip install -r requirements.txt

# 3. Set environment key
export OPENAI_API_KEY=your_key_here  # or use .env

# 4. Run the app
streamlit run app.py
```

## 📃 License

MIT License

---

## 📬 Contact

- goyalabhi2005@gmail.com

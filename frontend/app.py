import os
import streamlit as st
import time
from datetime import datetime, timedelta

# ========== Demo Configuration ==========
DEMO_DATA = {
    "request": "Reschedule 3PM team meeting - multiple members overwhelmed",
    "response": {
        "urgency": 4,
        "sentiment": -0.7,
        "recommendation": "🚨 Reschedule to 4PM with 30min buffer",
        "conflicts": [
            ("2024-03-15", "Team burnout after back-to-back meetings", 0.8),
            ("2024-02-28", "Critical bug missed due to rushed planning", 0.9),
            ("2024-02-10", "Client conflict from overbooked sprint", 0.7)
        ]
    }
}

# ========== Mock Data & Config ==========
st.set_page_config(page_title="StressAware Scheduler", layout="centered", page_icon="🤖")

# Sample meeting history for RAG
SAMPLE_HISTORY = [
    {"content": "Team conflict resolved by moving meeting to Friday", "severity": 8},
    {"content": "Urgent client call prioritized over internal review", "severity": 9},
    {"content": "Buffer added after stressful sprint planning", "severity": 7}
]

# ========== Enhanced UI Components ==========
def main():
    st.title("🤖 Socially-Aware Meeting Optimizer")
    
    # Dashboard Columns
    col1, col2 = st.columns([3, 2])
    
    with col1:
        st.subheader("📅 Schedule Assistant")
        meeting_input()
        
    with col2:
        st.subheader("📊 Team Wellness Dashboard")
        display_metrics()
        st.divider()
        display_historical_conflicts()

    # Demo System
    st.sidebar.subheader("🚀 Quick Start")
    if st.sidebar.button("▶️ Run Prebuilt Demo"):
        run_demo_scenario()

# ========== Core Functionality ==========
def meeting_input():
    """Main input section"""
    with st.form("meeting_form"):
        request = st.text_area("✍️ Meeting request:", 
                             placeholder="E.g. 'Reschedule 3PM team sync - John seems stressed'")
        
        uploaded_file = st.file_uploader("📁 Upload meeting notes", type=["txt"])
        
        if st.form_submit_button("🚀 Analyze"):
            process_request(request, uploaded_file)

def process_request(request, uploaded_file):
    """Handle analysis and recommendations"""
    with st.spinner("🔍 Analyzing request..."):
        # Sentiment Analysis
        urgency, sentiment = analyze_sentiment(request)
        
        # File Processing
        if uploaded_file:
            process_uploaded_file(uploaded_file)
        
        # Display Results
        with st.container(border=True):
            st.subheader("🤖 AI Recommendation")
            display_recommendation(urgency, sentiment)
            display_similar_conflicts(request)

# ========== Analysis Functions ==========
def analyze_sentiment(text):
    """Enhanced mock analysis"""
    urgency = min(len(text.split()) // 3 + 1, 5)  # Word count urgency
    sentiment = (urgency - 3) / 5  # Simulated sentiment
    return urgency, round(sentiment, 2)

def process_uploaded_file(file):
    """Handle file uploads"""
    content = file.getvalue().decode("utf-8")
    st.success(f"📄 Processed {len(content.split())} words from {file.name}")
    
# ========== Display Components ==========
def display_metrics():
    """Team wellness dashboard"""
    metric_col1, metric_col2 = st.columns(2)
    with metric_col1:
        st.metric("😊 Team Morale", "72%", "+8% this week")
    with metric_col2:
        st.metric("🔥 Burnout Risk", "Medium", "2 high-risk members")

def display_recommendation(urgency, sentiment):
    """AI recommendation box"""
    if urgency >= 4:
        st.error("🚨 Immediate Rescheduling Recommended")
        st.write("Suggested action: Create buffer time & notify team")
    else:
        st.success("✅ Schedule Approved with Buffer")
        st.write("Suggested action: Add 15min pre-meeting quiet time")
    
    st.write(f"""
    - **Urgency Level**: {urgency}/5
    - **Sentiment Score**: {sentiment:.2f}
    """)

# Add this function under the "Display Components" section
def display_similar_conflicts(request):
    """Show RAG-based similar conflicts"""
    st.subheader("🔍 Similar Past Conflicts")
    
    # Perform similarity search
    results = vector_store.similarity_search(request, k=3)
    
    # Display results
    for i, doc in enumerate(results):
        with st.container(border=True):
            cols = st.columns([1, 4])
            cols[0].write(f"**Conflict {i+1}**")
            cols[1].write(doc.page_content[:200] + "...")


def display_historical_conflicts():
    """Past conflict visualization"""
    st.write("### 📜 Conflict History")
    for i, conflict in enumerate(SAMPLE_HISTORY):
        st.write(f"{i+1}. {conflict['content']}")
        st.progress(conflict['severity']/10)

# ========== Enhanced Visible Demo System ==========
def run_demo_scenario():
    """Interactive demo with chat-style visibility"""
    demo_container = st.empty()
    
    with demo_container.container(border=True):
        st.subheader("🚀 Live Demo: Crisis Meeting Scenario")
        chat_container = st.container(height=500)
        
        with chat_container:
            # Initial Request
            with st.chat_message("user"):
                st.write("📩 **Initial Request**")
                st.code(DEMO_DATA["request"], language="text")
            
            # Analysis Progress
            with st.status("🔍 Analyzing request...", expanded=True):
                cols = st.columns([1, 3])
                with cols[0]:
                    st.markdown("<h2 style='text-align: center;'>🚨</h2>", unsafe_allow_html=True)
                with cols[1]:
                    st.write("Detecting emotional signals...")
                    time.sleep(1)
                    st.metric("Urgency Level", DEMO_DATA['response']['urgency'], delta="High")
                    st.metric("Sentiment Score", DEMO_DATA['response']['sentiment'], delta="Negative")

            # Historical Conflicts
            with st.chat_message("assistant"):
                st.write("📚 **Historical Pattern Match**")
                for date, desc, severity in DEMO_DATA['response']['conflicts']:
                    with st.container(border=True):
                        st.caption(f"🗓️ {date}")
                        st.write(desc)
                        st.progress(severity)
                    time.sleep(0.3)

            # Final Recommendation
            with st.chat_message("assistant", avatar="🤖"):
                st.write("💡 **AI Recommendation**")
                st.success(DEMO_DATA['response']['recommendation'])
                st.balloons()
                st.button("✅ Accept Recommendation", type="primary")

        # Persistent controls
        st.divider()
        st.caption("🔁 Refresh page to restart demo")

# ========== Run App ==========
if __name__ == "__main__":
    main()
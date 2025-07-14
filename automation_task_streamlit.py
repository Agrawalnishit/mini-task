import streamlit as st
import time
from datetime import datetime

# Simulated task status
task_status = {
    "Scheduled Task": False,
    "Last Run": "Never",
    "Logs": [],
}

def start_task():
    task_status["Scheduled Task"] = True
    log_event("Scheduled task started.")

def stop_task():
    task_status["Scheduled Task"] = False
    log_event("Scheduled task stopped.")

def run_manual_task():
    log_event("Manual task execution started.")
    time.sleep(2)  # Simulating task execution
    log_event("Manual task execution completed.")

def log_event(message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    task_status["Last Run"] = timestamp
    task_status["Logs"].insert(0, f"[{timestamp}] {message}")
    if len(task_status["Logs"]) > 50:  # Limit log length
        task_status["Logs"] = task_status["Logs"][:50]

# UI
st.title("⚙️ Automation Control Panel")

st.subheader("🔄 Task Status")
st.write(f"**Scheduled Task:** {'✅ Running' if task_status['Scheduled Task'] else '❌ Stopped'}")
st.write(f"**Last Run:** {task_status['Last Run']}")

col1, col2, col3 = st.columns(3)

with col1:
    if st.button("▶️ Start Task"):
        start_task()

with col2:
    if st.button("⏹️ Stop Task"):
        stop_task()

with col3:
    if st.button("🛠 Run Manual Task"):
        run_manual_task()

st.subheader("📜 Logs")
for log in task_status["Logs"]:
    st.text(log)

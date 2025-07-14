import gradio as gr
import time
from datetime import datetime

# Task state and logs
task_status = {
    "is_running": False,
    "last_run": "Never",
    "logs": [],
}

def log_event(message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    task_status["last_run"] = timestamp
    log_entry = f"[{timestamp}] {message}"
    task_status["logs"].insert(0, log_entry)
    task_status["logs"] = task_status["logs"][:50]  # keep only last 50 logs

def start_task():
    if not task_status["is_running"]:
        task_status["is_running"] = True
        log_event("Scheduled task started.")
    return get_status()

def stop_task():
    if task_status["is_running"]:
        task_status["is_running"] = False
        log_event("Scheduled task stopped.")
    return get_status()

def run_manual_task():
    log_event("Manual task started.")
    time.sleep(2)  # Simulate execution
    log_event("Manual task completed.")
    return get_status()

def get_status():
    status = f"✅ Running" if task_status["is_running"] else "❌ Stopped"
    last = task_status["last_run"]
    logs = "\n".join(task_status["logs"])
    return status, last, logs

with gr.Blocks() as demo:
    gr.Markdown("# ⚙️ Automation Control Panel")

    status_output = gr.Textbox(label="Task Status", interactive=False)
    last_run_output = gr.Textbox(label="Last Run", interactive=False)
    logs_output = gr.Textbox(label="Logs", lines=15, interactive=False)

    with gr.Row():
        start_btn = gr.Button("▶️ Start Task")
        stop_btn = gr.Button("⏹️ Stop Task")
        run_btn = gr.Button("🛠 Run Manual Task")

    start_btn.click(fn=start_task, outputs=[status_output, last_run_output, logs_output])
    stop_btn.click(fn=stop_task, outputs=[status_output, last_run_output, logs_output])
    run_btn.click(fn=run_manual_task, outputs=[status_output, last_run_output, logs_output])

    # Initial load
    demo.load(fn=get_status, outputs=[status_output, last_run_output, logs_output])

demo.launch()

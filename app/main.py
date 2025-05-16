from fastapi import FastAPI, WebSocket
from fastapi.responses import HTMLResponse
import asyncio

app = FastAPI()

html = """
<!DOCTYPE html>
<html>
<head>
    <title>WebSocket Progress</title>
    <style>
        body { font-family: Arial, sans-serif; padding: 2em; }
        #progress-container { width: 100%; background: #eee; border-radius: 4px; margin: 20px 0; }
        #progress-bar {
            height: 30px;
            width: 0%;
            background-color: #4caf50;
            text-align: center;
            line-height: 30px;
            color: white;
            border-radius: 4px;
        }
        #status { margin-top: 10px; font-weight: bold; }
    </style>
</head>
<body>
    <h1>🚀 WebSocket Progress Bar Demo</h1>
    <button onclick="startTask()">Start Task</button>
    <div id="progress-container">
        <div id="progress-bar">0%</div>
    </div>
    <div id="status">Idle</div>

    <script>
        let ws;

        function startTask() {
            if (ws) ws.close();
            ws = new WebSocket("ws://localhost:8000/ws/progress");
            const progressBar = document.getElementById("progress-bar");
            const status = document.getElementById("status");

            ws.onopen = () => {
                status.textContent = "Task started...";
            };

            ws.onmessage = (event) => {
                const data = JSON.parse(event.data);
                progressBar.style.width = data.percent + "%";
                progressBar.textContent = data.percent + "%";
                status.textContent = data.message;

                if (data.percent >= 100) {
                    status.textContent = "✅ Done!";
                    ws.close();
                }
            };

            ws.onclose = () => {
                if (progressBar.style.width !== "100%") {
                    status.textContent = "❌ Connection closed before completion";
                }
            };
        }
    </script>
</body>
</html>
"""

@app.get("/")
async def get():
    return HTMLResponse(html)

@app.websocket("/ws/progress")
async def websocket_progress(websocket: WebSocket):
    await websocket.accept()
    for i in range(101):
        await asyncio.sleep(0.1)  # simulate work
        await websocket.send_json({
            "percent": i,
            "message": f"Processing... {i}%"
        })
    await websocket.close()

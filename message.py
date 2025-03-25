from fastapi import WebSocket, WebSocketDisconnect

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    try:
        while True:
            data = await websocket.receive_text()  # Recebe dados do cliente
            await websocket.send_text(f"Mensagem recebida: {data}")  # Envia resposta
    except WebSocketDisconnect:
        print("Cliente desconectado")

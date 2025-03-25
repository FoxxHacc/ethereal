from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Modelo de dados para o status de verificação
class StatusResponse(BaseModel):
    status: str

# Endpoint para verificar a conexão com o servidor
@app.get("/api/verify", response_model=StatusResponse)
async def verify_connection():
    return {"status": "ok"}  # Retorna status ok se a API estiver funcionando corretamente

# Endpoint de exemplo para mais interações
@app.get("/api/player/{player_id}")
async def get_player_status(player_id: int):
    return {"player_id": player_id, "status": "active"}  # Exemplo de retorno

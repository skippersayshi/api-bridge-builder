from __future__ import annotations
from fastapi import FastAPI
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from bridge_builder import RalphLoop

app = FastAPI(title="API Bridge Builder")
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])

class BridgeRequest(BaseModel):
    description: str

@app.post("/api/bridge")
async def build_bridge(req: BridgeRequest):
    try:
        loop = RalphLoop()
        result = loop.run(req.description)
        return {"success": result.success, "notes": result.notes}
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})

@app.get("/", response_class=HTMLResponse)
async def index():
    with open("index.html") as f:
        return f.read()

import json
import asyncio
import uvicorn
from fastapi import FastAPI, Request

app = FastAPI()


@app.get("/echo")
@app.post("/echo")
async def root(request: Request):
    body = b''
    async for chunk in request.stream():
        body += chunk
    print(body)
    response = {
        "message": {
            "__METHOD__": request.method,
            "__URL__": str(request.url),
            "__HEADERS__": dict(request.headers),
            "__QUERY_PARAMS__": str(request.query_params),
            "__BODY__": json.loads(body.decode()) if body else ""
        }
    }
    return response


@app.get("/long/echo")
@app.post("/long/echo")
async def root(request: Request):
    body = b''
    async for chunk in request.stream():
        body += chunk
    response = {
        "message": {
            "__METHOD__": request.method,
            "__URL__": str(request.url),
            "__HEADERS__": dict(request.headers),
            "__QUERY_PARAMS__": str(request.query_params),
            "__BODY__": json.loads(body.decode()) if body else ""
        }
    }
    await asyncio.sleep(2)
    return response
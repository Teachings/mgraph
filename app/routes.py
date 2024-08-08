import asyncio
from fastapi import APIRouter, Request, WebSocket, WebSocketDisconnect
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from graph.setup import setup_graph

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")

graph = setup_graph()

@router.on_event("startup")
async def startup_event():
    graph.graph_generator = graph.execute()

@router.get("/", response_class=HTMLResponse)
async def get(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@router.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    try:
        while True:
            if graph.completed:
                await websocket.send_json({
                    "graph": graph.visualize('END'),
                    "state": graph.state.data,
                    "completed": True
                })
                break
            try:
                graph_data = next(graph.graph_generator)
            except StopIteration:
                graph_data = graph.visualize('END')
                graph.completed = True

            await websocket.send_json({
                "graph": graph_data,
                "state": graph.state.data,
                "completed": graph.completed
            })
            await asyncio.sleep(1)  # Delay to visualize the transition
    except WebSocketDisconnect:
        print("Client disconnected")
    except Exception as e:
        print(f"Unexpected error: {e}")
    finally:
        try:
            await websocket.close()
        except RuntimeError as e:
            print(f"WebSocket close error: {e}")

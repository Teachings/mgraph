from fastapi import APIRouter, Request
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

@router.get("/graph")
async def get_graph():
    if graph.completed:
        return {
            "graph": graph.visualize('END'),
            "state": graph.state.data,
            "completed": True
        }
    try:
        graph_data = next(graph.graph_generator)
    except StopIteration:
        graph_data = graph.visualize('END')  # Ensure the end node is visualized

    return {
        "graph": graph_data,
        "state": graph.state.data,
        "completed": graph.completed
    }

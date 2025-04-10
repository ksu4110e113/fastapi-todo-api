from fastapi import FastAPI, HTTPException, status
from fastapi.responses import RedirectResponse
from pydantic import BaseModel, Field
import database

app = FastAPI(title="FastAPI‑Todo‑API", version="1.1.0")

database.init_db()

# ----- Pydantic Schemas -----
class TaskCreate(BaseModel):
    title: str = Field(..., min_length=1, max_length=100)
    description: str = Field("", max_length=255)

class Task(TaskCreate):
    id: int

# ----- Root Redirect -----
@app.get("/", include_in_schema=False)
def root():
    """Render free plan 健康檢查 & 自動跳轉 Swagger UI"""
    return RedirectResponse(url="/docs")

# ----- CRUD Routes -----
@app.post("/tasks", response_model=Task, status_code=status.HTTP_201_CREATED)
def create_task(task: TaskCreate):
    return database.add_task(task.title, task.description)

@app.get("/tasks", response_model=list[Task])
def get_tasks():
    return database.get_all_tasks()

@app.get("/tasks/{task_id}", response_model=Task)
def get_task(task_id: int):
    task = database.get_task_by_id(task_id)
    if task:
        return task
    raise HTTPException(status_code=404, detail="Task not found")

@app.put("/tasks/{task_id}", response_model=Task)
def update_task(task_id: int, payload: TaskCreate):
    updated = database.update_task(task_id, payload.title, payload.description)
    if updated:
        return updated
    raise HTTPException(status_code=404, detail="Task not found")

@app.delete("/tasks/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(task_id: int):
    if database.delete_task(task_id):
        return  # 204 No Content
    raise HTTPException(status_code=404, detail="Task not found")
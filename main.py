from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.responses import RedirectResponse
import database

app = FastAPI()
database.init_db()

class Task(BaseModel):
    title: str
    description: str = ""

@app.get("/tasks")
def get_tasks():
    return database.get_all_tasks()

@app.post("/tasks")
def create_task(task: Task):
    return database.add_task(task.title, task.description)

@app.get("/tasks/{task_id}")
def get_task(task_id: int):
    task = database.get_task_by_id(task_id)
    if task:
        return task
    raise HTTPException(status_code=404, detail="Task not found")

@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    success = database.delete_task(task_id)
    if success:
        return {"message": "Task deleted"}
    raise HTTPException(status_code=404, detail="Task not found")

@app.get("/")
def root():
    return RedirectResponse(url="/docs")


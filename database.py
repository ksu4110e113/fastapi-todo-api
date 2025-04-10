import sqlite3
from contextlib import closing, contextmanager
from pathlib import Path

DB_NAME = "todo.db"

@contextmanager
def get_conn():
    conn = sqlite3.connect(DB_NAME, check_same_thread=False)
    try:
        yield conn
    finally:
        conn.close()

def init_db():
    Path(DB_NAME).touch(exist_ok=True)
    with get_conn() as conn, closing(conn.cursor()) as cur:
        cur.execute(
            """
            CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                description TEXT
            )
            """
        )
        conn.commit()

# ---------- CRUD helpers ----------

def _row_to_dict(row: tuple) -> dict:
    return {"id": row[0], "title": row[1], "description": row[2]}


def add_task(title: str, description: str) -> dict:
    with get_conn() as conn, closing(conn.cursor()) as cur:
        cur.execute(
            "INSERT INTO tasks (title, description) VALUES (?, ?)",
            (title, description),
        )
        conn.commit()
        return {"id": cur.lastrowid, "title": title, "description": description}


def get_all_tasks() -> list[dict]:
    with get_conn() as conn, closing(conn.cursor()) as cur:
        cur.execute("SELECT id, title, description FROM tasks")
        return [_row_to_dict(r) for r in cur.fetchall()]


def get_task_by_id(task_id: int) -> dict | None:
    with get_conn() as conn, closing(conn.cursor()) as cur:
        cur.execute(
            "SELECT id, title, description FROM tasks WHERE id = ?", (task_id,)
        )
        row = cur.fetchone()
        return _row_to_dict(row) if row else None


def update_task(task_id: int, title: str, description: str) -> dict | None:
    with get_conn() as conn, closing(conn.cursor()) as cur:
        cur.execute(
            "UPDATE tasks SET title = ?, description = ? WHERE id = ?",
            (title, description, task_id),
        )
        conn.commit()
        if cur.rowcount:
            return {"id": task_id, "title": title, "description": description}
        return None


def delete_task(task_id: int) -> bool:
    with get_conn() as conn, closing(conn.cursor()) as cur:
        cur.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
        conn.commit()
        return bool(cur.rowcount)

import sqlite3
import os

DB_NAME = "todo.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT
        )
    ''')
    conn.commit()
    conn.close()

def get_all_tasks():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT id, title, description FROM tasks")
    rows = cursor.fetchall()
    conn.close()
    return [{"id": row[0], "title": row[1], "description": row[2]} for row in rows]

def add_task(title, description):
    print("🔍 資料庫路徑：", os.path.abspath(DB_NAME))
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO tasks (title, description) VALUES (?, ?)", (title, description))
    conn.commit()
    task_id = cursor.lastrowid
    cursor.execute("SELECT * FROM tasks")
    print("📝 資料庫內容：", cursor.fetchall())
    conn.close()
    return {"id": task_id, "title": title, "description": description}

def get_task_by_id(task_id):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT id, title, description FROM tasks WHERE id = ?", (task_id,))
    row = cursor.fetchone()
    conn.close()
    if row:
        return {"id": row[0], "title": row[1], "description": row[2]}
    return None

def delete_task(task_id):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
    conn.commit()
    affected = cursor.rowcount
    conn.close()
    return affected > 0

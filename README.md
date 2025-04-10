# FastAPI Todo List API 📝

這是一個用 **FastAPI + SQLite** 開發的簡易任務管理 API，支援基本 CRUD 功能，並使用 Swagger UI 提供測試介面。適合作為後端學習的入門練習專案。

---

## 🚀 功能 Features

- 建立任務（POST `/tasks`）
- 取得所有任務（GET `/tasks`）
- 查詢單一任務（GET `/tasks/{id}`）
- 刪除任務（DELETE `/tasks/{id}`）

---

## 🧱 技術堆疊 Stack

- Python 3.10+
- [FastAPI](https://fastapi.tiangolo.com/)
- SQLite（原生 `sqlite3` 模組）
- Swagger UI（FastAPI 自動產生文件）
- Uvicorn（啟動伺服器）

---

## 📦 專案架構


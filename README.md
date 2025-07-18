# FastAPI Todo List API 📋

一個簡潔、高效的任務管理 REST API，基於 **FastAPI** 和 **SQLite** 開發。提供完整的任務管理功能，適合作為後端開發學習或快速搭建專案原型。

## ✨ 特色

- 🚀 **高效能** – 基於 FastAPI 的現代 ASGI 框架
- 📱 **API 文檔** - 整合 Swagger UI 的互動式文件
- 🔄 **完整 CRUD** - 支援所有任務管理操作
- 🧪 **介面簡潔，日後易於撰寫測試** - 簡潔的 API 介面設計

## 📋 API 端點

| 方法 | 路徑 | 說明 |
|------|------|------|
| `GET` | `/tasks` | 獲取所有任務清單 |
| `POST` | `/tasks` | 新增任務 |
| `GET` | `/tasks/{id}` | 獲取特定任務詳情 |
| `DELETE` | `/tasks/{id}` | 刪除指定任務 |
| `PUT` | `/tasks/{id}` | 更新任務（標題、描述） |
| `GET` | `/` | 自動導向 Swagger UI |

## 🛠️ 技術棧

- **Python 3.10+**
- **FastAPI** - 現代、高效的 Python Web 框架
- **SQLite** - 輕量級關聯式資料庫
- **Pydantic** - 資料驗證與設定管理
- **Uvicorn** - ASGI 伺服器

## 🗂️ 專案結構

```
fastapi-todo/
├── main.py          # API 路由與主程式
├── database.py      # 資料庫操作邏輯
├── todo.db          # SQLite 資料庫（自動生成）
├── requirements.txt # 專案依賴
├── .gitignore       # Git 忽略配置
└── README.md        # 專案文檔
```

## 🚀 快速開始

### 安裝與設置

```bash
# 複製專案
git clone https://github.com/ksu4110e113/fastapi-todo-api.git
cd fastapi-todo-api

# 建立虛擬環境
python -m venv venv

# 啟動虛擬環境
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows

# 安裝依賴
pip install -r requirements.txt
```

### 啟動伺服器

```bash
uvicorn main:app --reload
```

### 使用 API

開啟瀏覽器訪問：
- API 文檔：http://127.0.0.1:8000/docs

## 📈 未來規劃

- ~~✅ **更新功能** – 實現任務編輯功能 (`PUT /tasks/{id}`)~~
- 🔐 **用戶認證** - 整合 JWT 登入機制
- 🗄️ **資料庫升級** - 遷移至 PostgreSQL
- ☁️ **雲端部署** - 部署至 Render 或 Railway
- 🖥️ **前端整合** - 開發配套的前端應用 (React/Vue)

## 🔍 API 示例

### 建立任務

```bash
curl -X 'POST' \
  'http://127.0.0.1:8000/tasks' \
  -H 'Content-Type: application/json' \
  -d '{
  "title": "學習 FastAPI",
  "description": "完成線上教程並實作一個專案"
}'
```

---

## 🌐 線上 Demo（已驗證）

> 本專案曾部署至 Render 測試，若服務剛好處於 Sleep 狀態，首次喚醒約需 30–60 秒。

🔗 https://fastapi-todo-api-0ejl.onrender.com/docs/

---

## 🗒️ 版本紀錄

- **v1.0.0** – 初版：CRUD、SQLite、Render 部署
- **v1.1.0** – 新增 `PUT /tasks/{id}` 更新任務

## 👨‍💻 關於作者

- GitHub: [@ksu4110e113](https://github.com/ksu4110e113)

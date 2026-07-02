# Mini Blog API

一个轻量级的个人博客 API，基于 FastAPI + SQLite 实现。

## 技术栈

- **框架**: FastAPI
- **数据库**: SQLite (SQLAlchemy ORM)
- **运行环境**: Python 3.12

## 安装

```bash
# 创建虚拟环境
uv venv --python 3.12

# 激活虚拟环境
.venv\Scripts\activate.ps1

# 安装依赖
uv pip install fastapi uvicorn sqlalchemy pytest httpx
```

## 运行

```bash
uv run uvicorn app.main:app --reload
```

服务启动后访问 http://127.0.0.1:8000

- API 文档 (Swagger): http://127.0.0.1:8000/docs
- API 文档 (ReDoc): http://127.0.0.1:8000/redoc

## API 接口

| 方法 | 路径 | 说明 |
|------|------|------|
| GET | /api/posts?page=1&page_size=10 | 获取文章列表（分页） |
| GET | /api/posts/{id} | 获取单篇文章 |
| POST | /api/posts | 创建文章 |
| PUT | /api/posts/{id} | 更新文章 |
| DELETE | /api/posts/{id} | 删除文章 |

### 使用示例

```bash
# 创建文章
curl.exe -X POST "http://127.0.0.1:8000/api/posts" ^
  -H "Content-Type: application/json" ^
  -d "{\"title\": \"我的第一篇博客\", \"content\": \"内容\"}"

# 获取文章列表
curl.exe "http://127.0.0.1:8000/api/posts"

# 获取单篇文章
curl.exe "http://127.0.0.1:8000/api/posts/1"

# 更新文章
curl.exe -X PUT "http://127.0.0.1:8000/api/posts/1" ^
  -H "Content-Type: application/json" ^
  -d "{\"title\": \"新标题\", \"content\": \"新内容\"}"

# 删除文章
curl.exe -X DELETE "http://127.0.0.1:8000/api/posts/1"
```

## 测试

```bash
uv run pytest tests/ -v
```

## 项目结构

```
mini-blog-api-base-in-fastapi/
├── app/
│   ├── __init__.py
│   ├── main.py          # FastAPI 应用入口
│   ├── database.py      # 数据库连接配置
│   ├── models.py        # SQLAlchemy 模型
│   ├── schemas.py       # Pydantic 数据模型
│   └── routers/
│       ├── __init__.py
│       └── posts.py     # 文章路由
├── tests/
│   ├── __init__.py
│   └── test_posts.py   # 接口测试
├── blog.db              # SQLite 数据库文件（运行后自动生成）
├── design.md            # 设计文档
├── plan.md              # 实现计划
└── README.md
```

# 实现计划

## 步骤 1：初始化项目环境
- 使用 `uv` 创建 Python 3.12 虚拟环境
- 安装依赖：fastapi, uvicorn, sqlalchemy

## 步骤 2：创建项目结构
- 创建 `app/` 包目录
- 创建 `app/routers/` 子包目录

## 步骤 3：实现数据库配置
- `app/database.py` — SQLite 连接配置，SQLAlchemy engine 和 SessionLocal

## 步骤 4：实现数据模型
- `app/models.py` — Post 模型（id, title, content, created_at, updated_at）

## 步骤 5：实现 Pydantic schemas
- `app/schemas.py` — PostCreate, PostUpdate, PostResponse, PaginatedPosts

## 步骤 6：实现文章路由
- `app/routers/posts.py` — 5 个 RESTful 接口

## 步骤 7：实现应用入口
- `app/main.py` — FastAPI 应用，注册路由

## 步骤 8：运行测试
- 启动 uvicorn 服务
- 测试各接口

# 个人博客 API 设计文档

## 概述
一个轻量级的个人博客 API，基于 FastAPI + SQLite 实现，无需用户认证，无需评论功能。

## 技术栈
- **框架**: FastAPI
- **数据库**: SQLite (通过 SQLAlchemy ORM)
- **运行环境**: Python 3.12 (uv 虚拟环境)

## 功能需求

### 文章 (Posts)
- 创建文章
- 获取文章列表（支持分页）
- 获取单篇文章详情
- 更新文章
- 删除文章

### 文章字段
| 字段 | 类型 | 说明 |
|------|------|------|
| id | Integer | 主键，自增 |
| title | String(200) | 文章标题 |
| content | Text | 文章内容 (Markdown) |
| created_at | DateTime | 创建时间 |
| updated_at | DateTime | 更新时间 |

## API 接口设计

| 方法 | 路径 | 说明 |
|------|------|------|
| GET | /api/posts | 获取文章列表（分页） |
| GET | /api/posts/{id} | 获取单篇文章 |
| POST | /api/posts | 创建文章 |
| PUT | /api/posts/{id} | 更新文章 |
| DELETE | /api/posts/{id} | 删除文章 |

### 请求/响应示例

**POST /api/posts**
```json
{
  "title": "文章标题",
  "content": "文章内容（支持 Markdown）"
}
```

**响应**
```json
{
  "id": 1,
  "title": "文章标题",
  "content": "文章内容（支持 Markdown）",
  "created_at": "2026-07-02T12:00:00",
  "updated_at": "2026-07-02T12:00:00"
}
```

**GET /api/posts?page=1&page_size=10**
```json
{
  "items": [
    {
      "id": 1,
      "title": "文章标题",
      "content": "文章内容",
      "created_at": "2026-07-02T12:00:00",
      "updated_at": "2026-07-02T12:00:00"
    }
  ],
  "total": 1,
  "page": 1,
  "page_size": 10
}
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
├── design.md
├── plan.md
└── README.md
```

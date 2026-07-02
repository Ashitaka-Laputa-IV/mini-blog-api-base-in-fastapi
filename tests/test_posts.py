from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


class TestPosts:
    def test_create_post(self):
        response = client.post(
            "/api/posts",
            json={"title": "测试文章", "content": "这是测试内容"},
        )
        assert response.status_code == 201
        data = response.json()
        assert data["title"] == "测试文章"
        assert data["content"] == "这是测试内容"
        assert "id" in data
        assert "created_at" in data
        assert "updated_at" in data

    def test_list_posts(self):
        # 先创建两篇文章
        client.post("/api/posts", json={"title": "文章A", "content": "内容A"})
        client.post("/api/posts", json={"title": "文章B", "content": "内容B"})

        response = client.get("/api/posts")
        assert response.status_code == 200
        data = response.json()
        assert data["total"] >= 2
        assert len(data["items"]) >= 2
        assert data["page"] == 1
        assert data["page_size"] == 10
        # 按时间倒序，文章B应该在文章A前面
        assert data["items"][0]["title"] == "文章B"

    def test_list_posts_pagination(self):
        response = client.get("/api/posts?page=1&page_size=1")
        assert response.status_code == 200
        data = response.json()
        assert data["page"] == 1
        assert data["page_size"] == 1
        assert len(data["items"]) == 1

    def test_get_post(self):
        # 先创建一篇文章
        create_resp = client.post(
            "/api/posts", json={"title": "获取测试", "content": "获取内容"}
        )
        post_id = create_resp.json()["id"]

        response = client.get(f"/api/posts/{post_id}")
        assert response.status_code == 200
        data = response.json()
        assert data["title"] == "获取测试"
        assert data["content"] == "获取内容"
        assert data["id"] == post_id

    def test_get_post_not_found(self):
        response = client.get("/api/posts/99999")
        assert response.status_code == 404
        assert response.json()["detail"] == "Post not found"

    def test_update_post(self):
        # 先创建
        create_resp = client.post(
            "/api/posts", json={"title": "更新前", "content": "旧内容"}
        )
        post_id = create_resp.json()["id"]

        response = client.put(
            f"/api/posts/{post_id}",
            json={"title": "更新后", "content": "新内容"},
        )
        assert response.status_code == 200
        data = response.json()
        assert data["title"] == "更新后"
        assert data["content"] == "新内容"
        # updated_at 应该更新了
        assert data["updated_at"] != data["created_at"]

    def test_update_post_not_found(self):
        response = client.put(
            "/api/posts/99999",
            json={"title": "不存在", "content": "不存在"},
        )
        assert response.status_code == 404

    def test_delete_post(self):
        # 先创建
        create_resp = client.post(
            "/api/posts", json={"title": "待删除", "content": "将被删除"}
        )
        post_id = create_resp.json()["id"]

        response = client.delete(f"/api/posts/{post_id}")
        assert response.status_code == 204

        # 确认已删除
        get_resp = client.get(f"/api/posts/{post_id}")
        assert get_resp.status_code == 404

    def test_delete_post_not_found(self):
        response = client.delete("/api/posts/99999")
        assert response.status_code == 404

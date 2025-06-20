import pytest
import httpx

BASE_URL = "http://127.0.0.1:8000"

@pytest.mark.asyncio
async def test_submit_data():
    payload = {
        "beauty_title": "пер.",
        "title": "Тестовый перевал",
        "other_titles": "Testovyi",
        "connect": "с перевалом Y",
        "add_time": "2024-01-01T12:00:00",
        "user": {
            "email": "test@example.com",
            "phone": "+79001112233",
            "fam": "Иванов",
            "name": "Иван",
            "otc": "Иванович"
        },
        "coords": {
            "latitude": 45.123,
            "longitude": 42.123,
            "height": 1234
        },
        "level": {
            "winter": "1A",
            "summer": "1B",
            "autumn": None,
            "spring": None
        },
        "images": [
            {"image_url": "http://example.com/img1.jpg", "title": "Фото 1"},
            {"image_url": "http://example.com/img2.jpg", "title": "Фото 2"}
        ]
    }

    async with httpx.AsyncClient(base_url=BASE_URL) as client:
        response = await client.post("/submitData", json=payload)
        assert response.status_code == 200
        json_data = response.json()
        print(json_data)
        assert json_data["status"] == 200
        assert "id" in json_data
        global last_id
        last_id = json_data["id"]

@pytest.mark.asyncio
async def test_get_pereval():
    async with httpx.AsyncClient(base_url=BASE_URL) as client:
        response = await client.get(f"/submitData/{last_id}")
        assert response.status_code == 200
        data = response.json()
        assert data["title"] == "Тестовый перевал"

@pytest.mark.asyncio
async def test_update_pereval():
    updated_payload = {
        "beauty_title": "пер. обновлённый",
        "title": "Тестовый перевал",
        "other_titles": "Обновлённое имя",
        "connect": "новая связка",
        "add_time": "2024-02-02T12:00:00",
        "user": {
            "email": "test@example.com",
            "phone": "+79001112233",
            "fam": "Иванов",
            "name": "Иван",
            "otc": "Иванович"
        },
        "coords": {
            "latitude": 45.555,
            "longitude": 42.555,
            "height": 1500
        },
        "level": {
            "winter": "2A",
            "summer": "2B",
            "autumn": None,
            "spring": None
        },
        "images": [
            {"image_url": "http://example.com/img3.jpg", "title": "Новое фото"}
        ]
    }

    async with httpx.AsyncClient(base_url=BASE_URL) as client:
        response = await client.patch(f"/submitData/{last_id}", json=updated_payload)
        assert response.status_code == 200
        json_data = response.json()
        assert json_data["state"] == 1

@pytest.mark.asyncio
async def test_get_by_email():
    async with httpx.AsyncClient(base_url=BASE_URL) as client:
        response = await client.get("/submitData/?user__email=test@example.com")
        assert response.status_code == 200
        data = response.json()
        assert isinstance(data, list)
        assert any(p["title"] == "Тестовый перевал" for p in data)

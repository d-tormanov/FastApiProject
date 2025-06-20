import pytest
import httpx

BASE_URL = "http://127.0.0.1:8000"

@pytest.mark.asyncio
@pytest.mark.parametrize("invalid_payload, expected_status", [
    ({}, 422),  # completely empty
    ({
        "title": "No user",  # missing required user
        "coords": {"latitude": 45.0, "longitude": 42.0, "height": 1200},
        "level": {"winter": "1A"},
        "images": []
    }, 422),
    ({
        "title": "No coords",
        "user": {
            "email": "bad@example.com",
            "phone": "123",
            "fam": "Bad",
            "name": "Tester",
            "otc": "Bot"
        },
        "level": {"winter": "1A"},
        "images": []
    }, 422),
    ({
        "title": "Invalid email",
        "user": {
            "email": "not-an-email",
            "phone": "123",
            "fam": "Bad",
            "name": "Tester",
            "otc": "Bot"
        },
        "coords": {"latitude": 45.0, "longitude": 42.0, "height": 1200},
        "level": {"winter": "1A"},
        "images": []
    }, 422),
])
async def test_submit_validation_errors(invalid_payload, expected_status):
    async with httpx.AsyncClient(base_url=BASE_URL) as client:
        response = await client.post("/submitData", json=invalid_payload)
        assert response.status_code == expected_status

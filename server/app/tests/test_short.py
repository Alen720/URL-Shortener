def test_create_short_link(client):
    response = client.post(
        "/api/shorten",
        json={"original_url": "https://example.com"}
    )

    assert response.status_code == 201
    data = response.json()

    assert "short_code" in data

    assert len(data["short_code"]) == 6

    assert data["original_url"] == "https://example.com/"

def test_get_all_links(client):
    client.post(
        "/api/shorten",
        json={"original_url": "https://python.org"}
    )

    response = client.get("/api/link")

    assert response.status_code == 200
    data = response.json()

    assert isinstance(data, list)
    assert len(data) == 1
    assert data[0]["original_url"] == "https://python.org/"
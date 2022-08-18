import requests

for _ in range(10):
    response = requests.get("http://localhost:6999/run_worker")
    assert response.status_code == 200

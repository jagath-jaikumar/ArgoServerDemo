import requests

response = requests.get("http://localhost:6999/run_worker")
assert response.status_code == 200

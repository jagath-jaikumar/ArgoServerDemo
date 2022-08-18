import couler.argo as couler
from couler.argo_submitter import ArgoSubmitter
from fastapi import FastAPI

app = FastAPI()


@app.get("/run_worker")
def run_worker():
    container_settings = {
        "image": "localhost:5000/argo-test-ml-worker",
        "command": ["python"],
        "args": ["-u", "main.py"],
        "step_name": "test",
    }
    couler.run_container(**container_settings)
    couler.config_workflow(name="test")
    submitter = ArgoSubmitter(namespace="argo")
    couler.run(submitter=submitter)

    return {"status": "success"}

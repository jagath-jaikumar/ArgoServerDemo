# import couler.argo as couler
# from couler.argo_submitter import ArgoSubmitter
# from fastapi import FastAPI

# app = FastAPI()


# @app.get("/run_worker")
# def run_worker():
#     container_settings = {
#         "image": "localhost:5000/argo-test-ml-worker",
#         "command": ["python"],
#         "args": ["-u", "main.py"],
#         "step_name": "test",
#     }
#     couler.run_container(**container_settings)
#     couler.config_workflow(name="test")
#     submitter = ArgoSubmitter(namespace="argo")
#     couler.run(submitter=submitter)

#     return {"status": "success"}

from fastapi import FastAPI
from hera import Task, Workflow, WorkflowService, Resources, ImagePullPolicy
from uuid import uuid4

app = FastAPI()

token = ""


def say(m: str):
    print(m)


@app.get("/run_worker")
def run_worker():
    with Workflow(
        f"test-{str(uuid4())[:8]}",
        service=WorkflowService(
            host="",
            verify_ssl=False,
            token=token,
        ),
        namespace="argo",
    ) as w:
        Task(
            "dummy-ml-model",
            image="localhost:5000/argo-test-ml-worker",
            image_pull_policy=ImagePullPolicy.Never,
            command=["python", "-u", "main.py"],
            resources=Resources(min_mem="2Gi"),
        )

    w.create()

    return {"status": "success"}

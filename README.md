# Argo tester

## Setup

Docker Desktop Kubernetes, Skaffold, and Kubectl installed on MacOS

```
kubectl create ns argo
kubectl apply -n argo -f https://raw.githubusercontent.com/argoproj/argo-workflows/master/manifests/quick-start-postgres.yaml

docker run -d -p 5000:5000 --restart=always --name registry registry:2

skaffold dev -d localhost:5000 # blocking

kubectl -n argo port-forward deployment/argo-server 2746:2746 # blocking

# Test Single: 
python single_runner.py

# Test Multiple:
python multi_runner.py
```





## Useful Scripts

docker build -t localhost:5000/argo-test-ml-worker:latest -f ml-worker/Dockerfile ml-worker
docker push localhost:5000/argo-test-ml-worker:latest
docker run localhost:5000/argo-test-ml-worker:latest


kubectl -n argo port-forward deployment/argo-server 2746:2746
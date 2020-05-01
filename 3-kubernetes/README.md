# 3-kubernetes

## Prerequisites
```bash
brew install minikube
```

## Get Started
```bash
minikube start

kubectl get deployments,pods

kubectl create deployment predictor --image=docker.io/chck/container-tutorial:1.3

kubectl logs $POD_NAME

kubectl set env deployment predictor MODEL_PATH=https://storage.googleapis.com/ailab-users/chck/tutorial/model_20191215.pkl.gz

kubectl get deployments,pods

kubectl logs $POD_NAME

kubectl expose deployment predictor --type=NodePort --port=8000

kubectl get deployments,pods,services

minikube service predictor --url

open $URL

kubectl scale --replicas=3 deployment predictor

kubectl get deployments,pods

kubectl set env deployment.apps/predictor MODEL_PATH=https://storage.googleapis.com/ailab-users/chck/tutorial/model_20200401.pkl.gz

kubectl get deployments,pods

open $URL

kubectl delete service predictor

kubectl delete deployment predictor

kubectl get deployments,pods,services

minikube stop
```

## STEP 1 - Create a PVC
file used: as88662-test-redis-pvc.yml
command used: kubectl apply -f as88662-test-redis-pvc.yml
output: prsistentvolumeclaim/as88662-tst-redis-pvc-data created

## STEP 2 - Create a deployment for the redis database
file used: as88662-test-redis-deployment.yml
command used: kubectl apply -f as88662-test-redis-deployment.yml
output: deployment.apps/as88662-test-pvc-deployment created

## STEP 3 - Create a service for the redis database
file used: as88662-test-redis-service.yml
command used: kubectl apply -f as88662-test-redis-service.yml
output: service/as88662-test-redis-service created

## CHECK STEPS 1 TO 3
file used: as88662-test-debug.yml
command used: kubectl get services
output:
```
NAME                         TYPE        CLUSTER-IP       EXTERNAL-IP   PORT(S)          AGE
app1                         NodePort    10.110.162.23    <none>        5000:32244/TCP   27d
as88662-test                 ClusterIP   10.107.218.62    <none>        6408/TCP         10d
as88662-test-flask-service   ClusterIP   10.111.54.72     <none>        5000/TCP         9d
as88662-test-redis-service   ClusterIP   10.101.75.200    <none>        6379/TCP         9d
hello-service                ClusterIP   10.102.189.226   <none>        5000/TCP         22d
```
command used: kubectl get pods --selector "app=py-app"
output:
```
NAME                                   READY   STATUS    RESTARTS   AGE
py-debug-deployment-5cc8cdd65f-srrwm   1/1     Running   1          22d
```
commands and outputs:
```
[as88662@isp02 homework06]$ kubectl exec -it py-debug-deployment-5cc8cdd65f-srrwm -- /bin/bash
root@py-debug-deployment-5cc8cdd65f-srrwm:/# pip3 install redis
Requirement already satisfied: redis in /usr/local/lib/python3.9/site-packages (3.5.3)
root@py-debug-deployment-5cc8cdd65f-srrwm:/# python3
Python 3.9.4 (default, Apr 10 2021, 15:31:19)
[GCC 8.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import redis
>>> rd=redis.StrictRedis(host='10.101.75.200', port=6379, db=8)
>>> rd.set('checking', 'it works')
True
```

In a seperate shell, commands and their outputs:
```
[as88662@isp02 homework06]$ kubectl get pods --selector "app=as88662-test-redis"
NAME                                          READY   STATUS    RESTARTS   AGE
as88662-test-pvc-deployment-6f49b5957-49mqx   1/1     Running   0          9d
[as88662@isp02 homework06]$ kubectl delete pods as88662-test-pvc-deployment-6f49b5957-49mqx
pod "as88662-test-pvc-deployment-6f49b5957-49mqx" deleted
```
Confirm that a new redis pod is created, command and output:
```
[as88662@isp02 homework06]$ kubectl get pods --selector "app=as88662-test-redis"
NAME                                          READY   STATUS    RESTARTS   AGE
as88662-test-pvc-deployment-6f49b5957-wkx79   1/1     Running   0          88s
```
Check if you can get the key inside the debug container
```
>>> rd.get('checking')
b'it works'
```

## STEP 4
Create deployment for flask API
file used: as88662-test-flask-deployment.yml
command used: kubectl apply -f as88662-test-flask-deployment.yml
output: deployment.apps/as88662-test-flask-deployment created

## STEP 5
Create service for flask API
file used: as88662-test-flask-service.yml
command used: kubectl apply -f as88662-test-flask-service.yml
output: service/as88662-test-flask-service created

# ubuntu 16.04 + nginx + uwsgi + flask + supervisor

### eb init


```
eb init
```


### Create base image

```
docker build -t vandle-cp-potato-base -f BaseDockerfile .
docker push xxxxxx.dkr.ecr.ap-northeast-1.amazonaws.com/api-base:latest
```


### Config EB environment

Use AWS web console to configure environment.


### Create EB environment

```
eb create api-stg-$( date '+%Y%m%d%H%M' ) --cfg 20161228-01-stg-api
```


### Deploy source to EB

```
eb deploy api-stg-201612212222
```

# shift-creation
This repository is for developing shift creation system.


## Docker
In this project, we build three containers of docker.(Nuxt-frontend, Django-backend, PostgreSQL-DataBase) 

### Building　containers
```
docker-compose up -d
```
Please check that three containers are built correctly.
```
docker ps
```

### Starting Nuxt.js Server
First, access target container of nuxt(front).
```
docker-compose exec front bash
```
Next, setting for running server.
```
npm i
export NODE_OPTIONS=--openssl-legacy-provider
npm run dev
```
Check whether server is run　([localhost:3030](http://localhost:3030/))

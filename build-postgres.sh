docker build -f Dockerfile-postgres . -t postgres-write:1.0
docker run --network register-network --rm postgres-write:1.0
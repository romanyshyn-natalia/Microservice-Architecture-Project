docker build -f Dockerfile-patients-app . -t run_app:1.0
docker run -p 8080:8080 --network full-network --rm run_app:1.0

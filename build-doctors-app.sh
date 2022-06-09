docker build -f Dockerfile-doctors-app . -t run_doctor_app:1.0
docker run -p 8881:8881 --network full-network --rm run_doctor_app:1.0

docker network create my-cassandra-network

docker run --name cassandra-node1 --network my-cassandra-network -d cassandra:latest

sleep 60
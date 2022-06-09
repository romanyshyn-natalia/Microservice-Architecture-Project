docker network create full-network

docker run --name cassandra-node1 --network full-network -d cassandra:latest

docker run --name cassandra-node2 --network full-network -d -e CASSANDRA_SEEDS=cassandra-node1 cassandra:latest

sleep 60
# Microservice-Architecture-Project
The final project of Software Architecture course

Temporary instructions:
```
brew services start mongodb-community@5.0
```

```	
docker run --name test_postgres -p 5432:5432 -e POSTGRES_PASSWORD=postgres -d postgres

? docker exec -it test_postgres psql -U postgres
? create database test_db;
? \c test_db
? create schema test_schema;
```

Launch postgres client and patients service after that.

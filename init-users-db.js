db = db.getSiblingDB("users");
db['registered-users'].drop();

db['registered-users'].insertMany([
    {
        "username": "Daria_Omelkina",
        "email": "omelkina.n@ucu.edu.ua",
        "role": "Main Doctor",
        "password": "f7b39419b3f0dde181ec395d002e5090a45143740091ce3b6fa00d868e143b87"
    },
    {
        "username": "Nataliia_Romanyshyn",
        "email": "romanyshyn.n@ucu.edu.ua",
        "role": "Doctor",
        "password": "2373c24605d6af11bd4c3284912857072ce10f0b56f5c4112f2ee0636ef5a65a"
    },

]);

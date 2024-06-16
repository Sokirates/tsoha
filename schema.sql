CREATE TABLE areas (
    id SERIAL PRIMARY KEY, 
    topic TEXT NOT NULL, 
    created_at TIMESTAMP NOT NULL
);

CREATE TABLE messages (
    id SERIAL PRIMARY KEY,
    area_id INTEGER REFERENCES areas,
    message TEXT NOT NULL,
    created_at TIMESTAMP NOT NULL
);

CREATE TABLE users (
    id SERIAL PRIMARY KEY, 
    username TEXT NOT NULL, 
    password TEXT NOT NULL
);

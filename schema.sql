CREATE TABLE areas (
    id SERIAL PRIMARY KEY, 
    topic TEXT NOT NULL, 
    created_at TIMESTAMP NOT NULL,
    creator_id INTEGER REFERENCES users
);

CREATE TABLE messages (
    id SERIAL PRIMARY KEY,
    area_id INTEGER REFERENCES areas,
    message TEXT NOT NULL,
    created_at TIMESTAMP NOT NULL,
    sender_id INTEGER REFERENCES users
);

CREATE TABLE users (
    id SERIAL PRIMARY KEY, 
    username TEXT NOT NULL, 
    password TEXT NOT NULL
);

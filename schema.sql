CREATE TABLE users (
    id SERIAL PRIMARY KEY, 
    username TEXT NOT NULL, 
    password TEXT NOT NULL
);

CREATE TABLE areas (
    id SERIAL PRIMARY KEY, 
    topic TEXT NOT NULL, 
    created_at TIMESTAMP NOT NULL,
    creator TEXT
);

CREATE TABLE messages (
    id SERIAL PRIMARY KEY,
    area_id INTEGER REFERENCES areas ON DELETE CASCADE,
    message TEXT NOT NULL,
    created_at TIMESTAMP NOT NULL,
    sender TEXT
);

CREATE TABLE areas_likes (
    id SERIAL PRIMARY KEY,
    area_id INTEGER REFERENCES areas ON DELETE CASCADE,
    user_id INTEGER REFERENCES users ON DELETE CASCADE,
    likes INTEGER,
    liked_at TIMESTAMP NOT NULL
);
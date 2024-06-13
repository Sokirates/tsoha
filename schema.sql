CREATE TABLE areas (
    id SERIAL PRIMARY KEY, 
    topic TEXT, 
    created_at TIMESTAMP
);

CREATE TABLE messages (
    id SERIAL PRIMARY KEY,
    area_id INTEGER REFERENCES areas(id),
    message TEXT,
    created_at TIMESTAMP
);
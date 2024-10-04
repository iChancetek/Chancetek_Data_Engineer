CREATE TABLE IF NOT EXISTS sneakers (
    sneakerID VARCHAR(255) PRIMARY KEY,
    brand VARCHAR(255),
    model VARCHAR(255),
    size INT,
    price DECIMAL(10, 2),
    releaseDate DATE,
    color VARCHAR(255)
);
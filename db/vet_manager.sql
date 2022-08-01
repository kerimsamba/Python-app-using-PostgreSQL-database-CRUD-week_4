DROP TABLE pets;
DROP TABLE vets;
DROP TABLE owners;

CREATE TABLE vets (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(255),
    surname VARCHAR(255)
    );

CREATE TABLE owners (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(255),
    surname VARCHAR(255),
    telephone VARCHAR(255),
    email VARCHAR(255)
    );

CREATE TABLE pets (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    dob DATE,
    type VARCHAR(255),
    treatment_notes TEXT,
    vet_id INT REFERENCES vets(id) ON DELETE CASCADE,
    owner_id INT REFERENCES owners(id) ON DELETE CASCADE
);




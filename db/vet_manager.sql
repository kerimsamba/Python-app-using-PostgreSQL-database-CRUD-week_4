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
    surname VARCHAR(255)
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




-- CREATE TABLE visits (
--   id SERIAL PRIMARY KEY,
--   user_id INT REFERENCES users(id) ON DELETE CASCADE,
--   location_id INT NOT NULL REFERENCES locations(id) ON DELETE CASCADE,
--   review TEXT
-- );

-- name, dob, type, treatment_notes, vet_id = None, owner_id = None, id = None):
--         self.name = name
--         self.dob = dob
--         self.type = type
--         self.treatment_notes = treatment_notes
--         self.vet_id = vet_id
--         self.owner_id = owner_id
--         self.id = id
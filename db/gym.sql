DROP TABLE IF EXISTS gym_bookings;
DROP TABLE IF EXISTS gym_members;
DROP TABLE IF EXISTS gym_classes;

CREATE TABLE gym_classes (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    capacity INT
);

CREATE TABLE gym_members (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    age INT,
    phone_number INT,
    email VARCHAR(255)
);

    
CREATE TABLE gym_bookings (
  id SERIAL PRIMARY KEY,
  gym_class_id  INT REFERENCES gym_classes(id) ON DELETE CASCADE,
  gym_member_id INT REFERENCES gym_members(id) ON DELETE CASCADE,
  review TEXT
);
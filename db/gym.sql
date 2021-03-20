DROP TABLE IF EXISTS gym_bookings;
DROP TABLE IF EXISTS gym_members;
DROP TABLE IF EXISTS gym_classes;
DROP TABLE IF EXISTS gym_categories;


CREATE TABLE gym_members (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    age INT,
    address VARCHAR(255)
    phone_no INT,
    email VARCHAR(255)
    premium BOOLEAN,
    membership_no INT,
    is_active BOOLEAN
);

CREATE TABLE gym_classes (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255),
    duration VARCHAR(255),
    capacity INT,
    intensity VARCHAR(255),
    difficulty VARCHAR(255),
    date DATE,
    time TIME, 
    location VARCHAR(255)
);

CREATE TABLE gym_categories (
    id SERIAL PRIMARY KEY,
    category VARCHAR(255)
);
 
CREATE TABLE gym_bookings (
  id SERIAL PRIMARY KEY,
  gym_member_id INT REFERENCES gym_members(id) ON DELETE CASCADE,
  gym_class_id  INT REFERENCES gym_classes(id) ON DELETE CASCADE,
  gym_category_id  INT REFERENCES gym_categories(id) ON DELETE CASCADE,
  bookings INT,
  booked_count INT
);
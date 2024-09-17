USE ecommerce;

CREATE TABLE users(
    id integer not null auto_increment,
    first_name VARCHAR(100) not null,
    last_name VARCHAR(100) not null,
    age INT not null,
    PRIMARY KEY(id)
);

INSERT INTO users (first_name, last_name, age) VALUES ('Pedro', 'Cabral', 25)
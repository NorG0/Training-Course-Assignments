SELECT * FROM states;

SELECT 'Hello, World!';
SELECT first_name FROM people;
SELECT last_name FROM people;
SELECT first_name, last_name FROM people;
SELECT last_name, first_name FROM people;

SELECT * FROM people WHERE shirt_or_hat='hat';
SELECT first_name, last_name FROM people WHERE shirt_or_hat='shirt';
SELECT first_name, last_name, shirt_or_hat FROM people WHERE shirt_or_hat='shirt';
-- SELECT first_name, last_name, shirt_or_hat WHERE shirt_or_hat='shirt' FROM people;


SELECT first_name, last_name, state, company FROM people WHERE company LIKE '%LLC' LIMIT 5;
SELECT first_name, last_name, state, company FROM people WHERE company LIKE '%LLC' LIMIT 10;
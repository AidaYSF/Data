-- Question a: Total number of 
 by model by country
SELECT
    country,
    model,
    COUNT(*) AS total_cars
FROM
    cars
GROUP BY
    country, model;
-- Question b: Country with the most cars for each model
SELECT
    model,
    country,
    COUNT(*) AS total_cars
FROM
    cars
GROUP BY
    model, country
ORDER BY
    model, total_cars DESC
LIMIT 1;
-- Question c: Models sold in the USA but not in France
SELECT DISTINCT
    model
FROM
    cars
WHERE
    country = 'USA'
EXCEPT
SELECT DISTINCT
    model
FROM
    cars
WHERE
    country = 'France';
-- Question d: Average car costs in every country by engine type
SELECT
    country,
    engine_type,
    AVG(price) AS average_cost
FROM
    cars
GROUP BY
    country, engine_type;

-- Question e: Average ratings of electric cars vs thermal cars
SELECT
    engine_type,
    AVG(rating) AS average_rating
FROM
    cars
GROUP BY
    engine_type;

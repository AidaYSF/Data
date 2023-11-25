-- Question a: Total number of cars by model by country
SELECT
    c."Model",
    c."Country",
    COUNT(*) AS total_cars
FROM
    consumers AS c
GROUP BY
    c."Model", c."Country"
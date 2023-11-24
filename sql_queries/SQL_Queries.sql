-- Question a: Total number of cars by model by country
SELECT
    c."Model",
    c."Country",
    COUNT(*) AS total_cars
FROM
    consumers AS c
GROUP BY
    c."Model", c."Country"

-- Model is sold in the USA but not in France.

SELECT DISTINCT
    "Model"
FROM
    consumers AS c_usa
WHERE
    "Country" = 'USA'
    AND NOT EXISTS (
        SELECT 1
        FROM
            consumers AS c_france
        WHERE
            c_france."Model" = c_usa."Model"
            AND c_france."Country" = 'France'
    );
	
-- Coût moyen arrondi de chaque voiture par pays, par type de moteur
SELECT
    "Country",
    "Engine Type",
    ROUND(AVG("Price"), 2) AS avg_car_cost
FROM
    consumers AS c
JOIN
    cars AS car ON c."Model" = car."Make"
GROUP BY
    "Country", "Engine Type";


-- Average ratings of electric cars vs. thermal cars
SELECT
    "Engine Type",
    ROUND(AVG("Review Score")) AS avg_rating
FROM
    consumers AS c
JOIN
    cars AS car ON c."Model" = car."Make"
WHERE
    car."Engine Type" IN ('Electric', 'Thermal')
GROUP BY
    "Engine Type";





	



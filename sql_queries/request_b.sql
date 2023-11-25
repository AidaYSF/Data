-- Question b: Country with the most cars for each model

WITH RankedCars AS (
    SELECT
        "Model",
        "Country",
        COUNT(*) AS total_cars,
        RANK() OVER (PARTITION BY "Model" ORDER BY COUNT(*) DESC) AS rnk
    FROM
        consumers
    GROUP BY
        "Model", "Country"
)

SELECT
    "Model",
    "Country",
    total_cars
FROM
    RankedCars
WHERE
    rnk = 1;

--the average car costs in every country by engine type.

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

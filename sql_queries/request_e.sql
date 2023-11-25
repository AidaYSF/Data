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

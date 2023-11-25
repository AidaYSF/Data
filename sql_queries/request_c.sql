
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
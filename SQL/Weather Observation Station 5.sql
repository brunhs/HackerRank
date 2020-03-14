(SELECT city, LENGTH(city) AS city_length
FROM STATION
ORDER BY city_length ASC, city
LIMIT 1
)
UNION
(SELECT city, LENGTH(city) AS city_length
FROM STATION
ORDER BY city_length DESC, city
LIMIT 1)
SELECT DISTINCT(city) as distinct_city
FROM STATION 
WHERE SUBSTRING(city, 1, 1) NOT IN ('a', 'e', 'i', 'o', 'u')
OR
SUBSTRING(city, -1, 1) NOT IN ('a', 'e', 'i', 'o', 'u')
ORDER BY distinct_city
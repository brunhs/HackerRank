SELECT 
CASE 
    WHEN A = B AND B = C AND A = C THEN 'Equilateral'
    WHEN (A = B AND A + B <= C) OR (B = C AND B + C <= A) OR (C = A AND C + A <= B) OR (A != B AND A + B <= C) THEN 'Not A Triangle'
    WHEN (A = B AND B != C) OR (A = C AND A != B) OR (B = C AND B != A) THEN 'Isosceles'
    WHEN (A != B AND A + B >= C) THEN 'Scalene'
END
FROM triangles;
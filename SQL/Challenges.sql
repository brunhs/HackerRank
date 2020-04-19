SELECT H.hacker_id, H.name, COUNT(C.challenge_id) as challenges_created 
FROM HACKERS H,
     CHALLENGES C
WHERE H.hacker_id = C.hacker_id
GROUP BY H.hacker_id, H.name
HAVING COUNT(C.challenge_id) IN
  (SELECT MAX(challenges_created)
   FROM
     (SELECT COUNT(*) AS challenges_created
      FROM CHALLENGES
      GROUP BY hacker_id))
OR COUNT(C.challenge_id) IN
  (SELECT challenges_created
   FROM
     (SELECT COUNT(*) AS challenges_created
      FROM CHALLENGES
      GROUP BY hacker_id)
   GROUP BY challenges_created
   HAVING COUNT(challenges_created)=1)
ORDER BY COUNT(C.challenge_id) DESC, H.hacker_id;

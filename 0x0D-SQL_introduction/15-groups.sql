-- Lists the number of records with the same score in secont_table
-- The result should display the score, and the number of records for this score
SELECT score, COUNT(*) AS number FROM second_table GROUP BY score ORDER BY number DESC;
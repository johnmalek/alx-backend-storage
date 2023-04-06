-- a script that ranks country of origin of bands
-- ranks by fans(non-unique)
SELECT origin, SUM(fans) AS nb_fans
FROM metal_bands
GROUP BY origin
ORDER BY nb_fans DESC;

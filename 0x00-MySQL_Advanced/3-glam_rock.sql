-- A script that lists all bands with Glam rock as main style
-- Lists by longevity
SELECT band_name, ABS(split - formed) AS lifespan
FROM metal_bands
WHERE style='Glam rock' > 0
ORDER BY lifespan DESC;

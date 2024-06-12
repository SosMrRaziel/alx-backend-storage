-- Go to the glam_rock table and select the band_name and formed columns.
SELECT band_name,
	ifnull(split, YEAR(CURDATE())) - formed as lifespan
FROM metal_bands
WHERE style LIKE "%Glam rock%"
ORDER BY lifespan DESC;

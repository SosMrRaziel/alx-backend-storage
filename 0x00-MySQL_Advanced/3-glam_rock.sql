-- Go to the glam_rock table and select the band_name and formed columns.
SELECT band_name, (IFNULL(split, 2020) - formed) AS lifespan
FROM metal_bands WHERE style LIKE '%Glam rock%'
ORDER BY lifespan  DESC;

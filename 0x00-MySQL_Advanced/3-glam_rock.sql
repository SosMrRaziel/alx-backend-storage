-- Go to the glam_rock table and select the band_name and formed columns.
SELECT band_name,
    if(split IS NOT NULL AND split !="", 2022 - formed, NULL) AS lifespan
FROM metal_bands
ORDER BY lifespan DESC;

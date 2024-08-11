SELECT 
    PERSONNAME AS athlete_name,
    COUNTRY AS athlete_country,
    DISCIPLINE AS athlete_discipline
FROM {{ source('olympic', 'ATHLETES') }}
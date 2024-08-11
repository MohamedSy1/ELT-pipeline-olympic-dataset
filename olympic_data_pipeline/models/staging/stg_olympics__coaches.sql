SELECT 
    NAME AS coach_name,
    COUNTRY AS coach_country,
    DISCIPLINE AS coach_discipline,
    EVENT AS coach_event
FROM {{ source('olympic', 'COACHES') }}

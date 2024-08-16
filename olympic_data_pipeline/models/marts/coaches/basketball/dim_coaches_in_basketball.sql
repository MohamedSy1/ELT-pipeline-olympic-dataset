WITH coach_info AS (
    SELECT *
    FROM {{ ref('stg_olympics__coaches') }}
)

SELECT 
    coach_country,
    COUNT(coach_name) AS num_coaches
FROM coach_info
WHERE coach_discipline = 'Basketball'
GROUP BY coach_country
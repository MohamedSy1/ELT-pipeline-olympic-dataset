WITH coach_info AS (
    SELECT 
        coach_country,
        coach_name
    FROM {{ ref('stg_olympics__coaches') }}
)

SELECT 
    coach_country,
    COUNT(coach_name) AS num_coaches
FROM coach_info
GROUP BY coach_country
ORDER BY num_coaches DESC
LIMIT 10
WITH gender_entries AS (
    SELECT *
    FROM {{ ref('stg_olympics__entriesgender') }}
),

coach_info AS (
    SELECT *
    FROM {{ ref('stg_olympics__coaches') }}
)

SELECT 
    c.coach_country AS team_country
FROM gender_entries eg
JOIN coach_info c
ON eg.entry_discipline = c.coach_discipline
WHERE c.coach_discipline = 'Basketball'
AND eg.male_entries > 0
GROUP BY team_country
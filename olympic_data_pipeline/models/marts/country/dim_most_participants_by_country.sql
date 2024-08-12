{{ 
    config (
        materialized='table'
    )
}}

with athletes as (
    SELECT * FROM {{ ref('stg_olympics__athletes') }}
)

SELECT
    athlete_country,
    COUNT(*) as athlete_count
FROM athletes
GROUP BY athlete_country
ORDER BY athlete_count DESC

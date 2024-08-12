{{ 
    config (
        materialized='table'
    )
}}

WITH athletes as (
    SELECT * FROM {{ ref("stg_olympics__athletes")}}
),

coaches as (
    SELECT * FROM {{ ref("stg_olympics__coaches") }}
),

entriesGender as (
    SELECT * FROM {{ ref("stg_olympics__entriesgender") }}
),

medals as (
    SELECT * FROM {{ ref("stg_olympics__medals") }}
)

SELECT 
    a.athlete_name,
    a.athlete_country,
    a.athlete_discipline,
    c.coach_name,
    c.coach_country,
    c.coach_discipline,
    c.coach_event,
    e.female_entries,
    e.male_entries,
    e.total_entries,
    m.team_country,
    m.gold_medals,
    m.silver_medals,
    m.bronze_medals,
    m.total_medals,
    m.rank_by_total
FROM athletes a
LEFT JOIN coaches c ON a.athlete_discipline = c.coach_discipline AND a.athlete_country = c.coach_country
LEFT JOIN entriesGender e ON a.athlete_discipline = e.entry_discipline
LEFT JOIN medals m ON a.athlete_country = m.team_country

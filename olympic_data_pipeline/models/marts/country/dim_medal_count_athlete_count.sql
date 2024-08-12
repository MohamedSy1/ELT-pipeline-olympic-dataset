WITH num_athletes AS (
    SELECT * FROM {{ ref("dim_most_participants_by_country") }}
),

total_medals AS (
    SELECT team_country, total_medals FROM {{ ref("stg_olympics__medals") }}
),

medal_on_player_count AS (
    SELECT * 
    FROM num_athletes 
    LEFT JOIN total_medals
    WHERE num_athletes.athlete_country = total_medals.team_country
)

SELECT * FROM medal_on_player_count

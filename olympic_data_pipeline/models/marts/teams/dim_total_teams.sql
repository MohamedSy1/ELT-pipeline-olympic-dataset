SELECT 
    team_country,
    COUNT(DISTINCT team_country) AS num_teams
FROM {{ ref('stg_olympics__medals') }}
GROUP BY team_country
SELECT 
    TEAMCOUNTRY AS team_country,
    GOLD AS gold_medals,
    SILVER AS silver_medals,
    BRONZE AS bronze_medals,
    TOTAL AS total_medals,
    RANK_BY_TOTAL AS rank_by_total
FROM {{ source('olympic', 'MEDALS') }}
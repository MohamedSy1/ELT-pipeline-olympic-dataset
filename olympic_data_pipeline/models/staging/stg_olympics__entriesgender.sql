SELECT 
    DISCIPLINE AS entry_discipline,
    FEMALE AS female_entries,
    MALE AS male_entries,
    TOTAL AS total_entries
FROM {{ source('olympic', 'ENTRIESGENDER') }}
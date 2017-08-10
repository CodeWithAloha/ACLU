# Schema

```
Lat, Lon -> Set of Rules

[
    {
        "unique_id": "112FB8F1-6E3B-42E1-9E75-2D18B87D826A",
        "organization": {
            "id": "3ADC097B-386A-4714-A5CC-FB518879D52B",
            "name": "Honolulu Police Department",
        },
        "name": "Sit-Lie Ban",
        "restrictions": {
            "time_of_day_start": "0800",
            "time_of_day_end": "1200",
            "effective_datetime_start": "2017-07-12 00:00:00Z",
            "effective_datetime_end": "2017-08-01 12:00:00Z",
            "day_of_week_restriction": ["M", "W"],
            "holiday_restrictions": ["state", "federal"]
        },
        "ownership": "city|state|private|federal|military"
        "geojson": "FEATURE_COLLECTION",
        "last_imported_at": "2017-07-07 00:00:00Z"
    },
    {
        "unique_id": "85DDDF26-C495-4F1B-8FA8-3A368826B2AD",
        "organization": {
            "id": "428A6F80-99C7-4334-BA45-E06139F0C5AA",
            "name": "Honolulu City and County",
        },
        "name": "Park Hours",
        "restrictions": {
            "time_of_day_start": "0800",
            "time_of_day_end": "1200",
            "effective_datetime_start": "2017-07-12 00:00:00Z",
            "effective_datetime_end": "2017-08-01 12:00:00Z",
            "day_of_week_restriction": ["M", "W"],
            "holiday_restrictions": ["state", "federal"]
        },
        "ownership": "city|state|private|federal|military"
        "geojson": "FEATURE_COLLECTION",
        "last_imported_at": "2017-07-07 00:00:00Z"
    }
]
```

# Testing plan for TimeTest

## Testing `__init__()`
### Equivalent Classes
- `year`
  - valid input --- positive integer n where (1950 <= n <= 2050)
  - valid type but invalid value --- integer outside the valid range
  - invalid type --- non-int input
- `month`
  - valid input --- positive integer n where (1 <= n <= 12)
  - valid type but invalid value --- integer outside the valid range
  - invalid type --- non-int input
- `day`
  - valid input --- positive integer n where (1 <= n <= 31)
  - valid type but invalid value --- integer outside the valid range
  - invalid type --- non-int input
- `hour`
  - valid input --- positive integer n where (0 <= n <= 23)
  - valid type but invalid value --- integer outside the valid range
  - invalid type --- non-int input
- `minute`
  - valid input --- positive integer n where (0 <= n <= 59)
  - valid type but invalid value --- integer outside the valid range
  - invalid type --- non-int input

### Combinatorial Testing
- Valid input for all parameters

| Parameter | Input Type | Input Value  |
|-----------|------------|--------------|
| year      | int        | positive int |
| month     | int        | positive int |
| day       | int        | positive int |
| hour      | int        | positive int |
| minute    | int        | positive int |

Expected result: Pass

- Invalid value for `year`

| Parameter | Input Type | Input Value                     |
|-----------|------------|---------------------------------|
| year      | int        | integer outside the valid range |
| month     | int        | positive int                    |
| day       | int        | positive int                    |
| hour      | int        | positive int                    |
| minute    | int        | positive int                    |

Expected result: Fail

- Invalid value for `month`
- 
| Parameter | Input Type | Input Value                     |
|-----------|------------|---------------------------------|
| year      | int        | positive int                    |
| month     | int        | integer outside the valid range |
| day       | int        | positive int                    |
| hour      | int        | positive int                    |
| minute    | int        | positive int                    |

Expected result: Fail

- Invalid value for `day`

| Parameter | Input Type | Input Value                     |
|-----------|------------|---------------------------------|
| year      | int        | positive int                    |
| month     | int        | positive int                    |
| day       | int        | integer outside the valid range |
| hour      | int        | positive int                    |
| minute    | int        | positive int                    |

Expected result: Fail

- Invalid value for `hour`

| Parameter | Input Type | Input Value                     |
|-----------|------------|---------------------------------|
| year      | int        | positive int                    |
| month     | int        | positive int                    |
| day       | int        | positive int                    |
| hour      | int        | integer outside the valid range |
| minute    | int        | positive int                    |

Expected result: Fail

- Invalid value for `minute`

| Parameter | Input Type | Input Value                      |
|-----------|------------|----------------------------------|
| year      | int        | positive int                     |
| month     | int        | positive int                     |
| day       | int        | positive int                     |
| hour      | int        | positive int                     |
| minute    | int        | integer outside the valid range  |

Expected result: Fail

- Invalid type for `year`

| Parameter | Input Type | Input Value   |
|-----------|------------|---------------|
| year      | non-int    | non-int value |
| month     | int        | positive int  |
| day       | int        | positive int  |
| hour      | int        | positive int  |
| minute    | int        | positive int  |

Expected result: Fail

- Invalid type for `month`

| Parameter | Input Type | Input Value    |
|-----------|------------|----------------|
| year      | int        | positive int   |
| month     | non-int    | non-int value  |
| day       | int        | positive int   |
| hour      | int        | positive int   |
| minute    | int        | positive int   |

Expected result: Fail

- Invalid type for `day`

| Parameter | Input Type | Input Value    |
|-----------|------------|----------------|
| year      | int        | positive int   |
| month     | int        | positive int   |
| day       | non-int    | non-int value  |
| hour      | int        | positive int   |
| minute    | int        | positive int   |

Expected result: Fail

- Invalid type for `hour`

| Parameter | Input Type  | Input Value    |
|-----------|-------------|----------------|
| year      | int         | positive int   |
| month     | int         | positive int   |
| day       | int         | positive int   |
| hour      | non-int     | non-int value  |
| minute    | int         | positive int   |

Expected result: Fail

- Invalid type for `hour`

| Parameter | Input Type | Input Value    |
|-----------|------------|----------------|
| year      | int        | positive int   |
| month     | int        | positive int   |
| day       | int        | positive int   |
| hour      | int        | positive int   |
| minute    | non-int    | non-int value  |

Expected result: Fail

## Testing `get_year()`
- Returns year of the time as an integer

## Testing `get_month()`
- Returns year of the time as an integer

## Testing `get_day()`
- Returns year of the time as an integer

## Testing `get_hour()`
- Returns year of the time as an integer

## Testing `get_minute()`
- Returns year of the time as an integer

## Testing `set_year()`
### Equivalent Classes
- positive int (Pass)
- integer outside the valid range (Fail)
- non-int (Fail)

## Testing `set_month()`
### Equivalent Classes
- positive int (Pass)
- integer outside the valid range (Fail)
- non-int (Fail)

## Testing `set_day()`
### Equivalent Classes
- positive int (Pass)
- integer outside the valid range (Fail)
- non-int (Fail)

## Testing `set_hour()`
### Equivalent Classes
- positive int (Pass)
- integer outside the valid range (Fail)
- non-int (Fail)

## Testing `set_minute()`
### Equivalent Classes
- positive int (Pass)
- integer outside the valid range (Fail)
- non-int (Fail)

## Testing `get_object()`
- Returns the Time object in the form of dictionary

## Testing` __str__()`
- Returns the string of time in the order of year, month, day, hour, minute
# Testing Plan for ReminderTest

## Testing `__init__()`

### Equivalent Classes
- `method`
  - valid str input --- "email" or "popup" (Pass)
  - invalid str input --- any str but "email" and "popup" (Fail)
  - invalid input type --- any input besides str
- `minutes`
  - valid int input --- any positive integer
  - invalid int input --- any non-positive integer
  - invalid input type --- any types besides int

### Combinatorial Testing
- Valid input for both parameter

| Parameter | Input Type | Input Value               |
|-----------|------------|---------------------------|
| method    | str        | either "email" or "popup" |
| minutes   | int        | positive integer          |

Expected result: Pass

- Valid input for `method`, invalid type for `minutes`

| Parameter | Input Type          | Input Value                   |
|-----------|---------------------|-------------------------------|
| method    | str                 | either "email" or "popup"     |
| minutes   | any type except int | any types of input except int |

Expected result: Fail

- Invalid value for `method`, valid input for `minutes`

| Parameter | Input Type | Input Value                         |
|-----------|------------|-------------------------------------|
| method    | str        | any str besides "email" and "popup" |
| minutes   | int        | positive integer                    |

Expected result: Fail

- Invalid type for `method`, valid input for `minutes`

| Parameter | Input Type          | Input Value          |
|-----------|---------------------|----------------------|
| method    | any type except str | any value except str |
| minutes   | int                 | positive integer     |

Expected result: Fail

- Valid input for `method`, invalid input value for `minutes`

| Parameter | Input Type | Input Value               |
|-----------|------------|---------------------------|
| method    | str        | either "email" or "popup" |
| minutes   | int        | any non-positive integer  |

Expected result: Fail


## Testing `get_method()`

- Returns method of the reminder as a str

## Testing `get-minutes()`

- Returns minutes before events as an integer

## Testing `set_method()`
### Equivalent Classes
- Valid input --- either "email" or "popup" (Pass)
- Valid type but Invalid value --- any str except "email" or "popup" (Fail)
- Invalid type --- any types except str (Fail)

## Testing `set_minutes()`
### Equivalent Classes
- Valid input --- positive integer (Pass)
- Valid type but Invalid value --- any non-positive integer (Fail)
- Invalid type --- any input except int (Fail)

## Testing `get_object()`

- Returns the Reminder object in a form of dictionary

## Testing `str()`

- Returns a string with information of reminding methods and minutes before events


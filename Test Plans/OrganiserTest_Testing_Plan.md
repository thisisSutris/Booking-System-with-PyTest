# Testing Plan fpr Organiser Test

## Testing `__init__()`

### Equivalent Classes
- `email`:
    - str input (Pass)
    - non-str input (Fail)
- `is_self`:
    - bool input (Pass)
    - No input (Pass)
    - non-bool input (Pass)

### Combinatorial Testing

### Valid Inputs for both parameters
| Parameter | Input Type |
|-----------|------------|
| email     | str        |
| is_self   | bool       |

Expected result:  Pass

### Invalid input for `email`, boolean input for `is_self`

| Parameter | Input Type |
|-----------|------------|
| email     | int        |
| is_self   | bool       |

Expected result: Fail

### str input for `email`, Invalid input for `is_self`

| Parameter | Input Type |
|-----------|------------|
| email     | str        |
| is_self   | int        |

Expected result: Fail

### Valid input for `email`, No input for `is_self`
| Parameter | Input Type |
|-----------|------------|
| email     | str        |
| is_self   | No input   |

Expected result: Pass

### Invalid input for `email`, No input for `is_self`

| Parameter | Input Type |
|-----------|------------|
| email     | int        |
| is_self   | No input   |

Expected result: Fail

## Testing `get_email()`
- Returns the email address as a str

## Testing `get_is_self()`
- Returns as a boolean value

## Test `set_email()`
### Equivalant Classes
- `email` --- str input (Pass)
- `email` --- non-str input (Fail)

## Test `get_object()`
- Correct object is given for the test Organiser

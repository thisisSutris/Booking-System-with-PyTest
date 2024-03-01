# Testing `init_address()` and `init_link()`

## Equivalence Classes

### `Street number`

- str input (Pass)
- Non-str input (Fail)

### `Street Name`

- str input (Pass)
- Non-str input (Fail)

### `Suburb`

- str input (Pass)
- Non-str input (Fail)

### `State`

- str input (Pass)
- Non-str input (Fail)

### `Postcode`

- str input (Pass)
- Non-str input (Fail)

### `Country`

- str input (Pass)
- Non-str input (Fail)

### `Link`

- str input (Pass)
- Non-str input (Fail)

## Combinatorial Testing

- Valid inputs

| Parameter     | Input Type |
|---------------|------------|
| street Number | str        |
| street Name   | str        |
| suburb        | str        |
| state         | str        |
| postcode      | str        |
| country       | str        |

Expected result: Pass

- Invalid input type for `street Number`

| Parameter     | Input Type |
|---------------|------------|
| street Number | int        |
| street Name   | str        |
| suburb        | str        |
| state         | str        |
| postcode      | str        |
| country       | str        |

Expected result: Fail

- Invalid input type for `street Name`

| Parameter     | Input Type |
|---------------|------------|
| street Number | str        |
| street Name   | float      |
| suburb        | str        |
| state         | str        |
| postcode      | str        |
| country       | str        |

Expected result: Fail

- Invalid input type for `suburb`

| Parameter     | Input Type |
|---------------|------------|
| street Number | str        |
| street Name   | str        |
| suburb        | set        |
| state         | str        |
| postcode      | str        |
| country       | str        |

Expected result: Fail

- Invalid input type for `state`

| Parameter     | Input Type |
|---------------|------------|
| street Number | str        |
| street Name   | str        |
| suburb        | str        |
| state         | list       |
| postcode      | str        |
| country       | str        |

Expected result: Fail

- Invalid input type for `postcode`

| Parameter     | Input Type |
|---------------|------------|
| street Number | str        |
| street Name   | str        |
| suburb        | str        |
| state         | str        |
| postcode      | None       |
| country       | str        |

Expected result: Fail

- Invalid input type for Country

| Parameter     | Input Type |
|---------------|------------|
| street Number | str        |
| street Name   | str        |
| suburb        | str        |
| state         | str        |
| postcode      | str        |
| country       | list       |

Expected result: Fail

- Invalid input type for `link`

| Parameter | Input Type |
|-----------|------------|
| link      | int        |

Expected result: Fail

## Testing `get_street_number()`
- Returns street number of the meeting as a str

## Testing `get_street_name()`
- Returns the street name as a str

## Testing `get_suburb()`
- Returns the suburb name as a str

## Testing `get_state()`
- Returns the state name as a str

## Testing `get_postcode()`
- Returns the postcode as a str

## Testing `get_country()`
- Returns the country name as a str

## Testing `get_link()`
- Returns the link for meetings as a str

## Testing `set_street_number()`
### Equivalent classes
- `street number` --- str input(Pass)
- `street number` --- non-str input(Fail)

## Testing `set_street_name()`
### Equivalent classes
- `street name` --- str input(Pass)
- `street name` --- non-str input(Fail)

## Testing `set_suburb()`
### Equivalent classes
- `suburb` --- str input(Pass)
- `suburb` --- non-str input(Fail)

## Testing `set_state()`
### Equivalent classes
- `state` --- str input(Pass)
- `state` --- non-str input(Fail)

## Testing `set_postcode()`
### Equivalent classes
- `postcode` --- str input(Pass)
- `postcode` --- non-str input(Fail)

## Testing `set_country()`
### Equivalent classes
- `country` --- str input(Pass)
- `country` --- non-str input(Fail)

## Testing `set_link()`
### Equivalent classes
- `link` --- str input(Pass)
- `link` --- non-str input(Fail)

## Testing `get_object()`
### Equivalent classes
- Correct object is given for the test Location with addresses
- Correct object is given for the test Location with link

## Testing `__str__()`
### Equivalent classes
- Correct location is returned for Locations with addresses
- Correct link is returned for Locations with links


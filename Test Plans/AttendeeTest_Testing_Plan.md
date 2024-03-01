# Testing `__init__()`
## Testing strategy
The tests aim to maximise branch and path coverage by entering each if statement.
Since most of the branches involved are precondition checks, most of them will result in failure.
As a result, the test cases were chosen in such a way to guarantee the entering of each precondition branch.
This was done by using combinatorial testing, and to only change one variable from a passing test to a failure. This would demonstrate the change of the specific variable would be solely responsible for causing a failure.

## Equivalence Classes
`email`:
- str input (Pass)
- Non-str input (Fail)

`organiser`:
- bool input (Pass)
- Non-bool input (Fail)
- No input (Pass)

`is_self`:
- bool input (Pass)
- Non-bool input (Fail)
- No input (Pass)

## Test Cases
- Valid inputs
    - email str input
    - organiser bool
    - is_self bool
    - (Pass)
- Valid `email`, invalid `organiser`
    - email str input
    - organiser Non-bool input
    - is_self No input
    - (Fail)
- Valid `email`, invalid `is_self`
    - email str input
    - organiser No input
    - is_self Non-bool input
    - (Fail)
- Invalid `email`
    - email str Non-str input
    - organiser bool
    - is_self bool
    - (Fail)
- Invalid `email`, invalid `organiser`
    - email str Non-str input
    - organiser Non-bool input
    - is_self No input
    - (Fail)
- Invalid `email`, invalid `is_self`
    - email str Non-str input
    - organiser No input
    - is_self Non-bool input (Fail)


# Testing `get_email()`
## Testing Strategy
Since this method is merely an accessor method, we only need to check that it returns the correct value.

## Test Cases
- Returns email of the test Attendee as a str


# Testing `get_organiser()`
## Testing Strategy
Since this method is merely an accessor method, we only need to check that it returns the correct value.

## Test Cases
- Returns the organiser status of the test Attendee as a bool


# Testing `get_is_self()`
## Testing Strategy
Since this method is merely an accessor method, we only need to check that it returns the correct value.

## Test Cases
- Returns the is_self status of the test Attendee as a bool


# Testing `get_response_status()`
## Testing Strategy
Since this method is merely an accessor method, we only need to check that it returns the correct value.

## Test Cases
- Returns the reponse_status of the test Attendee as a str


# Testing `set_email()`
## Testing Strategy
Since this method is a mutator method, we just need to check the error raising upon entering an invalid type, and that the attribute's value is correctly set.

## Equivalence Classes/Test Cases
- email str input, correct email is set (Pass)
- email Non-str input (Fail)


# Testing `set_organiser()`
## Testing Strategy
Since this method is a mutator method, we just need to check the error raising upon entering an invalid type, and that the attribute's value is correctly set.

## Equivalence Classes/Test Cases
- organiser bool input, correct status is set (Pass)
- organiser Non-str input (Fail)


# Testing `set_response_status()`
## Testing Strategy
Since this method is a mutator method, we just need to check the error raising upon entering an invalid type, and that the attribute's value is correctly set.

## Equivalence Classes/Test Cases
- Valid response status is given, correct status is set (Pass)
- Invalid response status is given, error is thrown (Fail)
- Non-str input is given, error is thrown (Fail)


# Testing `accept_invitation()`
## Testing Strategy
We only need to check that response_status has been succesfully updated.

## Test Cases
- Test Attendee response_status set to "accepted"


# Testing `decline_invitiation()`
## Testing Strategy
We only need to check that response_status has been succesfully updated.

## Test Cases
- Test Attendee response_status set to "declined"


# Testing `get_object()`
## Testing Strategy
Since this method serves a similar purpose to that of accessor methods, we only need to check that the correct object is returned.

## Test Cases
- Correct object is given for the test Attendee


# Testing `__str__()`
## Testing Strategy
Since this method serves a similar purpose to that of accessor methods, we only need to check that the correct string is returned.

## Test Cases
- Correct email is returned
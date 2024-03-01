# Testing __init__()
## Testing strategy
The tests aim to maximise branch and path coverage by entering each if statement.
Since most of the branches involved are precondition checks, most of them will result in failure.
As a result, the test cases were chosen in such a way to guarantee the entering of each precondition branch.
This was done by using combinatorial testing, and to only change one variable from a passing test to a failure. This would demonstrate the change of the specific variable would be solely responsible for causing a failure.

## Equivalence Classes
**Starting_time**:
- Time input (Pass)
- None input (Pass)
- Other type input (Fail)

**Ending_time**:
- Time input (Pass)
- None input (Pass)
- Other type input (Fail)

**Attendees**:
- list input (Pass)
- None input (Pass)
- Other type input (Fail)

**Summary**:
- str input (Pass)
- None input (Pass)
- Other type input (Fail)

**Description**:
- str input (Pass)
- None input (Pass)
- Other type input (Fail)

**Location**:
- Location input (Pass)
- None input (Pass)
- Other type input (Fail)

**Reminders**:
- list input (Pass)
- None input (Pass)
- Other type input (Fail)

**Event_id**:
- str input (Pass)
- No input (Pass)
- None input (Fail)
- Other type input (Fail)

## Test Cases (aiming to maximise branch and path coverage)
- Valid inputs
    - starting_time Time input
    - ending_time Time input
    - attendees list input
    - summary str input
    - description str input
    - location Location input
    - reminders list input
    - event_id str input
    - (Pass)
- Invalid ending_time type
    - starting_time Time input
    - ending_time other type input
    - attendees None input
    - summary None input
    - description None input
    - location None input
    - reminders None input
    - event_id no input
    - (Fail)
- Invalid attendees type
    - starting_time Time input
    - ending_time None input
    - attendees other type input
    - summary str input
    - description str input
    - location Location input
    - reminders list input
    - event_id str input
    - (Fail)
- Invalid summary type
    - starting_time Time input
    - ending_time Time input
    - attendees list input
    - summary other type input
    - description str input
    - location Location input
    - reminders list input
    - event_id str input
    - (Fail)
- Invalid description type
    - starting_time Time input
    - ending time None input
    - attendees None input
    - summary None input
    - description other type input
    - location None input
    - reminders None input
    - event_id no input
    - (Fail)
- Invalid location type
    - starting_time None input
    - ending time None input
    - attendees None input
    - summary None input
    - description None input
    - location other type input
    - reminders None input
    - event_id no input
    - (Fail)
- Invalid reminders type
    - starting_time None input
    - ending time None input
    - attendees None input
    - summary None input
    - description None input
    - location None input
    - reminders other type input
    - event_id no input
    - (Fail)
- event_id None input
    - starting_time None input
    - ending_time Time input
    - attendees list input
    - summary str input
    - description str input
    - location Location input
    - reminders list input
    - event_id None input
    - (Fail)
- Invalid event_id type
    - starting_time None input
    - ending_time Time input
    - attendees list input
    - summary str input
    - description str input
    - location Location input
    - reminders list input
    - event_id other type input
    - (Fail)
- Invalid starting_time type
    - starting_time other type input
    - ending_time Time input
    - attendees list input
    - summary str input
    - description str input
    - location Location input
    - reminders list input,
    - event_id str input
    - (Fail)
- Valid None types
    - starting_time None input
    - ending_time None input
    - attendees None input
    - summary None input
    - description None input
    - location None input
    - reminders None input
    - event_id no input
    - (Pass)


# Testing get_event_id
## Testing Strategy
Since this method is merely an accessor method, we only need to check that it returns the correct value.

## Test Cases
- Returns event_id of the test Event as a str or None if event_id is not properly initialised


# Testing get_starting_time
## Testing Strategy
Since this method is merely an accessor method, we only need to check that it returns the correct value.

## Test Cases
- Returns starting_time of the test Event as a Time


# Testing get_ending_time
## Testing Strategy
Since this method is merely an accessor method, we only need to check that it returns the correct value.

## Test Cases
- Returns ending_time of the test Event as a Time


# Testing get_organiser
## Testing Strategy
Since this method is merely an accessor method, we only need to check that it returns the correct value.

## Test Cases
- Returns organiser of the test Event as an Orgainser


# Testing get_attendees
## Testing Strategy
Since this method is merely an accessor method, we only need to check that it returns the correct value.

## Test Cases
- Returns attendees of the test Event as a list


# Testing get_summary
## Testing Strategy
Since this method is merely an accessor method, we only need to check that it returns the correct value.

## Test Cases
- Returns summary of the test Event as a str


# Testing get_description
## Testing Strategy
Since this method is merely an accessor method, we only need to check that it returns the correct value.

## Test Cases
- Returns description of the test Event as a str


# Testing get_location
## Testing Strategy
Since this method is merely an accessor method, we only need to check that it returns the correct value.

## Test Cases
- Returns location of the test Event as a Location


# Testing get_reminders
## Testing Strategy
Since this method is merely an accessor method, we only need to check that it returns the correct value.

## Test Cases
- Returns reminders of the test Event as a list


# Testing initialise_event_id
## Testing Strategy
Since this method is similar to that of a mutator method (except that it can only be run once), we need to check the error raising upon entering an invalid type, when the event_id has already been initialised, and that the attribute's value is correctly set.

## Equivalence Classes
- event_id is not properly initialised and str is given (Pass)
- event_id has already been initialised and str is given (Fail)
- Non-str type is given (Fail)


# Testing set_starting_time()
## Testing Strategy
Since this method is a mutator method, we just need to check the error raising upon entering an invalid type, and that the attribute's value is correctly set.

## Equivalence Classes/Test Cases
- starting_time Time input, starting_time is before ending_time, correct time is set (Pass)
- starting_time Time input, starting_time is after ending_time, error is thrown (Fail)
- starting_time None input (Pass)
- starting_time non-Time input, error is thrown (Fail)


# Testing set_ending_time()
## Testing Strategy
Since this method is a mutator method, we just need to check the error raising upon entering an invalid type, and that the attribute's value is correctly set.

## Equivalence Classes/Test Cases
- ending_time Time input, ending_time is after starting_time, correct time is set (Pass)
- ending_time Time input, ending_time is before starting_time, error is thrown (Fail)
- ending_time None input (Pass)
- ending_time non-Time input, error is thrown (Fail)


# Testing set_organiser()
## Testing Strategy
Since this method is a mutator method, we just need to check the error raising upon entering an invalid type, and that the attribute's value is correctly set.

## Equivalence Classes/Test Cases
- organiser Organiser input, correct organiser is set (Pass)
- organiser None input (Pass)
- organiser non-Organiser input, error is thrown (Fail)


# Testing set_attendees()
## Testing Strategy
Since this method is a mutator method, we just need to check the error raising upon entering an invalid type, and that the attribute's value is correctly set.

## Equivalence Classes/Test Cases
- attendees list input, len(attendees) <= 20, correct attendees is set (Pass)
- attendees list input, len(attendees) > 20, error is thrown (Fail)
- attendees None input (Pass)
- attendees non-list input, error is thrown (Fail)


# Testing set_summary()
## Testing Strategy
Since this method is a mutator method, we just need to check the error raising upon entering an invalid type, and that the attribute's value is correctly set.

## Equivalence Classes/Test Cases
- summary str input, correct summary is set (Pass)
- summary None input (Pass)
- summary non-str input, error is thrown (Fail)


# Testing set_description()
## Testing Strategy
Since this method is a mutator method, we just need to check the error raising upon entering an invalid type, and that the attribute's value is correctly set.

## Equivalence Classes/Test Cases
- description str input, correct description is set (Pass)
- description None input (Pass)
- description non-str input, error is thrown (Fail)


# Testing set_location()
## Testing Strategy
Since this method is a mutator method, we just need to check the error raising upon entering an invalid type, and that the attribute's value is correctly set.

## Equivalence Classes/Test Cases
- location Location input, correct location is set (Pass)
- location None input (Pass)
- location non-Location input, error is thrown (Fail)


# Testing set_reminders()
## Testing Strategy
Since this method is a mutator method, we just need to check the error raising upon entering an invalid type, and that the attribute's value is correctly set.

## Equivalence Classes/Test Cases
- reminders list input, correct reminders is set (Pass)
- reminders None input (Pass)
- reminders non-list input, error is thrown (Fail)


# Testing add_attendee()
## Testing Strategy
For this method, we need check that the correct type of given for the attendee, whether or not adding the attendee will overflow the 20 attendee limit, and that the attendees list has been correctly updated.

## Equivalence Classes/Test Cases
- attendee Attendee input, correct attendees list is set (Pass)
- attendee non-Attendee input, error is thrown (Fail)
- len(attendees) is 20, error is thrown (Fail)


# Testing remove_attendee()
## Testing Strategy
For this method, since the input is an index of the attendees list, we need to check that index is an integer, if it is in range of the attendees list, and that the attendees list has been correctly updated.

## Equivalence Classes/Test Cases
- index int input, index is in range, correct attendees list is set (Pass)
- index int input, index is out of range, error is thrown (Fail)
- index non-int input, error is thrown (Fail)


# Testing attendee_accept()
## Testing Strategy
For this method, since the input is an index of the attendees list, we need to check that index is an integer, if it is in range of the attendees list, and that the attendees list has been correctly updated.

## Equivalence Classes/Test Cases
- index int input, index is in range, correct attendee response status is set (Pass)
- index int input, index is out of range, error is thrown (Fail)
- index non-int input, error is thrown (Fail)


# Testing attendee_decline()
## Testing Strategy
For this method, since the input is an index of the attendees list, we need to check that index is an integer, if it is in range of the attendees list, and that the attendees list has been correctly updated.

## Equivalence Classes/Test Cases
- index int input, index is in range, correct attendee response status is set (Pass)
- index int input, index is out of range, error is thrown (Fail)
- index non-int input, error is thrown (Fail)


# Testing add_reminder()
## Testing Strategy
For this method, we simply need to check the type of the reminder, and that the reminders list has been correctly upated.

## Equivalence Classes/Test Cases
- reminder Reminder input, correct reminder list is set (Pass)
- reminder non-Reminder input, error is thrown (Fail)


# Testing remove_reminder()
## Testing Strategy
For this method, since the input is an index of the reminders list, we need to check that index is an integer, if it is in range of the reminders list, and that the reminders list has been correctly updated.

## Equivalence Classes/Test Cases
- index int input, index is in range, correct reminders list is set (Pass)
- index int input, index is out of range, error is thrown (Fail)
- index non-int input, error is thrown (Fail)


# Testing cancel_event()
## Testing Strategy
We only need to check that cancelled has been succesfully updated.

## Test Cases
- cancelled is set to True


# Testing uncancel_event()
## Testing Strategy
We only need to check that cancelled has been succesfully updated.

## Test Cases
- cancelled is set to False


# Testing transfer_ownership()
## Testing Strategy
For this method, MC/DC was used to for the coverage of the first if (and its embedded if) statement. There are two conditions here:
- self.attendees[i].get_organiser() == True
- self.attendees[i].get_email() != organiser.get_email()
Since there are no combination of conditions where the first condition is false such that we get a overall true result, we only need to consider the second condition.
This results in two test cases such that the first condition is true and the second condition is either true or false.

For the second if statement, we only need consider when the condition is true and false.

## Test Cases
- organiser type Organiser, organiser in attendee list (self.attendees[i].get_organiser() == True), the organiser in the attendee is not the organiser (self.attendees[i].get_email() != organiser.get_email()) (Pass)
- organiser type Organiser, organiser in attendee list (self.attendees[i].get_organiser() == True), the organiser in the attendee is the organiser (self.attendees[i].get_email() == organiser.get_email()) (Pass)
- (organiser type Organiser, organiser not in attendee list, but the new organiser is in the attendee list, the attendee is given organiser status (Pass)) (Note: this test case is tested in combination with the first test case)
- organiser type Organiser, organiser not in attendee list, and the new organiser is not in the attendee list (Pass)
- organiser non-Organiser input, error is thrown (Fail)


# Testing get_body()
## Testing Strategy
Since this method serves a similar purpose to that of accessor methods, we only need to check that the correct object is returned.

## Test Cases
- Correct event body is returned for the test Event
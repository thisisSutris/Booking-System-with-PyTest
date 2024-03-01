# Testing get_events()
## Testing Strategy
This function acts similar to that of an accessor where it merely returns a list of events stored in the api. As a result, we only need to check if the return value is correct or not.

## Test Cases
- Test that the function returns the correct set of events from the api


# Testing create_location_address()
## Testing Strategy
The tests aim to maximise branch and path coverage by entering each if statement.
Since most of the branches involved are precondition checks, most of them will result in failure.
As a result, the test cases were chosen in such a way to guarantee the entering of each precondition branch.
This was done by using combinatorial testing, and to only change one variable from a passing test to a failure. This would demonstrate the change of the specific variable would be solely responsible for causing a failure.

## Equivalence Classes
**street_number**
- str input (Pass)
- Non-str input, error is thrown (Fail)

**street_name**
- str input (Pass)
- Non-str input, error is thrown (Fail)

**suburb**
- str input (Pass)
- Non-str input, error is thrown (Fail)

**state**
- str input (Pass)
- Non-str input, error is thrown (Fail)

**postcode**
- str input (Pass)
- Non-str input, error is thrown (Fail)

**country**
- str input (Pass)
- Non-str input, error is thrown (Fail)

## Test Cases
- Pass test cases
    - street_number str input
    - street_name str input
    - suburb str input
    - state str input
    - postcode str input
    - country str input
    - (Pass)
- Invalid street_number type
    - street_number non-str input
    - street_name str input
    - suburb str input
    - state str input
    - postcode str input
    - country str input
    - (Fail)
- Invalid street_name type
    - street_number str input
    - street_name non-str input
    - suburb str input
    - state str input
    - postcode str input
    - country str input
    - (Fail)
- Invalid suburb type
    - street_number str input
    - street_name str input
    - suburb non-str input
    - state str input
    - postcode str input
    - country str inpu
    - (Fail)
- Invalid state type
    - street_number str input
    - street_name str input
    - suburb str input
    - state non-str input
    - postcode str input
    - country str 
    - (Fail)
- Invalid postcode type
    - street_number str input
    - street_name str input
    - suburb str input
    - state str input
    - postcode non-str input
    - country str input
    - (Fail)
- Invalid country type
    - street_number str input
    - street_name str input
    - suburb str input
    - state str input
    - postcode str input
    - country non-str input
    - (Fail)


# Testing create_event_link()
## Testing Strategy
This function only accepts one argument and performs no logic on its own. As a result, we only need to check if the argument provided is of the correct type or not.

## Equivalence Classes/Test Cases
**link**
- str input (Pass)
- Non-str input (Fail)


# Testing create_event()
## Testing Strategy
The tests aim to maximise branch and path coverage by entering each if statement.
Since most of the branches involved are precondition checks, most of them will result in failure.
As a result, the test cases were chosen in such a way to guarantee the entering of each precondition branch.
This was done by using combinatorial testing, and to only change one variable from a passing test to a failure. This would demonstrate the change of the specific variable (usually variable type) would be solely responsible for causing a failure.

Additionally, since little logic is done in the function itself, no path/condition/decision coverage is required.

Since the function interfaces directly with the api, mocking is used to mock the api and test the functionality.

## Equivalence Classes
**events**
- list input (Pass)
- Non-list input (Fail)

**starting_time**
- Time input, before ending_time, after current time, before 2050 (Pass)
- Time input, after ending_time, after current time, before 2050 (Fail)
- Time input, before ending_time, before current time, before 2050 (Fail)
- Time input, before ending_time, after current time, after 2050 (Fail)
- Non-Time input (Fail)

**ending_time**
- Time input, after starting_time (Pass)
- Time input, before starting_time (Fail)
- Non-Time input (Fail)

**attendees**
- list input (Pass)
- Non-list input (Fail)

**summary**
- str input (Pass)
- Non-str input (Fail)

**description**
- str input (Pass)
- Non-str input (Fail)

**location**
- Location input (Pass)
- Non-Location input (Fail)

**reminders**
- list input (Pass)
- Non-list input (Fail)

## Test Cases
- Invalid events type
    - events non-list input
    - starting_time Time input, before ending_time, after current time, before 2050
    - ending_time Time input, after starting_time
    - attendees list input
    - summary str input
    - description str input
    - location Location input
    - reminders list input
    - (Fail)
- Invalid starting_time: after ending_time
    - events list input
    - starting_time Time input, after ending_time, after current time, before 2050
    - ending_time Time input, after starting_time
    - attendees list input
    - summary str input
    - description str input
    - location Location input
    - reminders list input
    - (Fail)
- Invalid starting_time: before current time
    - events list input
    - starting_time Time input, before ending_time, before current time, before 2050
    - ending_time Time input, after starting_time
    - attendees list input
    - summary str input
    - description str input
    - location Location input
    - reminders list input
    - (Fail)
- Invalid starting_time: after 2050
    - events list input
    - starting_time Time input, before ending_time, after current time, after 2050
    - ending_time Time input, after starting_time
    - attendees list input
    - summary str input
    - description str input
    - location Location input
    - reminders list input
    - (Fail)
- Invalid starting_time type
    - events list input
    - starting_time non-Time input
    - ending_time Time input, after_starting_time
    - attendees list input
    - summary str input
    - description str input
    - location Location input
    - reminders list input
    - (Fail)
- Invalid ending_time: before starting_time
    - events list input
    - starting_time Time input, before ending_time, after current time, before 2050
    - ending_time Time input, before starting_time
    - attendees list input
    - summary str input
    - description str input
    - location Location input
    - reminders list input 
    - (Fail)
- Invalid ending_time type
    - events list input
    - starting_time Time input, before ending_time, after current time, before 2050
    - ending_time non-Time input
    - attendees list input
    - summary str input
    - description str input
    - location Location input
    - reminders list input
    - (Fail)
- Invalid attendees type
    - events list input
    - starting_time Time input, before ending_time, after current time, before 2050
    - ending_time Time input, after starting_time
    - attendees non-list input
    - summary str input
    - description str input
    - location Location input
    - reminders list input
    - (Fail)
- Invalid summary type
    - events list input
    - starting_time Time input, before ending_time, after current time, before 2050
    - ending_time Time input, after starting_time
    - attendees list input; summary non-str input
    - description str input; location Location input
    - reminders list input
    - (Fail)
- Invalid description type
    - events list input
    - starting_time Time input, before ending_time, after current time, before 2050
    - ending_time Time input, after starting_time
    - attendees list input
    - summary str input
    - description non-str input
    - location Location input
    - reminders list input
    - (Fail)
- Invalid location type
    - events list input
    - starting_time Time input, before ending_time, after current time, before 2050
    - ending_time Time input, after starting_time
    - attendees list input
    - summary str input
    - description str input
    - location non-Location input
    - reminders list input
    - (Fail)
- Invalid reminders type
    - events list input
    - starting_time Time input, before ending_time, after current time, before 2050
    - ending_time Time input, after starting_time
    - attendees list input
    - summary str input
    - description str input
    - location Location input
    - reminders non-list input
    - (Fail)
- Valid inputs
    - events list input
    - starting_time Time input, before ending_time, after current time, before 2050
    - ending_time Time input, after starting_time; attendees list input
    - summary str input
    - description str input
    - location Location input
    - reminders list input
    - (Pass)
    - (Note: this specific test case(s) is tested under "Functionality" heading, which tests the actual functionality)

## Functionality
- Event is created, correct event event body in server, correct initialisation of event_id and organiser, correct Event return


# Testing delete_event()
## Testing Strategy
For this function, the test cases aim to maximise branch and path coverage by entering each precondition if statement. The tests were chosen in a way to guarantee that each if statement would be entered.
This was done by changing variables such that a passing test would change into a failure, thus testing to see if the change of that variable only was enough to cause the failure.

Additionally, since little logic is done in the function itself, no path/condition/decision coverage is required.

Since the function interfaces directly with the api, mocking is used to mock the api and test the functionality.

## Equivalence Classes
**events**
- list input (Pass)
- Non-list input, error is thrown (Fail)

**event_id**
- str input (Pass)
- Non-str input, error is thrown (Fail)

**Functionality**
- Event in the past is deleted, event is deleted from the server and from the events list
- Event in the present/future is deleted, event is deleted from the server and marked as cancelled in the events list

## Test Cases
- events non-list input, event_id str input (Fail)
- events list input, event_id non_str input (Fail)
- events list input, event_id str input (Pass) (Note: this specific test case(s) is tested under "Functionality" heading, which tests the actual functionality)


# Testing update_event()
## Testing Strategy
Similar to the create_event() and delete_event(), the test cases aim to maximise branch and path coverage by entering each precondition if statement. The tests were chosen in a way to guarantee that each if statement would be entered.
This was done by changing variables such that a passing test would change into a failure, thus testing to see if the change of that variable only was enough to cause the failure.

Additionally, since little logic is done in the function itself, no path/condition/decision coverage is required.

Since the function interfaces directly with the api, mocking is used to mock the api and test the functionality.

## Equivalence Classes
**events**
- list input (Pass)
- Non-list input (Fail)

**event_id**
- str input, valid event_id (Pass)
- str input, invalid event_id (Fail)
- Non-str input (Fail)

**event**
- Event input (Pass)
- Non-Event input (Fail)

## Test Cases
- Invalid events type
    - events non-list input
    - event_id str input, valid event_id
    - event Event input
    - (Fail)
- Invalid event_id
    - events list input
    - event_id str input, invalid event_id
    - event Event input
    - (Fail)
- Invalid event_id type
    - events list input
    - event_id non-str input
    - event Event
    - (Fail)
- Invalid event type
    - events list input
    - event_id str input, valid event_id
    - event non-Event input
    - (Fail)
- Valid input
    - events list input
    - event_id str input, valid event_id
    - event Event input
    - (Pass)
    - (Note: this specific test case(s) is tested under "Functionality" heading, which tests the actual functionality)

## Functionality
- Event is correctly updated


# Testing get_events_date()
## Testing Strategy
Since this function contains many precondition checks, checking both value and type, tests were conducted by setting one variable to a value/type that would cause a failure from a passing test. This aims to maximise branch/path coverage by entering each precondition statement.

Additionally, since the function contains a bit of logic, test cases were written to test how the function interacted with various combinations of inputs (usually to see if they were int or None). However, due to the high number of conditions (especially when year, month and day are provided), MC/DC was not performed.

## Equivalence Classes
**events**
- list input (Pass)
- Non-list input (Fail)

**year**
- int input (Pass)
- Non-int input (Fail)

**month**
- int input, month in [1, 12] (Pass)
- int input, month < 1 (Fail)
- int input, month > 12 (Fail)
- None/no input (Pass)
- Other type input (Fail)

**day**
- int input, day in [1, 31] (Pass)
- int input, day < 1 (Fail)
- int input, day > 31 (Fail)
- None/no input (Pass)
- Other type input (Fail)

## Test Cases
The test cases here aim to test each condition that could potentially lead to failure.
The test cases maximises branch coverage by entering each if statement (100% not possible due to lack of else statements).
**Note:** due to the absurd number of conditions, MC/DC was not done here
**Note:** all passing tests will need to have their functionalities tested
- Valid inputs
    - events list input
    - year int input
    - month int input, month in [1, 12]
    - day int input, day in [1, 31]
    - (Pass)
    - (Note: this specific test case(s) is tested under "Functionality" heading, which tests the actual functionality)
- Invalid events type
    - events non-list input
    - year int input
    - month int input, month in [1, 12]
    - day int input, day in [1, 31]
    - (Fail)
- Invalid year type
    - events list input
    - year non-int input
    - month int input, month in [1, 12]
    - day int input, day in [1, 31]
    - (Fail)
- month < 1
    - events list input
    - year int input
    - month int input, month < 1
    - day int input, day in [1, 31]
    - (Fail)
- month > 12
    - events list input
    - year int input
    - month int input, month > 12
    - day int input, day in [1, 31]
    - (Fail)
- month is None/no input, day is None/no input
    - events list input
    - year int input
    - month None input
    - day None input
    - (Pass)
    - (Note: this specific test case(s) is tested under "Functionality" heading, which tests the actual functionality)
- month is None/no input, day is not None/no input
    - events list input
    - year int input
    - month None/no input
    - day int input, day in [1, 31]
    - (Fail)
- Invalid month type
    - events list input
    - year int input
    - month other type input
    - day int input, day in [1, 31]
    - (Fail)
- day < 1
    - events list input
    - year int input
    - month int input, month in [1, 12]
    - day int input, day < 1
    - (Fail)
- day > 31
    - events list input
    - year int input
    - month int input, month in [1, 12]
    - day int input, day > 31
    - (Fail)
- month is not None/no input, day is None/no input
    - events list input
    - year int input
    - month int input, month in [1, 12]
    - day None/no input
    - (Pass)
    - (Note: this specific test case(s) is tested under "Functionality" heading, which tests the actual functionality)
- Invalid day type
    - events list input
    - year int input
    - month int input, month in [1, 12]
    - day other type input
    - (Fail)

# Functionality
- Year input, no month input, no day input: all events in the year are returned
- Year input, month input, no day input: all events in the month in the year are returned
- Year input, month input, day input: all events in the day in the month in the year are returned


# Testing get_time_now()
## Testing Strategy
This function takes no input and contains no logic by itself. The logic is mostly contained in time_to_Time(), for which its logic is lightly tested (most of its testing will be done for time_to_Time()).

The function does however depend on the current time of day. As a result, the tests use patch the datetime class (which is used to get the  current) and mocks the return value to test the functionality of the function.

## Equivalence Classes
- Current time is [0:00, 14:00) UTC, time +10:00 is returned.
- Current is [14:00, 24:00) UTC, correct time is returned (wrap around time for the next day).

## Boundary Conditions
- Current time is 13:59 UTC (23:59 Melbourne time) (off-point boundary condition)
- Current time is 14:00 UTC (00:00 next day Melbourne time) (on-point boundary condition)


# Testing time_to_Time()
## Testing Strategy
The tests for this function tests the input type as well as the logic which sets the current time in Australia/Melbourne time.

The type testing is done to see if the precondition successfully raises an exception when in invalid type is entered.

The logic was tested using path coverage.
- str input, where +10:00 will be the next day (Pass) aims to cover the path dictated by the line numbers: 288, 289, 291, 292, 309, 310.
- str input, where +10:00 will be the next month (Pass) aims to cover the path dictated by the line numbers: 288, 289, 291, 292, 294, 296, 297, 305, 306, 307.
- str input, where +10:00 will be the next year (Pass) aims to cover the path dictated by the line numbers: 288, 289, 291, 292, 294, 296, 297, 299, 300, 301, 302, 303.

## Test Cases
- str input, where +10:00 will not change the day/month/year (Pass)
- str input, where +10:00 will be the next day (Pass)
- str input, where +10:00 will be the next month (Pass)
- str input, where +10:00 will be the next year (Pass)
- Non-str input (Fail)


# Testing attendee_to_Attendee()
## Testing Strategy
For the input, the type is checked to see if an exception is raised when an invalid type is entered. The input dictionary is then checked to see if the 'email' key is present and raise an exception if otherwise. Both these conditions are checked with dict input, email absent (Fail) and Non-dict input (Fail).

The logic of the function is tested with the aim of maximising path coverage.
- dict input, 'email' present, 'organizer' present, 'organizer': True, 'self' present, 'self': True, 'responseStatus' present (Pass) aims to cover the path dictated by the line numbers: 329, 330, 331, 332, 333, 334, 335, 336, 337
- dict input, 'email' present, 'organizer' present, 'organizer': True, 'self' present, 'self': True, 'responseStatus' absent (Pass) aims to cover the path dictated by the line numbers: 329, 330, 331, 332, 333, 334, 335, 336, 338, 339
- dict input, 'email' present, 'organizer' present, 'organizer': False, 'self' present, 'self': False, 'responseStatus' present (Pass) aims to cover the path dictated by the line numbers: 329, 330, 332, 333, 335, 336, 337, which follows the path such that if attendee['organizer'] and if attendee['self'] are both false.
- dict input, 'email' present, 'organizer' absent, 'self' absent, 'responseStatus' present (Pass) aims to cover the path dictated by the line numbers: 329, 332, 335, 336, 337, which follows the path such that if 'organizer' in attendee.keys() and if 'self' in attendee.keys() are both false.

## Equivalence Classes
- dict input, 'email' absent (Fail)
- Non-dict input (Fail)
- dict input, 'email' present, 'organizer' present, 'organizer': True, 'self' present, 'self': True, 'responseStatus' present (Pass)
- dict input, 'email' present, 'organizer' present, 'organizer': True, 'self' present, 'self': True, 'responseStatus' absent (Pass)
- dict input, 'email' present, 'organizer' present, 'organizer': False, 'self' present, 'self': False, 'responseStatus' present (Pass)
- dict input, 'email' present, 'organizer' absent, 'self' absent, 'responseStatus' present (Pass)


# Testing organiser_to_Organiser()
## Testing Strategy
Since Attendees and Organisers are very similar, their testing strategies are very similar as well.

For path coverage,
- dict input, email present, 'self' present, 'self': True (Pass) covers the path: 352, 353, 354, 355.
- dict input, email present, 'self' present, 'self': False (Pass) covers the path: 352, 353, 354, where the 'self' key is false.
- dict input, email present, 'self' absent (Pass) covers the path: 352, 353, where the 'self' key is absent.

## Test Cases
- dict input, email absent (Fail)
- Non-dict input (Fail)
- dict input, email present, 'self' present, 'self': True (Pass)
- dict input, email present, 'self' present, 'self': False (Pass)
- dict input, email present, 'self' absent (Pass)


# Testing location_to_Location()
## Testing Strategy
Since this function only takes in one input and performs very little branching logic, only the input needs to be tested. As a result the tests are dedicated to testing if the proper exceptions are raised when an invalid type is entered, and to check that the function does indeed return the correct Location object.

## Equivalence Classes/Test Cases
- str input (Pass)
- Non-str input (Fail)


# Testing reminder_to_Reminder()
## Testing Strategy
For this function, most of the logic applied are preconditions and will thus lead the raising of exceptions if triggered. As a result, path coverage is not required here. The test cases here aim to test each precondition by setting a single variable to an invalid input that would result in a failure from a passing test.

## Equivalence Classes
- dict input, valid (Pass)
- dict input, missing method (Fail)
- dict input, missing minutes (Fail)
- Non-dict input (Fail)

## Test cases
These test cases aim to maximise branch coverage by entering each if statement.
- dict input, method present, minutes present (Pass)
- dict input, method missing, minutes present (Fail)
- dict input, method present, minutes missing (Fail)
- Non-dict input (Fail)


# Testing event_to_Event()
## Testing Strategy
The tests for this function aims to test the preconditions of the function, as well as to maximise path coverage.

Since the checking of each key is independent of each other, we can maximise path coverage by testing inputs such that all if statements return true, and another test testing inputs such that all if statements return false.

An additional pair of tests is included to test paths of the the embedded if statement in the 'reminders' check.

## Equivalence Classes/Test Cases
- dict input, all entries present (Pass)
- dict input, no entries present (except event_id) (Pass)
- dict input, no entries present, except for reminders ('overrides': True) (and event_id) (Pass)
- dict input, no entries present, except for reminders ('overrides': False) (and event_id) (Pass)
- dict input, missing event_id (Fail)
- Non-dict input (Fail)


# Testing check_self_organiser()
## Testing Strategy
The only logic present in the function is checking the input type as well if the event has an organiser or not. As a result, only these two conditions need to be checked, as well as a test checking that neither condition is entered.

## Equivalence Classes
- Event input, event has organiser (Pass) (Tested in 'Functionality')
- Event input, event has no organiser (somehow) (Pass) (Tested in 'Functionality')
- Non-Event input (Fail)

## Functionality
- Event has no organiser (somehow)
- The user is the event organiser
- The user is not the event organiser


# Testing search_phrase()
## Testing Strategy
The tests for this function, like those before, test the preconditions of the function, as well as the logic contained in the function.

The logic is tested with the aim of maximising path coverage and checking the correct outputs.

## Equivalence Classes
**events**
- list input of Events (Pass)
- list input of non-Events (Fail)
- Non-list input (Fail)

**phrase**
- str input (Pass)
- Non-str input (Fail)

## Testing Inputs
- Valid inputs
    - events list input of Events
    - phrase str input
    - (Pass)
    - (tested as part of 'Functionality')
- List of non-Events
    - events list input of non-Events
    - phrase str input
    - (Fail)
- Invalid events type
    - events non-list input
    - phrase str input
    - (Fail)
- Invalid phrase type
    - events list input of Events
    - phrase non-str input
    - (Fail)

## Functionality (for path coverage)
- events is a list of events, event has a summary, phrase is in the summary
- events is a list of events, event has a summary, phrase is not in the summary, event has a description, phrase is in the description
- events is a list of events, event has no summary, event has a description, phrase is in the description
- events is a list of events, event has no summary, event has a description, phrase is not in the description
- events is a list of events, event has no summary and no description


# Testing import_events()
## Testing Strategy
This function contains a precondition and little logic. As a result, the test cases only check the type of the filename input and the resultant output.

## Equivalence Classes/Test Cases
**filename**
- str input (Pass)
- Non-str input (Fail)


# Testing export_events()
## Testing Strategy
The logic of this function pretty much only pertains to the preconditions. As a result, the test cases target towards testing each precondition with the aim of maximising branch coverage. This is done by only one variable from a passing test to result in an exception.

## Equivalence Classes/Test Cases
**events**
- list input of Events (Pass)
- list input of non-Events (Fail)
- Non-list input (Fail)

**filename**
- str input, .json ending (Pass)
- str input, not .json ending (Fail)
- Non-str input (Fail)

## Test Cases
- Valid inputs
    - events list input of Events
    - filename str input, .json ending
    - (Pass)
- List of non-Events
    - events list input of non-Events
    - filename str input, .json ending
    - (Fail)
- Invalid events type
    - events non-list input
    - filename str input, .json ending
- Not .json ending
    - events list input of Events
    - filename str input, not .json ending
- Invalid filename type
    - events list input of Events
    - filename non-str input


# Testing transfer_organiser()
## Testing Strategy
The logic in the function pertains pretty much only to the checking of preconditions, with the main bulk of the logic performed in the event.transfer_ownership() method. As a result the test cases only aim to check the preconditiosn and changes made to the event and its attendees/organiser.

Since the function directly interfaces with the api, mocking is used to mock the api and its return value.

## Equivalence Classes
**event**
- Event input (Pass)
- Non-Event input (Fail)

**organiser**
- Organiser input (Pass)
- Non-Organiser input (Fail)

## Test Cases
- Invalid Event type
    - Non-Event input
    - Organiser input
    - (Fail)
- Invalid Organiser type
    - Event input
    - Non-Organiser input
    - (Fail)
- Valid inputs
    - Event input
    - Organiser input
    - (Pass)
    - (Note: this specific test case(s) is tested under "Functionality" heading, which tests the actual functionality)

## Functionality
- New organiser is set, old organiser has organiser status removed, new organiser attendee (if applicable) has organiser status, event is updated on the server
# Testing Strategy for `Organiser`, `Reminder`, `Time`, `Location`

These four simple classes are very similar with each other therefore we decided to put the testing 
strategy together for these four classes.

## Strategy for testing `init()` function

The tests aim to maximise branch and path coverage by entering each if statement.
Since most of the branches involved are precondition checks, most of them will result in failure.
As a result, the test cases were chosen in such a way to guarantee the entering of each precondition branch.
This was done by using combinatorial testing, and to only change one variable from a passing test to a failure. 
This would demonstrate the change of the specific variable would be solely responsible for causing a failure.

## Strategy for testing all Accessor functions

The tests are pretty straight forward for accessors method because they are simply return the value of a variable. 
We will be comparing the expected output and the actual output to ensure they are working properly.

## Strategy for testing all Mutator functions

Since all the variables in these four classes have precondition check, the tests are designed to enter for 
each precondition check which includes type checks and value checks. Putting in inputs of invalid values and invalid types 
in the parameter can help us maximise branch/path coverage.

## Strategy for testing all `get_object()` function

Since the function is trying to return the object itself in a form of dictionary/str, we will only be conducting test
for comparing the return value and the expected value to ensure they are working properly.

## Strategy for testing `__str__()` function

Same as all the `get_object()` function, `__str__()` functions are simply returning the value of the object when 
it is casted to a str. We will be conducting tests for comparing the return value and the expected value to ensure they
are working properly.
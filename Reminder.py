class Reminder():
    def __init__(self, method: str, minutes: int) -> None:
        # Preconditions
        if type(method) != str:
            raise TypeError("Reminder __init__() method expected type str")
        if type(method) == str and method != "email" and method != "popup":
            raise ValueError("Method of Reminder should be either email or popup")
        if type(minutes) != int:
            raise TypeError("Reminder __init__() minutes expected type int")
        if minutes <= 0:
            raise ValueError("Minutes before meeting should be greater than 0")

        # Initialise
        self.method = method
        self.minutes = minutes

    def get_method(self) -> str:
        return self.method

    def get_minutes(self) -> int:
        return self.minutes

    def set_method(self, method: str) -> None:
        if type(method) != str:
            raise TypeError("Reminder set_method() method expected type str")
        if method != "email" and method != "popup":
            raise ValueError("Method of Reminder should be either email or popup")
        self.method = method

    def set_minutes(self, minutes: int) -> None:
        if type(minutes) != int:
            raise TypeError("Reminder set_minutes() minutes expected type int")
        if minutes <= 0:
            raise ValueError("Reminder set_minutes() minutes expected positive int")
        self.minutes = minutes

    def get_object(self) -> dict:
        return {
            'method': self.method,
            'minutes': self.minutes
        }

    def __str__(self) -> str:
        return "Method: " + str(self.method) + ", Minutes before: " + str(self.minutes)

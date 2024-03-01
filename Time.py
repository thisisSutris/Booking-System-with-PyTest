import datetime


class Time():
    def __init__(self, year: int, month: int, day: int, hour: int, minute: int) -> None:
        # Preconditions
        if type(year) != int:
            raise TypeError("Time __init__() year expected type int")
        if year < 1950 or year > 2050:
            raise ValueError("Time __init__() year expected int value between 1950(inclusive) and 2050(inclusive)")
        if type(month) != int:
            raise TypeError("Time __init__() month expected type int")
        if month < 1 or month > 12:
            raise ValueError("Time __init__() month expected int value between 1(inclusive) and 12(inclusive)")
        if type(day) != int:
            raise TypeError("Time __init__() day expected type int")
        if day < 1 or day > 31:
            raise ValueError("Time __init__() day expected int value between 1(inclusive) and 31(inclusive)")
        if type(hour) != int:
            raise TypeError("Time __init__() hour expected type int")
        if hour < 0 or hour > 23:
            raise ValueError("Time __init__() hour expected int value between 0(inclusive) and 23(inclusive)")
        if type(minute) != int:
            raise TypeError("Time __init__() minute expected type int")
        if minute < 0 or minute > 59:
            raise ValueError("Time __int__() minute expected int value between 0(inclusive) and 59(inclusive)")

        # Initialise
        self.year = year
        self.month = month
        self.day = day
        self.hour = hour
        self.minute = minute
    
    
    def get_year(self) -> int:
        return self.year
    
    def get_month(self) -> int:
        return self.month
    
    def get_day(self) -> int:
        return self.day
    
    def get_hour(self) -> int:
        return self.hour
    
    def get_minute(self) -> int:
        return self.minute
    

    def set_year(self, year: int) -> None:
        if type(year) != int:
            raise TypeError("Time set_year() year expected type int")
        if year < 1950 or year > 2050:
            raise ValueError("Time set_year() year expected int value between 1950(inclusive) and 2050(inclusive)")
        self.year = year

    def set_month(self, month: int) -> None:
        if type(month) != int:
            raise TypeError("Time set_month() month expected type int")
        if month < 1 or month > 12:
            raise ValueError("Time set_month() month expected int value between 1(inclusive) and 12(inclusive)")
        self.month = month
    
    def set_day(self, day: int) -> None:
        if type(day) != int:
            raise TypeError("Time set_day() day expected type int")
        if day < 1 or day > 31:
            raise ValueError("Time set_day() day expected int value between 1(inclusive) and 31(inclusive)")
        self.day = day
    
    def set_hour(self, hour: int) -> None:
        if type(hour) != int:
            raise TypeError("Time set_hour() hour expected type int")
        if hour < 0 or hour > 23:
            raise ValueError("Time set_hour() hour expected int value between 0(inclusive) and 23(inclusive)")
        self.hour = hour
    
    def set_minute(self, minute: int) -> None:
        if type(minute) != int:
            raise TypeError("Time set_minute() minute expected type int")
        if minute < 0 or minute > 59:
            raise ValueError("Time set_minute() minute expected int value between 0(inclusive) and 59(inclusive)")
        self.minute = minute

    
    def get_object(self) -> dict:
        return {
            'dateTime': str(self),
            'timeZone': 'Australia/Melbourne'
        }
    

    def __str__(self) -> str:
        return datetime.datetime(self.year, self.month, self.day, hour=self.hour, minute=self.minute).isoformat() + "Z"

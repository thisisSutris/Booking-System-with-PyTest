class Organiser:
    def __init__(self, email: str, is_self: bool = False) -> None:
        # Preconditions
        if type(email) != str:
            raise TypeError("Organiser __init__() email expected type str")
        if type(is_self) != bool:
            raise TypeError("Organiser __init__() is_self expected type bool")
        
        # Initialise
        self.email = email
        self.is_self = is_self
    

    def get_email(self) -> str:
        return self.email

    def get_is_self(self) -> bool:
        return self.is_self
    

    def set_email(self, email: str) -> None:
        if type(email) != str:
            raise TypeError("Organiser set_email() email expected type str")
        self.email = email
    
    
    def get_object(self) -> dict:
        return {
            'email': self.email,
            'self': self.is_self,
        }

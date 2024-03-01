class Attendee():
    STATUS_ACCEPTED = "accepted"
    STATUS_DECLINED = "declined"
    STATUS_PENDING = "needsAction"
    
    def __init__(self, email: str, organiser: bool = False, is_self: bool = False) -> None:
        # Preconditions
        if type(email) != str:
            raise ValueError("Attendee __init__() email expected type str")
        if type(organiser) != bool:
            raise ValueError("Attendee __init__() organiser expected type bool")
        if type(is_self) != bool:
            raise ValueError("Attendee __init__() is_self expected type bool")
        
        # Initialise
        self.email = email
        self.organiser = organiser
        self.is_self = is_self
        self.response_status = self.STATUS_PENDING
    

    def get_email(self) -> str:
        return self.email
    
    def get_organiser(self) -> bool:
        return self.organiser
    
    def get_is_self(self) -> bool:
        return self.is_self
    
    def get_response_status(self) -> str:
        return self.response_status
    

    def set_email(self, email: str) -> None:
        if type(email) != str:
            raise ValueError("Attendee set_email() email expected type str")
        self.email = email
    
    def set_organiser(self, organiser: bool) -> None:
        if type(organiser) != bool:
            raise ValueError("Attendee set_organiser() organiser expected type bool")
        self.organiser = organiser
    
    def set_response_status(self, response_status: str) -> None:
        if type(response_status) != str:
            raise ValueError("Attendee set_response_status() response_status expected type str")
        if response_status not in ["accepted", "declined", "needsAction"]:
            raise ValueError("Invalid response status, must be one of 'accepted', 'declined' or 'needsActions'")
        self.response_status = response_status
    
    def accept_invitation(self) -> None:
        self.response_status = self.STATUS_ACCEPTED
    
    def decline_invitation(self) -> None:
        self.response_status = self.STATUS_DECLINED


    def get_object(self) -> dict:
        return {
            'email': self.email,
            'organizer': self.organiser,
            'self': self.is_self,
            'response_status': self.response_status
        }


    def __str__(self) -> str:
        return self.email

class Location:
    LOCATION_ADDRESS = 1
    LOCATION_LINK = 2

    def __init__(self) -> None:
        self.location_type = 0
        self.link = None
        self.street_number = None
        self.street_name = None
        self.suburb = None
        self.state = None
        self.postcode = None
        self.country = None
    

    def init_address(self, street_number: str, street_name: str, suburb: str, state: str, postcode: str, country: str) -> None:
        # Preconditions
        if type(street_number) != str:
            raise TypeError("Location init_address() street_number expected type str")
        if type(street_name) != str:
            raise TypeError("Location init_address() street_name expected type str")
        if type(suburb) != str:
            raise TypeError("Location init_address() suburb expected type str")
        if type(state) != str:
            raise TypeError("Location init_address() state expected type str")
        if type(postcode) != str:
            raise TypeError("Location init_address() postcode expected type str")
        if type(country) != str:
            raise TypeError("Location init_address() country expected type str")

        # Initialise
        self.location_type = self.LOCATION_ADDRESS
        self.street_number = street_number
        self.street_name = street_name
        self.suburb = suburb
        self.state = state
        self.postcode = postcode
        self.country = country
    

    def init_link(self, link: str) -> None:
        # Preconditions
        if type(link) != str:
            raise TypeError("Location init_link() link expected type str")
        
        # Initialise
        self.location_type = self.LOCATION_LINK
        self.link = link


    def get_street_number(self) -> str:
        return self.street_number

    def get_street_name(self) -> str:
        return self.street_name
    
    def get_suburb(self) -> str:
        return self.suburb
    
    def get_state(self) -> str:
        return self.state
    
    def get_postcode(self) -> str:
        return self.postcode
    
    def get_country(self) -> str:
        return self.country
    
    def get_link(self) -> str:
        return self.link
    

    def set_street_number(self, street_number: str) -> None:
        if type(street_number) != str:
            raise TypeError("Location set_street_number() street_number expected type str")
        self.street_number = street_number

    def set_street_name(self, street_name: str) -> None:
        if type(street_name) != str:
            raise TypeError("Location set_street_name() street_name expected type str")
        self.street_name = street_name
    
    def set_suburb(self, suburb: str) -> None:
        if type(suburb) != str:
            raise TypeError("Location set_suburb() suburb expected type str")
        self.suburb = suburb
    
    def set_state(self, state: str) -> None:
        if type(state) != str:
            raise TypeError("Location set_state() state expected type str")
        self.state = state
    
    def set_postcode(self, postcode: str) -> None:
        if type(postcode) != str:
            raise TypeError("Location set_postcode() postcode expected type str")
        self.postcode = postcode
    
    def set_country(self, country: str) -> None:
        if type(country) != str:
            raise TypeError("Location set_country() country expected type str")
        self.country = country
    
    def set_link(self, link: str) -> None:
        if type(link) != str:
            raise TypeError("Location set_link() link expected type str")
        self.link = link
    

    def get_object(self) -> str:
        return str(self)

    def __str__(self) -> str:
        if self.location_type == self.LOCATION_ADDRESS:
            string = "{} {}\n{} {} {}\n{}".format(self.street_number, self.street_name, self.suburb, self.state, self.postcode, self.country)
        elif self.location_type == self.LOCATION_LINK:
            string = self.link
        return string
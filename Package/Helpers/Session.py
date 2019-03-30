# Class Session: to store current user information
class Session:

    def __init__(self,_id,firstName,lastName,email,password,phoneNumber):
        self._id=_id
        self.firstName=firstName
        self.lastName = lastName
        self.email = email
        self.password = password
        self.phoneNumber= phoneNumber

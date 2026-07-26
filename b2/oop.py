# User: fullname, birthdate, username, emai, pasword, gender
class User:
    def __init__(self, fullname, birthdate, username, emai, pasword, gender) -> None:
        #TODO: khai bao bien can dung (private)
        self.__fullname = fullname
        self.__birthdate = birthdate
        self.__username =username
        self.__emai=emai
        self.__pasword=pasword
        self.__gender=gender

    def get_full_name(self) -> Any:
        return self.__full_name
    def get_birthdate(self) -> Any:
        return self.__birthdate
    def get_gender(self) -> Any:
        return self.__gender
    def get_username(self) -> Any:
        return self.__username
    def get_password(self) -> Any:
        return self.__password
    def get_email(self) -> Any:
        return self.__email
    def set_username(self, username)->None:
        if len(username) > 6:
            self.__username = username
        else:
            print("Username must be longer than 6 characters.")

    def set_password(self, new_password, old_password)->None:
        if old_password == self.__password:
            if len(new_password) >6:
                self.__password = new_password
            else:
                print("New password must be lpnger than 6 characters.")
        else:
          print("Old password is incorrect")

    def get_gender(self,gender)-> None:
        if gender in ['male', 'female', 'other']:
            self.__gender = gender
        else:
            print("Invalid gender, Please choose from 'male', 'female', or 'other'.")






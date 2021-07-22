from utils import login_credentials


class LoginDAO:

    @staticmethod
    def check_login(username, password):
        return_text = ""
        if login_credentials.username == username:
            return_text = "Username is correct"
        else:
            return_text = "username is incorrect"

        if login_credentials.password == password:
            return_text += "Password is correct"
        else:
            return_text = "Password is incorrect"

        return return_text

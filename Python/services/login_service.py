from daos.login_dao import LoginDAO


class LoginService:
    login_dao = LoginDAO()

    @classmethod
    def check_login(cls, username, password):
        return cls.login_dao.check_login(username, password)

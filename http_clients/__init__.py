from requests import Session, Response


class RestClient:

    def __init__(
            self,
            base_url: str,
            base_headers: dict = None,
        ):
        self.base_url = base_url
        self.session: Session = Session()

        if base_headers:
            self.session.headers = base_headers
        


    def auth_register(
        self,
        username: str,
        email: str,
        password: str
    ) -> Response:
        return self.session.post(
            url=f"{self.base_url}/auth/register",
            json={
                "username": username,
                "email": email,
                "password": password
            }
        )
        
        
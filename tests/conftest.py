from pytest import fixture
from http_clients import RestClient
import settings


@fixture
def client():
    return RestClient(
        base_url=settings.FLASK_APP_API_URL,
        base_headers={
            "Content-Type": "application/json"
        }
    )
from unittest import mock
from app.main import can_access_google_page


@mock.patch("app.main.has_internet_connection", return_value=True)
@mock.patch("app.main.valid_google_url", return_value=True)
def test_google_page_with_url_cnnection(mocked_url: callable,
                                        mocked_internet: callable) -> None:
    assert can_access_google_page("https://google.com") == "Accessible"


@mock.patch("app.main.has_internet_connection", return_value=False)
@mock.patch("app.main.valid_google_url", return_value=True)
def test_google_page_with_url(mocked_url: callable,
                              mocked_internet: callable) -> None:
    assert can_access_google_page("https://google.com") == "Not accessible"


@mock.patch("app.main.has_internet_connection", return_value=False)
@mock.patch("app.main.valid_google_url", return_value=False)
def test_google_page(mocked_url: callable,
                     mocked_internet: callable) -> None:
    assert can_access_google_page("https://google.com") == "Not accessible"


@mock.patch("app.main.has_internet_connection", return_value=True)
@mock.patch("app.main.valid_google_url", return_value=False)
def test_google_page_with_connection(mocked_url: callable,
                                     mocked_internet: callable) -> None:
    assert can_access_google_page("https://google.com") == "Not accessible"

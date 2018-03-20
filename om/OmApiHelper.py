import requests
from requests.auth import HTTPBasicAuth


class OmApiHelper:

    def __init__(self, url, username, password, verify_ssl):

        self.url = url
        self.username = username
        self.verify_ssl = verify_ssl

        response = requests.post(
            "https://" + url + "/uaa/oauth/token?grant_type=password",
            auth=HTTPBasicAuth("opsman", ""),
            data={"username": username, "password": password},
            verify=verify_ssl
        )

        if response.status_code == requests.codes.ok:
            self.token = response.json()["token_type"] + " " + response.json()["access_token"]
        # elif response.status_code == requests.codes.unauthorized:
        # throw exception

    def get(self, endpoint):

        response = requests.get(
            "https://" + self.url + endpoint,
            headers={"Accept": "application/json", "Content-Type": "application/json", "Authorization": self.token},
            verify=self.verify_ssl
        )

        if response.status_code == requests.codes.ok:
            return response.json()
        # elif response.status_code == requests.codes.unauthorized:
        # throw exception

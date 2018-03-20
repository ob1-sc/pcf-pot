import argparse
import requests

# setup an argument parser
from requests.auth import HTTPBasicAuth


def login(om_url, username, password, verify_ssl):

    oauth_token_response = requests.post(
        "https://" + om_url + "/uaa/oauth/token?grant_type=password",
        auth=HTTPBasicAuth("opsman", ""),
        data={"username": username, "password": password},
        verify=verify_ssl
    )

    return oauth_token_response.json()["token_type"] + " " + oauth_token_response.json()["access_token"]


def main():

    parser = argparse.ArgumentParser(description='Tile Param Checker')

    # define the program arguments
    parser.add_argument("om_url")
    parser.add_argument("username")
    parser.add_argument("password")
    parser.add_argument("--skip-ssl-validation", action="store_false", dest="verify_ssl")

    # parse the arguments
    args = parser.parse_args()

    # login
    authorization = login(args.om_url, args.username, args.password, args.verify_ssl)

    print authorization

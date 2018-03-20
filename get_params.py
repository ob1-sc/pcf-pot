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


def get_tile_guid(om_url, auth, verify_ssl, tile_slug):

    get_staged_products_response = requests.get(
        "https://" + om_url + "/api/v0/staged/products",
        headers={"Accept": "application/json", "Content-Type": "application/json", "Authorization": auth},
        verify=verify_ssl
    )

    # get the staged tiles
    staged_tiles_json = get_staged_products_response.json()

    for staged_tile in staged_tiles_json:
        if staged_tile["type"] == tile_slug:
            tile_guid = staged_tile["guid"]
            break

    return tile_guid


def get_tile_params(om_url, auth, verify_ssl, tile_guid) :

    get_tile_params_response = requests.get(
        "https://" + om_url + "/api/v0/staged/products/" + tile_guid + "/properties",
        headers={"Accept": "application/json", "Content-Type": "application/json", "Authorization": auth},
        verify=verify_ssl
    )

    return get_tile_params_response.json()


def main():

    parser = argparse.ArgumentParser(description='Tile Param Checker')

    # define the program arguments
    parser.add_argument("om_url")
    parser.add_argument("username")
    parser.add_argument("password")
    parser.add_argument("tile_slug")
    parser.add_argument("--skip-ssl-validation", action="store_false", dest="verify_ssl")

    # parse the arguments
    args = parser.parse_args()

    # login
    auth = login(args.om_url, args.username, args.password, args.verify_ssl)

    # get the tile deployment id
    tile_guid = get_tile_guid(args.om_url, auth, args.verify_ssl, args.tile_slug)

    # get the tile properties
    tile_properties = get_tile_params(args.om_url, auth, args.verify_ssl, tile_guid)

    print(tile_properties)

main()
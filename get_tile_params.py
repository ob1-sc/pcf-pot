import argparse

from http import OmApiHelper


def get_tile_guid(om_api_helper, tile_slug):

    staged_tiles_json = om_api_helper.get("/api/v0/staged/products")

    for staged_tile in staged_tiles_json:
        if staged_tile["type"] == tile_slug:
            tile_guid = staged_tile["guid"]
            break

    return tile_guid


def get_tile_params(om_api_helper, tile_guid):

    tile_params_json = om_api_helper.get("/api/v0/staged/products/" + tile_guid + "/properties")

    return tile_params_json


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

    # login and create a helper for talking to the opsman API
    om_api_helper = OmApiHelper(args.om_url, args.username, args.password, args.verify_ssl)

    # get the tile deployment id
    tile_guid = get_tile_guid(om_api_helper, args.tile_slug)

    # get the tile properties
    tile_properties = get_tile_params(om_api_helper, tile_guid)

    print(tile_properties)

main()
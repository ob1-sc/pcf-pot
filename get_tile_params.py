import argparse
import pprint

from om import OmApiHelper
from om.tile_helper import get_tile_guid, get_tile_params


def generate_params_yml(tile_properties):

    with open("tile_params.yml", "w") as tile_params_yaml:

        # write the yaml header
        tile_params_yaml.write("---\n\n")

        # loop through all of the tile properties
        for tile_property in tile_properties["properties"]:

            # get the tile property config
            tile_propery_config = tile_properties["properties"][tile_property]

            # if the property is configurable
            if tile_propery_config["configurable"]:

                # write the type (boolean, string, selector, etc)
                if "type" in tile_propery_config:
                    property_type = tile_propery_config["type"]
                    tile_params_yaml.write("# Type: " + property_type + "\n")

                # write if the property is optional
                if "optional" in tile_propery_config:
                    property_optional = tile_propery_config["optional"]
                    tile_params_yaml.write("# Optional: " + str(property_optional) + "\n")

                # write the property default value
                if "value" in tile_propery_config:
                    property_value = tile_propery_config["value"]

                    if isinstance(property_value, basestring):
                        tile_params_yaml.write("# Default Value: " + property_value.encode("utf-8") + "\n")
                    else:
                        tile_params_yaml.write("# Default Value: " + str(property_value) + "\n")

                # write the property options
                if "options" in tile_propery_config:
                    property_options = tile_propery_config["options"]
                    tile_params_yaml.write("# Options: " + str(property_options) + "\n")

                # write the property name (minus the leading period '.')
                tile_params_yaml.write(tile_property[1:] + ": \n\n")


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

    # generate a tile properties yml
    generate_params_yml(tile_properties)

main()

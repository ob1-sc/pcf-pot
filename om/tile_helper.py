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

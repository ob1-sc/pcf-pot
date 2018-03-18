import argparse

# setup an argument parser
parser = argparse.ArgumentParser(description='Tile Param Checker')

# define the program arguments
parser.add_argument("om_url")
parser.add_argument("username")
parser.add_argument("password")

# parse the arguments
args = parser.parse_args()

# define the uaa login url
uaa_login_url = args.om_url + "/uaa/login"

def login(username, password):

    oauthTokenResponse = requests.post(
        "https://login." + foundationUrl + "/oauth/token?grant_type=password&client_id=cf",
        data={"username": username, "password": password, 'client_id': "cf"},
        auth=("cf", ""),
        verify=skipSsl
    )

    return oauthTokenResponse.json()["token_type"] + " " + oauthTokenResponse.json()["access_token"]


########################### MAIN ############################

# login
authorization = login("admin", "admin")

print authorization

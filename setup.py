from dotenv import load_dotenv
from utils import env_vars, get_env_vars, Venmo
from venmo_api import Client



### RETRIEVE VENMO ACCESS TOKEN
# # Get your access token. You will need to complete the 2FA process
# access_token=Client.get_access_token(username='xxxxxx',
#                                        password='xxxxx')
# # This will print the access token after the first time you use the library.
#
# print("My access token:", access_token)

### RETRIEVE VENMO USER IDS

load_dotenv()

access_token, chat_id, bot_token, *tail = get_env_vars(env_vars)

venmo = Venmo(access_token)

userId = venmo.get_user_id_by_username("Kevinwcao")
print("kcao userid:", userId)

print("san:", venmo.get_user_id_by_username("sanbae"))

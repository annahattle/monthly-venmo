from venmo_api import Client

# Get your access token. You will need to complete the 2FA process
access_token=Client.get_access_token(username='xxxxxx',
                                       password='xxxxx')
# This will print the access token after the first time you use the library.

print("My access token:", access_token)

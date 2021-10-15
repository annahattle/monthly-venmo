from venmo_api import Client
from dotenv import load_dotenv
from notifiers import get_notifier
from datetime import datetime

from utils import get_env, env_vars, get_month, Venmo, Telegram

def main(now):
  """
  The main function which initiates the script.
  """

  load_dotenv()  # take environment variables from .env.
  actualVars = []
  for var in env_vars:
    actualVars.append(get_env(var))

  access_token, chat_id, bot_token, k_friend_id, s_friend_id, l_friend_id, j_friend_id, p_friend_id = actualVars

  month = get_month(now)
  venmo = Venmo(access_token)
  telegram = Telegram(bot_token, chat_id)

  friends =[
    {
      "name": "Kev",
      "id": k_friend_id,
    },
    {
      "name": "San",
      "id": s_friend_id,
    },
    {
      "name": "Liz",
      "id": l_friend_id,
    },
    {
      "name": "Joe",
      "id": j_friend_id,
    },
    {
      "name": "Pav",
      "id": p_friend_id,
    },
  ]

  successfulRequests = []
  expectedRequests = len(friends)

  for friend in friends:
    name = friend["name"]
    id = friend["id"]
    description = "Spotify for the month of " + month + "— Automated Request from Anna"
    amount = 2.86
    message = f"""I have successfully requested money from {name}. — Efron"""
    success = venmo.request_money(id, amount, description, telegram.send_message(message))
    if success:
      successfulRequests.append(success)

  if len(successfulRequests) == expectedRequests:
    print("✅ Ran script successfully and sent " + str(expectedRequests) + " Venmo requests.")
  else:
    print("❌ Something went wrong. Only sent " + str(len(successfulRequests)) + "/" + str(expectedRequests) + " venmo requests.")

now = datetime.now()
main(now)

from datetime import datetime
from utils import get_env, verify_env_vars, env_vars, get_env_vars, Telegram, Venmo
from dotenv import load_dotenv

def main(now):
  load_dotenv()
  date = now.strftime("%B %d, %Y")
  time = now.strftime("%H:%M%p")
  print(f'🕘 Monthly health check running on {date} at {time}.\n')

  print("🔍 Verifying environment variables...")
  numOfExpected =  8
  envVarsAreDefined = verify_env_vars(env_vars, numOfExpected)

  if envVarsAreDefined:
    print(f'✅ Found all {numOfExpected} environment variables.\n')
  else:
    print('❌ Failed to verify environment variables.\n')

  access_token, chat_id, bot_token, *tail = get_env_vars(env_vars)

  venmo = Venmo(access_token)
  telegram = Telegram(bot_token, chat_id)

  print("🤑 Verifying Venmo client is working...")
  userId = venmo.get_user_id_by_username("Kevinwcao")

  if userId:
    print('✅ Venmo client is working as expected.\n')
  else:
    print('❌ Failed to get userId using Venmo client.\n')

  returnedUserId = bool(userId)

  if envVarsAreDefined and returnedUserId:
    print('✅ Everything looks good in the health check')
    message = """Checking in from your Monthly Venmo script. Everything looks to be in order."""
    telegram.send_message(message)
  elif envVarsAreDefined:
    print('❌ Venmo client might not be working. 1/2 checks failed in health script.')
    message = """The environment variables in your Monthly Venmo script are working, but the Venmo client isn't"""
    telegram.send_message(message)
  elif returnedUserId:
    print('❌ Envrionment variables check did not pass. 1/2 checks failed in health script.')
    message = """The Venmo client in your Monthly Venmo script is working, but there is a problem with the environment variables."""
    telegram.send_message(message)
  else:
    print('❌ Venmo client and environment variables did not pass. 2/2 checks failed in health script.')
    message = """The Venmo client and the environment variables are both failing in your Monthly Venmo script."""
    telegram.send_message(message)

# Grab current date and passing in when running function
now = datetime.now()
main(now)

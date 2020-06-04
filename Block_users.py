import twitter
import pandas as pd
import csv
import time

start = time.time()
accounts = []
non_existing_account = []

# You find these in twitter dev sections
access_token = ""
access_token_secret = ""
api_key = ""
api_key_secret = ""

api = twitter.Api(consumer_key=api_key,
                  consumer_secret=api_key_secret,
                  access_token_key=access_token,
                  access_token_secret= access_token_secret,
                  sleep_on_rate_limit=True)

print(api.VerifyCredentials())

def block_user(list_user):
    user_unknown = []
    nb_left = len(list_user)
    for user in list_user:
        try:
            api.CreateBlock(screen_name=user)
            print("Blocked user:", user)
            nb_left -= 1
            print(f"il reste {nb_left} left to block")
        except Exception as e:
            if e == "[{'code': 50, 'message': 'User not found.'}]":
                nb_left -= 1
                print(f"{user} not found")
                print(f"il reste {nb_left} left to block")
            else:
                # Useless
                print(e)
                user_unknown.append(user)
                print(len(user_unknown))
                pass

def unblock_user(list_user):
    nb_left = len(list_user)
    for user in list_user:
        try:
            api.DestroyBlock(user_id=user)
            time.sleep(0.2)
            print("Unblocked user :", user)
            nb_left -= 1
            print(f"il reste {nb_left} left to unblock")
        except Exception as e:
            if e == "[{'code': 50, 'message': 'User not found.'}]":
                nb_left -= 1
                print(f"{user} not found")
                print(f"il reste {nb_left} left to unblock")
            else:
                print(e)
                pass

# Get all account and put them in a list
with open("accounts.csv", newline='') as csvfile:
    accountreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for account in accountreader:
        accounts.append(str(account)[2:-2])

# Start the block / unblock
block_user(accounts)

stop = time.time()
print("Running time : ", stop - start)
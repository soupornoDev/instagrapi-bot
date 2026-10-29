from instagrapi import Client
import os
from dotenv import load_dotenv

# 1. Load the environment variables from the .env file
load_dotenv()

username=os.getenv("IG_USERNAME")
password=os.getenv("IG_PASSWORD")

cl = Client()
cl.login(username,password)

user = cl.user_info_by_username("instagram")
print(user.full_name, user.follower_count)

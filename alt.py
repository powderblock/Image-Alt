# reddit interface for Python
import praw
# oauth_file.py is a local file that contains the account's OAuth info.
# See the GitHub repo for the example file `oauth_file.py.example`
import oauth_file

# Set our user_agent so reddit knows what they are dealing with:
user_agent = ("A reposting script for people who have Imgur blocked at their school / work. Written in PRAW & SBI. See: https://github.com/powderblock/Image-Alt")
# Setup out Reddit object so that it uses out user_agent
r = praw.Reddit(user_agent)

# Call the OAuth_Info() function from oauth_file:
# We pass our file our Reddit object so that it can manipulate it.
oauth_file.OAuth_Info(r)

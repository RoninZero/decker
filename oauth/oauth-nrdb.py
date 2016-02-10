#!/usr/bin/env python3
import os
import hidden

# API testing for github.com
# ienvironment variable Needed for to use oauth2 over http (not https) url endpoints
os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'

# Credentials you get from registering a new application
creds = nrdb_oath_creds

# TODO fix the code below.
client_id = 'clientID'
client_secret = 'client_secret'
redirect_uri = 'http://this.is.the.redirect.url/'

# OAuth endpoints given in the GitHub API documentation
#authorization_base_url = 'https://github.com/login/oauth/authorize'
authorization_base_url = 'http://netrunnerdb.com/oauth/v2/auth'
token_url = 'http://netrunnerdb.com/oauth/v2/token'

from requests_oauthlib import OAuth2Session
nrdb = OAuth2Session(client_id, redirect_uri=redirect_uri)

# Redirect user to GitHub for authorization
authorization_url, state = nrdb.authorization_url(authorization_base_url)
print('Please go here and authorize,', authorization_url)

# Get the authorization verifier code from the callback url
redirect_response = input('Paste the full redirect URL here:')

# Fetch the access token
nrdb.fetch_token(token_url, client_secret=client_secret,
        authorization_response=redirect_response)

# Fetch a protected resource, i.e. user profile
r = nrdb.get('http://netrunnerdb.com/api_oauth2/decks')
print(r.content)

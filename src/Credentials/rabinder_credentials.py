import pyotp
name="Rabinder"
user_id="XR29452"
pswd="reset1234"
pin='7675'
first='7'
second='6'
third='7'
fourth='5'
client_id = '0HMOFAG8AD-100'
secret_key = '2OY8C5EO1C'
redirect_uri = 'https://fyers.in/'
auth_code='eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJhcGkubG9naW4uZnllcnMuaW4iLCJpYXQiOjE2NTM5ODEzMDIsImV4cCI6MTY1NDAxMTMwMiwibmJmIjoxNjUzOTgwNzAyLCJhdWQiOiJbXCJ4OjJcIiwgXCJkOjJcIiwgXCJkOjFcIiwgXCJ4OjFcIiwgXCJ4OjBcIl0iLCJzdWIiOiJhdXRoX2NvZGUiLCJkaXNwbGF5X25hbWUiOiJYUzA4MjYxIiwibm9uY2UiOiIiLCJhcHBfaWQiOiJTNUtNVkRZS1lKIiwidXVpZCI6IjkzNTkwMzRlMmNmNjQxMTNhOTExYzg2ZGRmZTAwZTM5IiwiaXBBZGRyIjoiMC4wLjAuMCIsInNjb3BlIjoiIn0.dUvb0CmsXyaD2wAQT5MCUxraYz473Ks17cZHBehXD1A'
app_id="0HMOFAG8AD-100"
key='TK6OW7YZDDSIB6G4EM66YXI3BLO7PVAR'
with open('./Token/rabinder_token.txt','r')as f:
	cr=f.read()
file_location='./Token/rabinder_token.txt'

access_token=cr
otp=pyotp.TOTP(key)
totp=otp.now()
# print(access_token)

# url=https://api.fyers.in/api/v2/generate-authcode?client_id=S5KMVDYKYJ-100&redirect_uri=https%3A%2F%2Ffyers.in%2F&response_type=code&state=None

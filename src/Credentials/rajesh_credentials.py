import pyotp
name="Rajesh"
user_id="XR29719"
pswd=""
pin="1234"
first='1'
second='2'
third='3'
fourth='4'
client_id = 'W87P0WWZH8-100'
secret_key = 'QUVH3DTNYA'
redirect_uri = 'https://fyers.in/'
auth_code='eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJhcGkubG9naW4uZnllcnMuaW4iLCJpYXQiOjE2NTM5ODEzMDIsImV4cCI6MTY1NDAxMTMwMiwibmJmIjoxNjUzOTgwNzAyLCJhdWQiOiJbXCJ4OjJcIiwgXCJkOjJcIiwgXCJkOjFcIiwgXCJ4OjFcIiwgXCJ4OjBcIl0iLCJzdWIiOiJhdXRoX2NvZGUiLCJkaXNwbGF5X25hbWUiOiJYUzA4MjYxIiwibm9uY2UiOiIiLCJhcHBfaWQiOiJTNUtNVkRZS1lKIiwidXVpZCI6IjkzNTkwMzRlMmNmNjQxMTNhOTExYzg2ZGRmZTAwZTM5IiwiaXBBZGRyIjoiMC4wLjAuMCIsInNjb3BlIjoiIn0.dUvb0CmsXyaD2wAQT5MCUxraYz473Ks17cZHBehXD1A'
app_id="W87P0WWZH8-100"
key="XVKUWP42GTBMHUXT5AUD2XQO4V6QK3TO"
file_location='./Token/rajesh_token.txt'
with open('./Token/rajesh_token.txt','r')as f:
    cr=f.read()

access_token=cr
otp=pyotp.TOTP(key)
totp=otp.now()
# print(access_token)

# url=https://api.fyers.in/api/v2/generate-authcode?client_id=S5KMVDYKYJ-100&redirect_uri=https%3A%2F%2Ffyers.in%2F&response_type=code&state=None

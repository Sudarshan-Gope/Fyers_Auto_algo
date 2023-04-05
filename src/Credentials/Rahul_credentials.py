import pyotp
name="Rahul"
user_id="XR29752"
pswd="reset1234"
pin="8055"
first='8'
second='0'
third='5'
fourth='5'
client_id = 'HRWWC1LJOT-100'
secret_key = 'XK28V6W5J5'
redirect_uri = 'https://fyers.in/'
auth_code='eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJhcGkubG9naW4uZnllcnMuaW4iLCJpYXQiOjE2NTM5ODEzMDIsImV4cCI6MTY1NDAxMTMwMiwibmJmIjoxNjUzOTgwNzAyLCJhdWQiOiJbXCJ4OjJcIiwgXCJkOjJcIiwgXCJkOjFcIiwgXCJ4OjFcIiwgXCJ4OjBcIl0iLCJzdWIiOiJhdXRoX2NvZGUiLCJkaXNwbGF5X25hbWUiOiJYUzA4MjYxIiwibm9uY2UiOiIiLCJhcHBfaWQiOiJTNUtNVkRZS1lKIiwidXVpZCI6IjkzNTkwMzRlMmNmNjQxMTNhOTExYzg2ZGRmZTAwZTM5IiwiaXBBZGRyIjoiMC4wLjAuMCIsInNjb3BlIjoiIn0.dUvb0CmsXyaD2wAQT5MCUxraYz473Ks17cZHBehXD1A'
app_id="HRWWC1LJOT-100"
key='Y2CCJIM4PDJ2CDBN4TRO2DHGGSHR7PZ2'
file_location='./Token/Rahul_token.txt'
with open('./Token/Rahul_token.txt','r')as f:
    cr=f.read()

access_token=cr
otp=pyotp.TOTP(key)
totp=otp.now()
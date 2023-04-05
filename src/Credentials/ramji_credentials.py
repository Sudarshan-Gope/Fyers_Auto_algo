import pyotp
name="Ramji"
user_id="XR29707"
pswd=""
pin='7070'
first='7'
second='0'
third='7'
fourth='0'
client_id = 'NC4SU96BH9-100'
secret_key = 'SCRS4ITDZF'
redirect_uri = 'https://fyers.in/'
auth_code='eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJhcGkubG9naW4uZnllcnMuaW4iLCJpYXQiOjE2NTM5ODEzMDIsImV4cCI6MTY1NDAxMTMwMiwibmJmIjoxNjUzOTgwNzAyLCJhdWQiOiJbXCJ4OjJcIiwgXCJkOjJcIiwgXCJkOjFcIiwgXCJ4OjFcIiwgXCJ4OjBcIl0iLCJzdWIiOiJhdXRoX2NvZGUiLCJkaXNwbGF5X25hbWUiOiJYUzA4MjYxIiwibm9uY2UiOiIiLCJhcHBfaWQiOiJTNUtNVkRZS1lKIiwidXVpZCI6IjkzNTkwMzRlMmNmNjQxMTNhOTExYzg2ZGRmZTAwZTM5IiwiaXBBZGRyIjoiMC4wLjAuMCIsInNjb3BlIjoiIn0.dUvb0CmsXyaD2wAQT5MCUxraYz473Ks17cZHBehXD1A'
app_id="NC4SU96BH9-100"
key='OSUM2NI47B4DK25XHKEIG664NB3EJCAU'
file_location='./Token/ramji_token.txt'
with open('./Token/ramji_token.txt','r')as f:
	cr=f.read()

access_token=cr
otp=pyotp.TOTP(key)
totp=otp.now()
# print(access_token)

# url=https://api.fyers.in/api/v2/generate-authcode?client_id=S5KMVDYKYJ-100&redirect_uri=https%3A%2F%2Ffyers.in%2F&response_type=code&state=None

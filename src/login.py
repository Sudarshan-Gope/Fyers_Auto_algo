from selenium import webdriver

import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from fyers_api import fyersModel
from fyers_api import accessToken
import platform
import os
import pyotp
# from Credentials import rabinder_credentials as rab
from Credentials import sudarshan_credentials as sud
from Credentials import ramji_credentials as rc



def login(name,client_id,user_id,totp_key,first,second,third,fourth,file_location,access_token,secret_key):
    #check access token authentication
    fyers = fyersModel.FyersModel(client_id=client_id, token=access_token,log_path='./log/')
    # print(fyers.get_profile())
    data=fyers.get_profile()
    if data['s'] =='ok':
        print(f'{name}: Valid Access Token ')
        # print('########## Executing Program ############')
    else:
        print(f"{name}: Need to get Access Token")
        os_check=platform.system()

        if os_check=='Windows':
            cur_path = os.path.dirname(__file__)

            path = os.path.relpath('..\\chromedriver\\chromedriver.exe')
        elif os_check=="Linux":
            cur_path = os.path.dirname(__file__)

            path = os.path.relpath('../chromedriver/chromedriver')

        # initialize the Chrome driver
        s = Service(path)
        driver = webdriver.Chrome(service=s)

        #head to login page
        driver.get("https://api.fyers.in/api/v2/generate-authcode?client_id="+client_id+"&redirect_uri=https%3A%2F%2Ffyers.in%2F&response_type=code&state=None")

        # find username/email field and send the username itself to the input field
        driver.find_element(By.ID,"fy_client_id").send_keys(user_id)
        time.sleep(2)
        # click button
        driver.find_element(By.ID,"clientIdSubmit").click()
        time.sleep(2)
        totp = pyotp.TOTP(totp_key)
        otp=totp.now()
        driver.find_element(By.ID,"first").send_keys(otp[0])
        driver.find_element(By.ID,"second").send_keys(otp[1])
        driver.find_element(By.ID,"third").send_keys(otp[2])
        driver.find_element(By.ID,"fourth").send_keys(otp[3])
        driver.find_element(By.ID,"fifth").send_keys(otp[4])
        driver.find_element(By.ID,"sixth").send_keys(otp[5])
        driver.find_element(By.ID,"confirmOtpSubmit").click()


        time.sleep(2)

        driver.find_element(By.XPATH,"//div[@id='pin-container']//input[@id='first']").send_keys(first)
        driver.find_element(By.XPATH,"//div[@id='pin-container']//input[@id='second']").send_keys(second)
        driver.find_element(By.XPATH,"//div[@id='pin-container']//input[@id='third']").send_keys(third)
        driver.find_element(By.XPATH,"//div[@id='pin-container']//input[@id='fourth']").send_keys(fourth)

        driver.find_element(By.ID,"verifyPinSubmit").click()

        time.sleep(2)
        url=driver.current_url
        driver.close()
        new_url=url.rpartition("https://fyers.in/?s=ok&code=200&auth_code=")[2]
        auth_code=new_url.partition("&state=None")[0]
        session=accessToken.SessionModel(client_id=client_id,
        secret_key=secret_key,redirect_uri=url,
        response_type='code', grant_type='authorization_code')
        session.set_token(auth_code)
        response = session.generate_token()
        access_token = response["access_token"]
        with open(file_location,'w') as f:
            f.write(access_token)
        print("Access Token Generated")
        # print(access_token)

def login_process(msg):
    name=msg.name
    client_id=msg.client_id
    user_id=msg.user_id
    secret_key=msg.secret_key
    access_token=msg.access_token
    url=msg.redirect_uri
    totp_key=msg.key
    first=msg.first
    second=msg.second
    third=msg.third
    fourth=msg.fourth
    file_location=msg.file_location
    login(name,client_id,user_id,totp_key,first,second,third,fourth,file_location,access_token,secret_key)


login_process(sud)
# login_process(rab)
# login_process(rc)
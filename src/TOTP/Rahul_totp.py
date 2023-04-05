import pyotp
def totp1():
    otp=pyotp.TOTP('Y2CCJIM4PDJ2CDBN4TRO2DHGGSHR7PZ2')

    print(f'Rahul: {otp.now()}')
    print('\n')
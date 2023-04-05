import pyotp
# otp=pyotp.TOTP('TK6OW7YZDDSIB6G4EM66YXI3BLO7PVAR')
def totp1():
    otp=pyotp.TOTP('XVKUWP42GTBMHUXT5AUD2XQO4V6QK3TO')

    print(f'Rajesh: {otp.now()}')
    print('\n')
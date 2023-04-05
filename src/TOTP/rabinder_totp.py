import pyotp

def totp1():
    otp=pyotp.TOTP('TK6OW7YZDDSIB6G4EM66YXI3BLO7PVAR')
    # otp=pyotp.TOTP('XVKUWP42GTBMHUXT5AUD2XQO4V6QK3TO')

    print(f'Rabinder: {otp.now()}')
    print('\n')
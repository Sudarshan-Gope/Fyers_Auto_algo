import pyotp
# otp=pyotp.TOTP('TK6OW7YZDDSIB6G4EM66YXI3BLO7PVAR')
def totp1():
    otp=pyotp.TOTP('OSUM2NI47B4DK25XHKEIG664NB3EJCAU')

    print(f'Ramji: {otp.now()}')
    print('\n')
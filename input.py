def open_door():
    # run servo
    return

def key_in():
    y=0
    #input from keypad
    return y

def pass_verify(x):
        otp_inp = key_in()
        if otp_inp== x:
            open_door()
            return 1
        else:
            return 0


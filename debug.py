DEBUG = True

def abort(e):
    if DEBUG:
        print(e)
    else:
        print('*****program aborted*****')
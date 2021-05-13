DEBUG = False

def abort(e):
    """
    abort(e, /)

    Output an error message
    """
    if DEBUG:
        print(e)
    else:
        print('*****program aborted*****')

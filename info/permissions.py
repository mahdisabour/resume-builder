from rest_framework import permissions




def isAuthorize(request):
    # this is for test
    token = '1531199489:AAEzccmXBb778Aliqgec9SWS3CgSljAmyV8'
    # you should write validate token here later
    if (request.headers.get('Token') == token):
        return True

    else:
        return False


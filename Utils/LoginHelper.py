


def sendOTP(to, otp):
    # conn = httplib.HTTPConnection("api.msg91.com")
    conn = http.client.HTTPConnection("api.msg91.com")
    msg = 'Hello There, Your OTP at Faces.AI is '+ str(otp)
    conn.request("GET", "/api/sendhttp.php?route=4&sender=FACEAI&mobiles="+str(to)+"&authkey=275140AFIXXNPrKm5ccd4027&encrypt=&message="+msg+"&country=91")
    res = conn.getresponse()
    data = res.read()
    return data.decode("utf-8")
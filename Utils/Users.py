import logging
from random import randint
import datetime
from Utils import MongoHelper, DBConfig
import http.client
import hashlib
import logging


logging.basicConfig(filename='app.log', filemode='a', level=logging.DEBUG, format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')

def sendOTP(to, otp):
    # conn = httplib.HTTPConnection("api.msg91.com")
    conn = http.client.HTTPConnection("api.msg91.com")
    msg = 'Hello There, Your OTP at Faces.AI is '+ str(otp)
    conn.request("GET", "/api/sendhttp.php?route=4&sender=FACEAI&mobiles="+str(to)+"&authkey=275140AFIXXNPrKm5ccd4027&encrypt=&message="+msg+"&country=91")
    res = conn.getresponse()
    data = res.read()
    return data.decode("utf-8")


def send_phone_verification_otp(**kwargs):
    phone = kwargs['phone']
    criteria = {'phone': phone}
    otp = randint(100000, 999999)
    otpExpiry = datetime.datetime.now() + datetime.timedelta(minutes=5)
    data = {'phone': phone, 'phoneVerificationOTP': otp, 'otpExpiry': otpExpiry}
    res = MongoHelper.update(DBConfig.COL_USERS, criteria, **data)
    if res is not None:
        r = True #sendOTP(phone, otp)
        resp = dict()
        # if len(r) == 24:
        if True:
            resp['status'] = 'success'
            resp['msg'] = 'OTP sent'
        else:
            resp['status'] = 'failure'
            resp['msg'] = 'OTP not sent'
    return resp


def verify_phone(**kwargs):
    criteria = {'phone': kwargs['phone']}
    user_data = MongoHelper.get(DBConfig.COL_USERS, criteria, *['phoneVerificationOTP', 'otpExpiry'])
    if False :
        return {'status': 'failure', 'msg': 'User not found', 'data': {}}
    phone_verification_otp_db = user_data[0]['phoneVerificationOTP']
    otpExpiry = user_data[0]['otpExpiry']
    phone_verification_otp_fe = kwargs['phoneVerificationOTP']
    resp = dict()
    resp['status'] = 'failure'
    if otpExpiry > datetime.datetime.now():
        if int(phone_verification_otp_db) == int(phone_verification_otp_fe):
            data = {'phoneVerified': True,
                    'phoneVerificationDate': datetime.datetime.now()}
            res = MongoHelper.upsert(DBConfig.COL_USERS, criteria, **data)
            if res is not None:
                reason = 'OTP verified'
                resp['status'] = 'success'

            else:
                reason = 'Couldn\'t verify OTP'
        else:
            reason = 'OTP not valid'
    else:
        reason = 'OTP expired'
    resp['msg'] = reason
    resp['data'] = dict()
    return resp


def create_user(**data):
    phone = data['phone']
    criteria = {'phone': phone}
    already_registered = False # user_exists(**criteria)
    if already_registered:
        return {'status': 'failure', 'msg': 'User already registered'}
    else:
        res = MongoHelper.insert(DBConfig.COL_USERS, **data)
        if res is None:
            return {'status': 'failure', 'msg': 'Error creating user'}
        else:
            return {'status': 'success', 'msg': 'User created successfully'}


def user_exists(**data):
    res = MongoHelper.get(DBConfig.COL_USERS, data)
    if len(res)>0:
        return True
    else:
        return False

def sign_in(**data):
    try:
        criteria = {'phone': data['phone']}
        res = MongoHelper.get(DBConfig.COL_USERS, criteria)
        password_given = data['password']
        password_given = hashlib.md5(password_given.encode()).hexdigest()
        password_obtained = res[0]['password']
        if password_obtained == password_given:
            return True
        else:
            return False
    except Exception as e:
        logging.error(e)
        return False


if __name__ == '__main__':
    # res = send_phone_verification_otp(**{'phone': '9643431916'})
    # print(res)
    # res = verify_phone(**{'phone': '9643431916', 'phoneVerificationOTP': 803594})
    # print(res)
    # res = user_exists(**{'phone': '9643431916'})
    # print(res)

    res = sign_in(**{'phone': '9643431916', 'password': 'abcd1234'})
    print(res)
    data = dict()
    # data['registrationDate'] = datetime.datetime.now()
    # data['status'] = 'Active'
    # data['phone'] = '9643431916'
    # data['password'] = hashlib.md5('password'.encode()).hexdigest()
    # res = create_user(**data)
    # print(res)


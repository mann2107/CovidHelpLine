from flask import Flask, render_template, request, session
from flask import jsonify
from flask_session import Session
import datetime
from Utils import Users
import model
import logging
import hashlib


logging.basicConfig(filename='app.log', filemode='a', level=logging.DEBUG, format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')

app = Flask(__name__)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)


@app.route("/", methods=['GET'])
def home():
    return render_template("index.html")


@app.route("/account", methods=['GET'])
def account():
    return render_template("account.html")

#
# @app.route("/login", methods=['GET'])
# def login():
#     return render_template("login.html")


@app.route("/listglobalrequirements", methods=['GET'])
def list_global_requirements():
    data = model.list_requirements()
    return jsonify(data)



@app.route("/listuserhelps", methods=['GET'])
def list_user_helps():
    data = model.list_user_helps()
    return jsonify(data)



@app.route("/listpatientrequirements", methods=['GET'])
def list_patient_requirements():
    data = model.list_patient_requirements()
    return jsonify(data)


# @app.route("/listrequirements", methods=['GET'])
# def list_requirements():
#     data = model.list_requirements()
#     return render_template("listrequirements.html", data=data)


@app.route("/create_account", methods=['GET'])
def create_account():
    data = request.form
    res = model.create_requirement(**data)
    if res:
        return "success"
    else:
        return "failure"
    return render_template("account.html")


@app.route("/create_requirement", methods=['POST'])
def create_requirement():
    
    data = request.form
    print(data)
    res = model.create_requirement(**data)
    if res:
        return jsonify({'status': 'success', 'msg': 'requirement created', 'data': {}})
    else:
        return jsonify({'status': 'failure', 'msg': 'failed', 'data': {}})


'''##############################Login and Sign up####################################################################'''


@app.route("/sign_up", methods=['POST'])
def sign_up():
    password = request.form['password']
    phone = request.form['mobile']
    try:
        data = dict()
        data['registrationDate'] = datetime.datetime.now()
        data['status'] = 'Active'
        data['phone'] = phone
        data['password'] = hashlib.md5(password.encode()).hexdigest()
        res = Users.create_user(**data)
        if res['status'] == 'success':
            logging.info('New user registered with phone ' + phone)
            resp = Users.send_phone_verification_otp(**{'phone': phone})
            return jsonify(resp)
        else:
            logging.error('Error registering user with phone ' + phone)
            return jsonify(res)
    except Exception as e:
        logging.error('Error registering user with phone ' + phone)
        return jsonify({'status': 'failure', 'msg': 'Some Error'})


'''
Sends phone verification otp
criteria: email, phone
returns: {'status': 'success/failure', 'data': data, 'reason': reason }
'''


@app.route("/get_phone_otp", methods=['POST'])
def get_phone_otp():
    try:
        data = dict()

        data['phone'] = int(request.form['phone'])
        res = Users.send_phone_verification_otp(data)
        return jsonify(res)
    except Exception as e:
        return jsonify({'status': 'failure', 'msg': str(e), 'data': {}})


'''
Verifies phone verification otp
criteria: email, phone
returns: {'status': 'success/failure', 'data': data, 'reason': reason }
'''


@app.route("/verify_phone_otp", methods=['POST'])
def verify_phone_otp():
    try:
        data = dict()
        data['phoneVerificationOTP'] = request.form['otp']
        data['phone'] = str(request.form['mobile'])

        d = Users.verify_phone(**data)
        return jsonify(d)
    except Exception as e:
        print(e)
        return jsonify({'status': 'failure', 'msg': str(e), 'data': {}})


@app.route("/sign_in", methods=['POST'])
def sign_in():
    data = dict()
    data['password'] = request.form['password']
    data['phone'] = request.form['mobile']
    res = Users.sign_in(**data)

    if res:
        session['user'] = data['phone']
        return jsonify({'status': 'success', 'data': dict(session)})
    else:
        return jsonify({'status': 'failure', 'msg': 'Login Failed'})


'''#############################################General APIs######################################'''
@app.route('/login')
def login():
    return render_template("login.html")


@app.route('/volunteer')
def volunteer():
    return render_template("volunteer.html")


@app.route('/volunteer-profile')
def volunteerprofile():
    return render_template("volunteer-profile.html")


@app.route('/requirement-profile')
def requirementprofile():
    return render_template("patient-profile.html")


@app.route('/requirement')
def requirement():
    return render_template("patient.html")


@app.route('/requirement-form')
def requirementform():
    return render_template("requirement-form.html")


if __name__ == "__main__":
    app.run(debug=True)
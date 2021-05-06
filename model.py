from Utils import Requirement, Volunteer, Patient


def create_requirement(**req):
    res = Requirement.create_requirement(**req)
    return res


def create_account(**req):
    actor = req['actor']
    res = False
    del req['actor']
    if actor == 'Volunteer':
        res = Volunteer.create_volunteer(**req)
    elif actor == 'Patient':
        res = Patient.create_patient(**req)
    return res


def list_requirements():
    return Requirement.list_requirements()
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
    # return Requirement.list_requirements()
    return [{'requirement_summary': 'Oxygen, 2', 'location': 'Jamalpur, India', 'patient_id': 'fiWNAEhM3qdVBMns8vTn5u', 'req_posted_at': '', 'status': 'Open', 'picked_by': 0, 'requirement_id': 'WxDHNUdF9y2hyUBLeSJadT', 'posted': '24.54 minutes ago', 'pick': ''}, {'requirement_summary': 'Covid Bed, 2', 'location': 'Jamalpur, India', 'patient_id': 'fiWNAEhM3qdVBMns8vTn5u', 'req_posted_at': '', 'status': 'Open', 'picked_by': 0, 'requirement_id': 'gogmLn7CPEj2s3LH9J4G4o', 'posted': '24.54 minutes ago', 'pick': ''}]


def list_user_helps():
    # return Requirement.list_requirements()
    return [{'requirement_summary': 'Oxygen, 4', 'location': 'Jamalpur, India', 'patient_id': 'fiWNAEhM3qdVBMns8vTn5u', 'posted': '24.54 minutes ago', 'volunteers': ['m83', 'vat69']},
            {'requirement_summary': 'Covid Bed, 6', 'location': 'Jamalpur, India', 'patient_id': 'fiWNAEhM3qdVBMns8vTn5u', 'posted': '24.54 minutes ago', 'volunteers': ['j007', '123']}]


def list_patient_requirements():
    # return Requirement.list_requirements()
    return [{'requirement_summary': 'Oxygen, 4', 'location': 'Jamalpur, India', 'patient_id': 'fiWNAEhM3qdVBMns8vTn5u', 'posted': '24.54 minutes ago', 'volunteers': ['m83', 'vat69']},
            {'requirement_summary': 'Covid Bed, 6', 'location': 'Jamalpur, India', 'patient_id': 'fiWNAEhM3qdVBMns8vTn5u', 'posted': '24.54 minutes ago', 'volunteers': ['j007', '123']}]
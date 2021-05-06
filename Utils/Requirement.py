import datetime
import shortuuid
from Utils import MongoHelper, DBConfig, Patient


def generate_requirement(**data):
    res = MongoHelper.insert(DBConfig.COL_REQUIREMENT, **data)
    if res is None:
        return False
    else:
        return True


def close_requirement(**data):
    res = MongoHelper.insert(DBConfig.COL_REQUIREMENT, **data)
    if res is None:
        return False
    else:
        return True


def build_requirement(**req):
    patient_id = shortuuid.uuid()
    patient_details = dict()
    patient_details['patient_id'] = patient_id
    requirements = []
    state = req['state']
    city = req['city']

    for k, v in req.items():
        if k.startswith('requirementType'):
            req_dict = dict()
            req_num = k[15:]
            quantity_key = 'Quantity' + req_num
            #
            # req_dict['requirement'] = req[k]
            # req_dict['quantity'] = req.get(quantity_key, None)

            req_dict['requirement_summary'] = req[k] + ', ' + req.get(quantity_key, '')

            req_dict['location'] = city + ', ' + state

            req_dict['patient_id'] = patient_id
            req_dict['req_posted_at'] = datetime.datetime.now()
            req_dict['status'] = 'Open'
            req_dict['picked_by'] = 0
            req_dict['requirement_id'] = shortuuid.uuid()
            requirements.append(req_dict)
        else:
            if not k.startswith('Quantity'):
                patient_details[k] = v
    return patient_details, requirements


def create_requirement(**req):
    # req = {'name': 'Manish Kumar', 'phone': '09643431916', 'age': '36', 'state': 'India', 'city': 'Jamalpur',
    #        'location': 'Near Hospital', 'requirementType1': 'Oxygen', 'Quantity1': '1', 'requirementType2': 'Covid Bed',
    #        'Quantity2': '2'}

    patient_details, requirements = build_requirement(**req)
    patient_created = Patient.create_patient(**patient_details)
    if patient_created:
        for r in requirements:
            generate_requirement(**r)
        return True
    else:
        return False


def list_global_requirements():
    res = MongoHelper.get(DBConfig.COL_REQUIREMENT, {'status': 'Open'})
    data = []
    for r in res:
        del r['_id']
        req_posted_at = r['req_posted_at']
        now = datetime.datetime.now()
        c = now - req_posted_at
        minutes = str(round(c.total_seconds() / 60, 2)) + ' minutes ago'
        r['posted'] = minutes
        r['pick'] = 'https:\\/\\/localhost:5005/pick?req_id='+r['requirement_id']
        data.append(r)
    return data


def list_requirements_patient_view():
    res = MongoHelper.get(DBConfig.COL_REQUIREMENT, {'status': 'Open'})
    data = []
    for r in res:
        req_posted_at = r['req_posted_at']
        now = datetime.datetime.now()
        c = now - req_posted_at
        minutes = str(round(c.total_seconds() / 60, 2)) + ' minutes ago'
        r['posted'] = minutes
        r['pick'] = 'https://localhost:5005/pick?req_id='+r['requirement_id']
        del r['_id']
        del r['status']
        del r['picked_by']
        del r['requirement_id']
        del r['req_posted_at']
        data.append(r)
    return data


def list_requirements_volunteer_view():
    res = MongoHelper.get(DBConfig.COL_REQUIREMENT, {'status': 'Open'})
    data = []
    for r in res:
        req_posted_at = r['req_posted_at']
        now = datetime.datetime.now()
        c = now - req_posted_at
        minutes = str(round(c.total_seconds() / 60, 2)) + ' minutes ago'
        r['posted'] = minutes
        r['pick'] = 'https://localhost:5005/pick?req_id='+r['requirement_id']
        del r['_id']
        del r['status']
        del r['picked_by']
        del r['requirement_id']
        del r['req_posted_at']
        data.append(r)
    return data


if __name__ == '__main__':
    data = list_requirements()
    print(data)
from Utils import MongoHelper, DBConfig


def create_patient(**data):
    res = MongoHelper.insert(DBConfig.COL_PATIENT, **data)
    if res is None:
        return False
    else:
        return True


if __name__ == '__main__':
    data = {'name': 'Test',
            'id_type': 'VoterID',
            'phone': 1234567890,
            'location': 'Near ABC Hospital',
            'id_no': 'abc128',
            'age': 65,
            'state': 'Bihar',
            'city': 'Patna'}
    patient_created = create_patient(**data)
    print(patient_created)

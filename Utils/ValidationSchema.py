patient = {'name': {'type': 'string', 'required': True},
           'id_type': {'type': 'string', 'required': False},
           'phone': {'type': 'number', 'required': True},
           'location': {'type': 'string', 'required': False},
           'id_no': {'type': 'string', 'required': False},
           'age': {'type': 'number', 'required': True},
           'state': {'type': 'string', 'required': True},
           'city': {'type': 'string', 'required': True}}

requirement = {'patient_id': {'type': 'string', 'required': True},
               'item': {'type': 'number', 'required': True},
               'quantity_units': {'type': 'string', 'required': True},
               'status': {'type': 'string', 'required': True},
               'volunteer_id': {'type': 'Array', 'required': True},
               'time_of_posting': {'type': 'string', 'required': True},
               'closing_time': {'type': '', 'required': True},
               'closing_volunteer_id': {'type': 'string', 'required': True}}

voulunteer = {'name': {'type': 'string', 'required': True},
              'id_type': {'type': 'string', 'required': False},
              'phone': {'type': 'number', 'required': True},
              'location': {'type': 'string', 'required': False},
              'id_no': {'type': 'string', 'required': False},
              'age': {'type': 'number', 'required': True},
              'state': {'type': 'string', 'required': True},
              'city': {'type': 'string', 'required': True}}

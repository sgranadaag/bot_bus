class Record():
    user_id = None
    user_type = None
    review = {
        'description': None,
        'vehicle_id': None,
        'spare_parts': None,
    }

    vehicle = {
        'id' : None,
        'model': None,
        'mark': None,
        'id_owner': None,
    }

    def set_user_data(self, user_id, user_type):
        self.user_id = user_id
        self.user_type = user_type

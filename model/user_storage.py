from model.user import User


class UserStorage:

    def __init__(self, data):
        if not data:
            self.d = User({})
        elif isinstance(data, dict):
            self.d = User(data)
        else:
            self.d = [User(u) for u in data]


    def get_json_obj(self):
        if isinstance(self.d, User):
            return self.d.to_dict()
        return [u.to_dict() for u in self.d]
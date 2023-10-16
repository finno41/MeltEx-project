class BaseDTO:
    def __init__(self, data, user):
        if not isinstance(data, dict):
            data = data.__dict__
        self.data = data

    def output(self):
        return self.data


class BaseDTOCollection:
    def __init__(self, data_collection, user, base_dto=BaseDTO):
        if not isinstance(data_collection, list):
            data_collection = list(data_collection.values())
        self.data_collection = [
            base_dto(
                data,
                user,
            ).output()
            for data in data_collection
        ]

    def output(self):
        return self.data_collection

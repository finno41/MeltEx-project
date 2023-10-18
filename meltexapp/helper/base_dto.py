class BaseDTO:
    def __init__(self, data, user, hide_keys=[], **kwargs):
        if not isinstance(data, dict):
            data = data.__dict__
        data = data | self.__dict__
        self.data = {k: v for k, v in data.items() if k not in hide_keys}

    def output(self):
        return self.data


class BaseDTOCollection:
    def __init__(self, data_collection, user, base_dto=BaseDTO, **kwargs):
        if not isinstance(data_collection, list):
            data_collection = list(data_collection.values())
        self.data_collection = [
            base_dto(
                data,
                user,
                **kwargs,
            ).output()
            for data in data_collection
        ]

    def output(self):
        return self.data_collection

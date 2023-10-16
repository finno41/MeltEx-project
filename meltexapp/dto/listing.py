from meltexapp.helper.base_dto import BaseDTOCollection, BaseDTO


class ListingDTO(BaseDTO):
    def __init__(self, data, user):
        super().__init__(data, user)


class ListingDTOCollection(BaseDTOCollection):
    def __init__(self, data, user):
        super().__init__(data, user)

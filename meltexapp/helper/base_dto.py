import pandas as pd
from django.db.models.query import QuerySet

UNIVERSAL_HIDE_KEYS = ["linked_model_df"]


class BaseDTO:
    def __init__(self, data, user, dto_collection=None, hide_keys=[], **kwargs):
        hide_keys += UNIVERSAL_HIDE_KEYS
        if not isinstance(data, dict):
            data = data.__dict__
        if dto_collection and hasattr(dto_collection, "linked_model_df"):
            for model, link_data in dto_collection.linked_model_df.items():
                linked_model_lookup = link_data["df"].loc[
                    [data[link_data["lookup_key"]]]
                ]
                linked_model_attributes = linked_model_lookup.to_dict("records")[0]
                setattr(self, f"{model}_data", linked_model_attributes)
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
                dto_collection=self,
                **kwargs,
            ).output()
            for data in data_collection
        ]

    def link_model(
        self,
        linked_model_name: str,
        user,
        foreign_key: str,
        model_primary_key: str,
        model_queryset: QuerySet,
        queryset_display_values: list,
    ):
        """
        This function links a model joined by a primary key to the DTO output which can be accessed
        in the return dictionary by using the key f"{linked_model_name}_data".
        foreign_key: the name of the key that connects to the model you wish to link
        model_primary_key: the primary key of that model you wish to link
        model_queryset: the queryset containing the model instances you wish to link
        queryset_display_values: the values you wish to return from the linked model
        """
        queryset_display_values.append(model_primary_key)
        linked_model_data = list(model_queryset.values(*queryset_display_values))
        linked_model_df = pd.DataFrame(linked_model_data)
        linked_model_df.set_index(model_primary_key, inplace=True)
        linked_model_data = {"df": linked_model_df, "lookup_key": foreign_key}
        if hasattr(self, "linked_model_df"):
            if linked_model_name in self.linked_model_df:
                # create exception which allows a dev only exception
                raise Exception(
                    "You cannot cal 'link_model()' more than once in a DTOCollection with the same linked_model_name"
                )
            self.linked_model_df[linked_model_name] = linked_model_data
        else:
            self.linked_model_df = {linked_model_name: linked_model_data}

    def output(self):
        return self.data_collection

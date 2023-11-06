import typing
from datetime import datetime
from dateutil import parser
from enum import Enum


class EfecteBaseModel:

    template_code: str = ""
    "Efecte Tepmlate Code for Subclasses"

    dataCardId: str = None
    "Efecte DatacardId"

    deleted: bool = False
    "Is item deleted"

    hidden: bool = False
    "Item is hidden"

    def __init__(self, data=None):
        # Local Module imports
        from .company import (EfecteCompany, EfecteCompanyTypeEnum, EfecteCompanyStatusEnum,
                              EfecteOrganizationInternalExternalEnum, EfecteWebsite)
        if self.template_code != data['templateCode']:
            raise Exception("Expected templateCode [{}] got [{}] from Efecte".format(self.template_code, data['templateCode']))
        if data is None:
            return
        self.dataCardId = data['dataCardId']
        self.folderName = data['folderName']
        if 'data' in data:
            for key, element in data['data'].items():
                if hasattr(self, key):
                    attr_type = self.__annotations__[key]
                    element_type = element['type']
                    values = element['values']
                    if len(values) == 1:
                        if attr_type == str:
                            if element_type != 'string':
                                raise TypeError("Expected string and got {}".format(element_type))
                        if attr_type == datetime:
                            if element_type != 'date':
                                raise TypeError("Expected date and got {}".format(element_type))
                            setattr(self, key, parser.parse(values[0]['value']))
                        elif attr_type == EfecteCompanyStatusEnum:
                            if element_type != 'static-value':
                                raise TypeError("Expected static-value and got {}".format(element_type))
                            setattr(self, key, EfecteCompanyStatusEnum(values[0]['value']))
                        elif attr_type == EfecteCompanyTypeEnum:
                            if element_type != 'static-value':
                                raise TypeError("Expected static-value and got {}".format(element_type))
                            setattr(self, key, EfecteCompanyTypeEnum(values[0]['value']))
                        elif attr_type == EfecteOrganizationInternalExternalEnum:
                            if element_type != 'static-value':
                                raise TypeError("Expected static-value and got {}".format(element_type))
                            setattr(self, key, EfecteOrganizationInternalExternalEnum(values[0]['value']))
                        elif attr_type == [EfecteWebsite]:
                            setattr(self, key, EfecteWebsite(values[0]['location'], values[0]['name']))
                        else:
                            if 'value' in values[0]:
                                setattr(self, key, values[0]['value'])
                    else:
                        if type(getattr(self, key)).__name__ == 'list':
                            items = list()
                            for item in values:
                                if attr_type == [EfecteWebsite]:
                                    items.append(EfecteWebsite(item['location'], item['name']))
                                else:
                                    items.append(item['value'])
                            setattr(self, key, items)

    def get_efecte_json(self):
        from .company import EfecteWebsite
        result = dict()
        for key, value in self.__dict__.items():
            if value is None:
                continue
            if key in ['template_code', 'folderName', 'dataCardId', 'creator',
                       'last_update_by', 'created', 'updated', 'deleted', 'hidden']:
                continue
            attr_type = self.__annotations__[key]
            if attr_type is typing.List[EfecteWebsite]:
                pass
            elif attr_type is typing.List[str]:
                pass
            elif issubclass(attr_type, Enum) or attr_type in (str, int, datetime):
                result[key] = dict()
                result[key]['values'] = list()
                if issubclass(attr_type, Enum):
                    if type(value) is str:
                        result[key]['values'].append({'value': value})
                    else:
                        result[key]['values'].append({'value': value.name})
                elif attr_type == datetime:
                    result[key]['values'].append({'value': value.isoformat()})
                else:
                    result[key]['values'].append({'value': value})
            else:
                raise NotImplementedError("Serialization of {} not implemented".format(attr_type))
        return result

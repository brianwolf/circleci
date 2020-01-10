import base64
from datetime import datetime
from uuid import UUID, uuid4
from pydantic import BaseModel, validator, BaseConfig
from pydantic.validators import dict_validator


import apps.configs.variables as var


class AppModel(BaseModel):

    @classmethod
    def get_validators(cls):
        yield cls.validate

    @classmethod
    def validate(cls, value):
        if isinstance(value, cls):
            return value
        else:
            return cls(**dict_validator(value))


class Modelo(AppModel):
    def __init__(self,
                 nombre: str,
                 archivos: list = [],
                 id: UUID = uuid4(),
                 fecha_creacion: datetime = datetime.now()):
        self.nombre = nombre
        self.archivos = archivos
        self.id = id
        self.fecha_creacion = fecha_creacion

    def to_dict(self):
        return {
            'nombre': self.nombre,
            'archivos': [archivo.to_dict() for archivo in self.archivos],
            'id': str(self.id),
            'fecha_creacion': str(self.fecha_creacion)
        }

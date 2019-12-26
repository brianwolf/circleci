import base64
from datetime import datetime
from uuid import UUID, uuid4

from mongoengine import (DateTimeField, Document, EmbeddedDocument,
                         EmbeddedDocumentField, EmbeddedDocumentListField,
                         ListField, StringField)

import app.configs.variables as var

#######################################################
# NEGOCIO
#######################################################

RAMA_MODELOS = var.get('RAMA_MODELOS')


class Modelo(object):
    def __init__(self,
                 nombre,
                 archivos: list = [],
                 id: UUID = uuid4(),
                 fecha_creacion=datetime.now()):
        self.nombre = nombre
        self.archivos = archivos
        self.id = id
        self.fecha_creacion = fecha_creacion

    @staticmethod
    def from_dict(d: dict):
        instancia = Modelo()
        instancia.__dict__.update(**d)
        return instancia

    def to_dict(self):
        return {
            'nombre': self.nombre,
            'archivos': [archivo.to_dict() for archivo in self.archivos],
            'id': str(self.id),
            'fecha_creacion': str(self.fecha_creacion)
        }

    def contenido_html(self, nombre: str = '') -> bytes:
        if nombre:
            if '.html' not in nombre:
                nombre += '.html'

            return [a.contenido for a in self.archivos
                    if a.nombre == nombre][0]

        for archivo in self.archivos:
            if '.html' in archivo.nombre:
                return archivo.contenido


class Archivo(object):
    def __init__(self,
                 rama: str,
                 nombre: str,
                 contenido: bytes,
                 fecha_creacion: datetime = datetime.now()):
        self.rama = rama
        self.nombre = nombre
        self.contenido = contenido
        self.fecha_creacion = fecha_creacion

    @staticmethod
    def from_dict(a: dict):
        instancia = Archivo(None, None)
        instancia.__dict__.update(**a)
        return instancia

    def to_dict(self):
        resultado = {
            'rama': self.rama,
            'nombre': self.nombre,
            'fecha_creacion': str(self.fecha_creacion)
        }

        if self.contenido:
            contenido_base64 = base64.b64encode(self.contenido)
            resultado['contenido'] = str(contenido_base64, 'utf-8')

        return resultado


#######################################################
# MONGO
#######################################################


class ArchivoDocument(EmbeddedDocument):
    meta = {'indexes': [{'fields': ['-nombre'], 'unique': True}]}

    rama = StringField(required=True, max_length=128)
    nombre = StringField(required=True, max_length=128)
    fecha_creacion = DateTimeField(default=datetime.now())

    @staticmethod
    def from_dict(d: dict):
        return ArchivoDocument(rama=d['rama'],
                               nombre=d['nombre'],
                               fecha_creacion=d['fecha_creacion'])

    @staticmethod
    def desde_archivo(a: Archivo):
        return ArchivoDocument(rama=a.rama,
                               nombre=a.nombre,
                               fecha_creacion=a.fecha_creacion)

    def to_dict(self):
        return {
            'rama': self.rama,
            'nombre': self.nombre,
            'fecha_creacion': self.fecha_creacion
        }


class ModeloDocument(Document):
    meta = {'indexes': [{'fields': ['-nombre'], 'unique': True}]}

    nombre = StringField(required=True, max_length=128)
    archivos = ListField(EmbeddedDocumentField(ArchivoDocument))
    fecha_creacion = DateTimeField(default=datetime.now)

    @staticmethod
    def from_dict(d: dict):
        return ModeloDocument(nombre=d['nombre'],
                              archivos=[
                                  ArchivoDocument.desde_diccionario(archivo)
                                  for archivo in d['archivos']
                              ],
                              fecha_creacion=d['fecha_creacion'])

    @staticmethod
    def por_modelo(modelo: Modelo):
        return ModeloDocument(nombre=modelo.nombre,
                              archivos=[
                                  ArchivoDocument.desde_archivo(archivo)
                                  for archivo in modelo.archivos
                              ],
                              fecha_creacion=modelo.fecha_creacion)

    def to_dict(self):
        return {
            'nombre': self.nombre,
            'archivos': [archivo.to_dict() for archivo in self.archivos],
            'id': self.id,
            'fecha_creacion': str(self.fecha_creacion)
        }

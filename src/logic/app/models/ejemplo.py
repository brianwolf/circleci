from dataclasses import dataclass
from datetime import datetime
from typing import List
from uuid import UUID, uuid4


@dataclass
class Modelo:
    numero: int
    texto: str
    uuid: UUID = None
    fecha: datetime = datetime.now()

    def to_dict(self):
        return {
            'numero': self.numero,
            'texto': self.texto,
            'uuid': str(self.uuid),
            'fecha': str(self.fecha)
        }

    @staticmethod
    def from_dict(d: dict) -> 'Modelo':
        instancia = Modelo(d['numero'], d['texto'])
        instancia.fecha = d.get('fecha', instancia.fecha)
        instancia.uuid = UUID(d['uuid']) if 'uuid' in d else instancia.uuid
        return instancia

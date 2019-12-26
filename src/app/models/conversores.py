from typing import Dict
from app.utils.wkhtml_to_pdf import Wkhtml_to_pdf


class Conversor():
    def __init__(self, datos: Dict):
        self.datos = datos


class HtmlToPdf(Conversor):
    def __init__(self, config: Wkhtml_to_pdf, datos: Dict):
        super().__init__(datos)
        self.config = config
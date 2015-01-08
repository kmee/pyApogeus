# -*- coding: utf-8 -*-


class PrazoPauta ():

    _template = (
            "{0.codigo_filial:0>1}"
            "{0.coluna_preco_pauta:0>2}"
            "{0.descritivo_coluna_precos: <15}"
            "{0.codigo_pauta_precos: <4}"
            "{0.reservado1: <50}"
        )

    def __init__(self, codigo_filial, coluna_preco_pauta,
        descritivo_coluna_precos, codigo_pauta_precos, reservado1=''):

        self.codigo_filial = codigo_filial
        self.coluna_preco_pauta = coluna_preco_pauta
        self.descritivo_coluna_precos = descritivo_coluna_precos
        self.codigo_pauta_precos = str(codigo_pauta_precos)[:4]
        self.reservado1 = reservado1

    @property
    def get_line(self):
        return(self._template.format(self))
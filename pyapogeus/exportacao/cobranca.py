# -*- coding: utf-8 -*-

class Cobranca():

    _template = (
        "{0.codigo_tipo_cobranca:0>3}"
        "{0.descricao_cobranca: <15}"
        "{0.codigo_filial:0>1}"
        "{0.valor_minimo_parcela:0>12}"
        "{0.codigo_pauta_precos: <4}"
        "{0.coluna_precos_pauta:0>2}"
        "{0.cobranca_cliente_novo: <1}"
        "{0.reservado1: <43}"
        )


    def __init__(self,codigo_tipo_cobranca, descricao_cobranca ,
        codigo_pauta_precos, coluna_precos_pauta, codigo_filial,
        valor_minimo_parcela='', cobranca_cliente_novo='', reservado1=''):

        self.codigo_tipo_cobranca = codigo_tipo_cobranca
        self.descricao_cobranca = descricao_cobranca[:15]
        self.codigo_filial = codigo_filial
        self.valor_minimo_parcela = valor_minimo_parcela
        self.codigo_pauta_precos = codigo_pauta_precos[:4]
        self.coluna_precos_pauta = coluna_precos_pauta
        self.cobranca_cliente_novo = cobranca_cliente_novo[:1]
        self.reservado1 = reservado1[:43]

    @property
    def get_line(self):
        return(self._template.format(self))
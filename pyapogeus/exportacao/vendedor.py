## -*- coding: utf-8 -*-

class Vendedor():

    _template = (
        "{0.codigo_filial:0>1}"
        "{0.codigo_vendedor:0>3}"
        "{0.nome_vendedor: <20}"
        "{0.meta:0>12}"
        "{0.valor_atual_faturado:0>12}"
        "{0.data_meta:0>8}"
        "{0.tipo_rota: <1}"
        "{0.saldo_flex:0>12}"
        "{0.sinal_do_flex: <1}"
        "{0.senha_ftp: <10}"
        "{0.transmite_flex_negativo: <1}"
        "{0.reservado1: <50}"
        )

    def __init__(self, codigo_filial, codigo_vendedor, nome_vendedor,
    transmite_flex_negativo, meta='', valor_atual_faturado='', data_meta='',
    tipo_rota='', saldo_flex='', sinal_do_flex='', senha_ftp='', reservado1=''):

        self.codigo_filial = codigo_filial
        self.codigo_vendedor = codigo_vendedor
        self.nome_vendedor = nome_vendedor[:20]
        self.meta = meta
        self.valor_atual_faturado = valor_atual_faturado
        self.data_meta = data_meta
        self.tipo_rota = tipo_rota[:1]
        self.saldo_flex = saldo_flex
        self.sinal_do_flex = sinal_do_flex[:1]
        self.senha_ftp = senha_ftp[:10]
        self.transmite_flex_negativo = transmite_flex_negativo[:1]
        self.reservado1 = reservado1[:50]

    @property
    def get_line(self):
        return(self._template.format(self))
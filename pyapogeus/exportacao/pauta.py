# -*- coding: utf-8 -*-


class Pauta():

    _template = (
        "{0.codigo_filial:0>1}"
        "{0.codigo_vendedor:0>3}"
        "{0.codigo_pauta_precos: <4}"
        "{0.descricao_pauta: <15}"
        "{0.data_inicial:0>8}"
        "{0.data_final:0>8}"
        "{0.controla_flex: <1}"
        "{0.acumulador_limitador_flex_negativo: <1}"
        "{0.acumulador_limitador_flex_positivo: <1}"
        "{0.permitir_flex_negativo: <1}"
        "{0.adiciona_desconto_saldo_flex: <1}"
        "{0.subtrai_desconto_saldo_flex: <1}"
        "{0.reservado1: <50}"
        )

    def __init__(self,codigo_filial, codigo_vendedor,codigo_pauta_precos,
        descricao_pauta, data_inicial, data_final, controla_flex,
        acumulador_limitador_flex_negativo, acumulador_limitador_flex_positivo,
        permitir_flex_negativo,adiciona_desconto_saldo_flex,
        subtrai_desconto_saldo_flex,reservado1=''):

        self.codigo_filial = codigo_filial
        self.codigo_vendedor = codigo_vendedor
        self.codigo_pauta_precos = str(codigo_pauta_precos)[:4]
        self.descricao_pauta = descricao_pauta[:15]
        self.data_inicial = data_inicial
        self.data_final = data_final
        self.controla_flex = controla_flex[:1]
        self.acumulador_limitador_flex_negativo = acumulador_limitador_flex_negativo[:1]
        self.acumulador_limitador_flex_positivo = acumulador_limitador_flex_positivo[:1]
        self.permitir_flex_negativo = permitir_flex_negativo[:1]
        self.adiciona_desconto_saldo_flex = adiciona_desconto_saldo_flex[:1]
        self.subtrai_desconto_saldo_flex = subtrai_desconto_saldo_flex[:1]
        self.reservado1 = reservado1[:50]

    @property
    def get_line(self):
        return(self._template.format(self))
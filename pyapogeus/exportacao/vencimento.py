    # -*- coding: utf-8 -*-

class Vencimento():

    _template = (
        "{0.codigo_filial:0>1}"
        "{0.codigo_pauta_precos: <4}"
        "{0.codigo_vencimento:0>4}"
        "{0.coluna_precos_pauta:0>2}"
        "{0.desconto_maximo:0>5}"
        "{0.descricao_vencimento: <15}"
        "{0.codigo_cobranca:0>3}"
        "{0.nomero_parcelas:0>2}"
        "{0.perc_desconto_financeiro:0>5}"
        "{0.perc_acrescimo_financeiro:0>5}"
        "{0.fator_ajuste_preco:0>7}"
        "{0.media_dias:0>3}"
        "{0.perc_custo_venda:0>6}"
        "{0.valor_minimo_pedido:0>12}"
        "{0.reservado1:0>7}"
    )

    def __init__(self, codigo_filial, codigo_pauta_precos, codigo_vencimento,
        coluna_precos_pauta, descricao_vencimento, codigo_cobranca,
        nomero_parcelas, desconto_maximo='',perc_desconto_financeiro='',
        perc_acrescimo_financeiro='',fator_ajuste_preco='',media_dias='',
        perc_custo_venda='',valor_minimo_pedido='', reservado1=''):

        self.codigo_filial = codigo_filial
        self.codigo_pauta_precos = codigo_pauta_precos[:4]
        self.codigo_vencimento = codigo_vencimento
        self.coluna_precos_pauta = coluna_precos_pauta
        self.desconto_maximo = desconto_maximo
        self.descricao_vencimento = descricao_vencimento[:15]
        self.codigo_cobranca = codigo_cobranca
        self.nomero_parcelas = nomero_parcelas
        self.perc_desconto_financeiro = perc_desconto_financeiro
        self.perc_acrescimo_financeiro = perc_acrescimo_financeiro
        self.fator_ajuste_preco = fator_ajuste_preco
        self.media_dias = media_dias
        self.perc_custo_venda = perc_custo_venda
        self.valor_minimo_pedido = valor_minimo_pedido
        self.reservado1 = reservado1

    @property
    def get_line(self):
        return(self._template.format(self))
# -*- coding: utf-8 -*-


        if StrRegZA['UFEmbarq'] !='' and StrRegZA['XLocEmbarq'] != '':
            StrZA = 'ZA|%s|%s|\n' % (StrRegZA['UFEmbarq'], StrRegZA['XLocEmbarq'])
            StrFile += StrZA



class Preco():

    _template = (
        "{0.codigo_produto: <16}"
        "{0.preco_venda1:0>9}"
        "{0.preco_venda2:0>9}"
        "{0.preco_venda3:0>9}"
        "{0.preco_venda4:0>9}"
        "{0.preco_venda5:0>9}"
        "{0.preco_venda6:0>9}"
        "{0.saldo_estoque:0>11}"
        "{0.codigo_pauta_precos: <4}"
        "{0.codigo_filial:0>1}"
        "{0.desconto_maximo:0>5}"
        "{0.acrescimo_maximo:0>5}"
        "{0.perc_positivo_flex:0>5}"
        "{0.perc_negativo_flex:0>5}"
        "{0.tipo_produto: <1}"
        "{0.alicota_st:0>5}"
        "{0.alicota_icms:0>5}"
        "{0.alicota_comsumidor:0>5}"
        "{0.valor_custo_st:0>9}"
        "{0.valor_unitario:0>9}"
        "{0.quantidade_maxima:0>9}"
        "{0.fator_ajuste_preco:0>7}"
        "{0.valor_unitario_reducao:0>9}"
        "{0.brinde: <1}"
        "{0.preco_custo:0>9}"
        "{0.perc_custo_venda:0>6}"
        "{0.perc_min_margem:0>7}"
        "{0.perc_max_margem:0>7}"
        "{0.quantidade_minima:0>9}"
        "{0.descontar_brinde: <1}"
        "{0.afeta_flex: <1}"
        "{0.alicota_ipi:0>5}"
        "{0.mostrar_margem: <1}"
        "{0.mostrar_markup: <1}"
        "{0.grupo_desconto:0>3}"
        "{0.reservado1: <39}"
        )

    def __init__(self, codigo_produto, preco_venda1, saldo_estoque,
        codigo_pauta_precos, codigo_filial, tipo_produto, preco_venda2='',
        preco_venda3='', preco_venda4='', preco_venda5='', preco_venda6='',
        desconto_maximo='', acrescimo_maximo='', perc_positivo_flex='',
        perc_negativo_flex='', alicota_st='', alicota_icms='',
        alicota_comsumidor='', valor_custo_st='', valor_unitario='',
        quantidade_maxima='', fator_ajuste_preco='', valor_unitario_reducao='',
        brinde='', preco_custo='', perc_custo_venda='', perc_min_margem='',
        perc_max_margem='', quantidade_minima='', descontar_brinde='',
        afeta_flex='', alicota_ipi='', mostrar_margem='', mostrar_markup='',
        grupo_desconto='', reservado1=''):

        self.codigo_produto = str(codigo_produto)[:16]
        self.preco_venda1 = preco_venda1
        self.preco_venda2 = preco_venda2
        self.preco_venda3 = preco_venda3
        self.preco_venda4 = preco_venda4
        self.preco_venda5 = preco_venda5
        self.preco_venda6 = preco_venda6
        self.saldo_estoque = saldo_estoque
        self.codigo_pauta_precos = str(codigo_pauta_precos)[:4]
        self.codigo_filial = codigo_filial
        self.desconto_maximo = desconto_maximo
        self.acrescimo_maximo = acrescimo_maximo
        self.perc_positivo_flex = perc_positivo_flex
        self.perc_negativo_flex = perc_negativo_flex
        self.tipo_produto = tipo_produto[:1]
        self.alicota_st = alicota_st
        self.alicota_icms = alicota_icms
        self.alicota_comsumidor = alicota_comsumidor
        self.valor_custo_st = valor_custo_st
        self.valor_unitario = valor_unitario
        self.quantidade_maxima = quantidade_maxima
        self.fator_ajuste_preco = fator_ajuste_preco
        self.valor_unitario_reducao = valor_unitario_reducao
        self.brinde = brinde[:1]
        self.preco_custo = preco_custo
        self.perc_custo_venda = perc_custo_venda
        self.perc_min_margem = perc_min_margem
        self.perc_max_margem = perc_max_margem
        self.quantidade_minima = quantidade_minima
        self.descontar_brinde = descontar_brinde[:1]
        self.afeta_flex = afeta_flex[:1]
        self.alicota_ipi = alicota_ipi
        self.mostrar_margem = mostrar_margem[:1]
        self.mostrar_markup = mostrar_markup[:1]
        self.grupo_desconto = grupo_desconto
        self.reservado1 = reservado1[:39]

    @property
    def get_line(self):
        return(self._template.format(self))
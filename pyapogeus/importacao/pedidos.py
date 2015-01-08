# -*- coding: utf-8 -*-
from .deserializer import *

class Pedidos():

    _pedido = [
        ('numero_pedido', 1, 20, cnv_alfa),
        ('data_emissao', 21, 8, cnv_float(8, 0)),
        ('codigo_vendedor', 29, 3, cnv_num),
        ('codigo_cliente', 32, 10, cnv_float(10, 0)),
        ('coluna_precos_pauta', 42, 2, cnv_num),
        ('tipo_cobranca', 44, 3, cnv_num),
        ('data_entrega', 47, 8, cnv_date),
        ('data_digitacao', 55, 8, cnv_hour),
        ('hora_digitacao', 63, 6, cnv_date),
        ('codigo_pauta_precos', 69, 4, cnv_alfa),
        ('observacao_pedido', 73, 230, cnv_alfa),
        ('autorizacao_compra', 303, 20, cnv_alfa),
        ('codigo_vencimento', 323, 4, cnv_num),
        ('codigo_filial', 327, 1, cnv_num),
        ('especial', 328, 1, cnv_alfa),
        ('peso', 329, 12, cnv_float(9, 3)),
        ('reservado1', 341, 5, cnv_alfa),
        ('pedido_troca_bonificacao', 346, 1, cnv_alfa),
        ('tipo_frete', 347, 1, cnv_alfa),
        ('transportadora', 348, 6, cnv_num),
        ('desconto_financeiro', 354, 9, cnv_float(7, 2)),
        ('acrescimo_financeiro', 363, 9, cnv_float(7, 2)),
        ('total_pedido_bruto', 372, 9, cnv_float(7, 2)),
        ('total_pedido_liquido', 381, 9, cnv_float(7, 2)),
        ('total_st', 390, 9, cnv_float(7, 2)),
        ('sequencia_entrega', 399, 3, cnv_num),
        ('valor_frete', 402, 8, cnv_float(6, 2)),
        ('valor_ipi', 410, 9, cnv_float(7, 2)),
        ('valor_desconto_financeiro', 419, 9, cnv_float(7, 2)),
        ('valor_acrescimo_financeiro', 428, 9, cnv_float(7, 2)),
        ('afetou_flex_financeiro', 437, 1, cnv_alfa),
        ('reservado2', 438, 52, cnv_alfa)
        ]

    _item = [
        ('numero_pedido', 1, 20, cnv_alfa),
        ('codigo_produto', 21, 16, cnv_alfa),
        ('quantidade', 37, 9, cnv_float(6,3)),
        ('inventario', 46, 9, cnv_float(6,3)),
        ('valor_venda',55, 9, cnv_float(7,2)),
        ('valor_original', 64, 9, cnv_float(7,2)),
        ('percentual', 73, 5, cnv_float(3,2)),
        ('sinal_percentual', 78, 1, cnv_alfa),
        ('peso_do_item', 79, 12, cnv_float(9,3)),
        ('vendido_com_senha', 91, 1, cnv_alfa),
        ('saldo_flex_item', 92, 9, cnv_float(9,2)),
        ('sinal_flex', 101, 1, cnv_alfa),
        ('desconto_maximo', 102, 5, cnv_float(3,2)),
        ('acrescimo_maximo', 107, 5, cnv_float(7,2)),
        ('percentual_positivo', 112, 5, cnv_float(3,2)),
        ('percentual_negativo', 117, 5, cnv_float(3,2)),
        ('afetou_flex', 122, 1, cnv_alfa),
        ('quantidade_multipla', 123, 9, cnv_float(6,3)),
        ('quantidade_brinde', 132, 9, cnv_float(6,3)),
        ('reservado1', 141, 5, cnv_float(3,2)),
        ('quantidade_bonificacao', 146, 9, cnv_float(6,3)),
        ('reservado2', 155, 9, cnv_float(6,3)),
        ('reservado3', 164, 9, cnv_float(6,3)),
        ('brinde', 173, 1, cnv_alfa),
        ('reservado4', 174, 1, cnv_alfa),
        ('valor_custo_st', 175, 9, cnv_float(7,2)),
        ('valor_un_st', 184, 9, cnv_float(7,2)),
        ('preco_custo', 193, 9, cnv_float(7,2)),
        ('perc_preco_custo', 202, 6, cnv_float(3,3)),
        ('perc_margem_lucro', 208, 7, cnv_float(4,3)),
        ('alicota_ipi', 215, 5, cnv_float(3,2)),
        ('valor_base_ipi', 220, 9, cnv_float(7,2)),
        ('valor_ipi', 229, 9, cnv_float(7,2)),
        ('grupo_desconto', 238, 3, cnv_float(3,0)),
        ('reservado4', 241, 33, cnv_alfa),
        ]

    _prazo_pedido = [
        ('numero_pedido', 1, 20, cnv_alfa),
        ('numero_parcela', 21, 3, cnv_float(3,0)),
        ('quantidade', 24, 8, cnv_float(8,0)),
        ('reservado1', 32, 50, cnv_alfa)
        ]



    def __init__(self):
        self. _pedidos = {}
        pass

    def unpack_pedido(self, raw_line):
        data = {
            'pedido': (unpack_fields(self._pedido, raw_line)),
            'itens': [],
            'prazo': False,
            }
        numero_pedido = data['pedido']['numero_pedido']
        self._pedidos[numero_pedido] = data

    def unpack_item(self, raw_line):
        item = unpack_fields(self._item, raw_line)
        numero_pedido = item['numero_pedido']

        if self._pedidos.has_key(numero_pedido):
            self._pedidos[numero_pedido]['itens'].append(item)
            return True
        else:
            return False

    def unpack_prazo(self, raw_line):
        prazo = unpack_fields(self._prazo_pedido, raw_line)
        numero_pedido = prazo['numero_pedido']

        if self._pedidos.has_key(numero_pedido):
            self._pedidos[numero_pedido]['prazo'] = prazo
            return True
        else:
            return False

    @property
    def get_data(self):
        return(self._pedidos)
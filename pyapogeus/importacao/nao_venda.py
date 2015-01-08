# -*- coding: utf-8 -*-
from deserializer import *

class NaoVenda():

    _tabela_nao_venda = [
    ('codigo_vendedor', 1, 3, cnv_alfa),
    ('codigo_cliente',4, 10, cnv_alfa),
    ('codigo_justificatica', 14, 4, cnv_alfa),
    ('nivel_justificatica', 18, 2, cnv_float(2,0)),
    ('data_nao_venda', 20, 8, cnv_date),
    ('hora_nao_venda', 28, 6, cnv_hour),
    ('codigo_filial', 34, 1, cnv_float(1,0)),
    ('complemento_justificatica', 35, 30, cnv_alfa),
    ('reservado8', 65, 100, cnv_alfa),
    ]

    def __init__(self):
        pass
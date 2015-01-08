# -*- coding: utf-8 -*-
from deserializer import *

class Mensagem():

    _msg_vendedores = [
        ('codigo_vendedor', 1, 3, cnv_num),
        ('data_mensagem',4, 8, cnv_date),
        ('hora_mensagem', 12, 5, cnv_num),
        ('mensagem', 17, 250, cnv_alfa),
        ('setor_responsavel', 276, 20, cnv_alfa),
        ('reservado1', 287, 100, cnv_alfa)
        ]

    def __init__(self):
        pass
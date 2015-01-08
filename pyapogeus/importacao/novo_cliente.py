# -*- coding: utf-8 -*-
from deserializer import *

class NovoCliente():

    _novos_clientes = [
        ('codigo_cliente', 1, 10, cnv_alfa),
        ('nome_cliente', 11, 45, cnv_alfa),
        ('nome_fantasia', 56, 30, cnv_float(8,0)),
        ('endereco_cliente', 86, 45, cnv_alfa),
        ('cidade', 131, 25, cnv_alfa),
        ('estado', 156, 2, cnv_alfa),
        ('reservado1', 158, 1, cnv_alfa),
        ('codigo_vendedor', 156, 2, cnv_alfa),
        ('telefone_cliente', 162, 20, cnv_alfa),
        ('fax_cliente', 162, 20, cnv_alfa),
        ('reservado1', 202, 13, cnv_float(11,2)),
        ('observacoes_cadastrais', 215, 100, cnv_alfa),
        ('observacoes_financeiras', 315, 100, cnv_alfa),
        ('reservado2', 415, 3, cnv_float(3,0)),
        ('reservado3', 418, 4, cnv_alfa),
        ('reservado4', 422, 2, cnv_float(2,0)),
        ('reservado5', 424, 4, cnv_float(4,0)),
        ('codigo_filial', 428, 1, cnv_float(1)),
        ('reservado6', 429, 4, cnv_float(4,0)),
        ('reservado7', 433, 5, cnv_float(4,0)),
        ('contato', 438, 5, cnv_alfa),
        ('data_aniversario', 468, 4, cnv_alfa),
        ('reservado8', 472, 8, cnv_alfa),
        ('bairro', 480, 35, cnv_alfa),
        ('cep', 515, 8, cnv_alfa),
        ('fisco_juridico', 523, 1, cnv_alfa),
        ('classificacao', 524, 14, cnv_alfa),
        ('cnpj_cpf', 530, 14, cnv_alfa),
        ('ie', 544, 14, cnv_alfa),
        ('canal', 558, 4, cnv_float(4,0)),
        ('quantidade_checkout', 562, 4, cnv_float(4,0)),
        ('emails_cliente', 566, 100, cnv_alfa),
        ('proximidade', 666, 50, cnv_alfa),
        ('cliente_simples', 716, 1, cnv_alfa),
        ('numero_endereco', 717, 30, cnv_alfa),
        ('cpf_socio1', 747, 14, cnv_float(14,0)),
        ('cpf_socio1', 761, 14, cnv_float(14,0)),
        ('sede_propria', 523, 1, cnv_alfa),
        ('data_fundacao', 776, 8, cnv_date),
        ('area_estabelecimento', 784, 8, cnv_float(8,0)),
        ('numero_funcionarios', 792, 6, cnv_float(6,0)),
        ('telefone_fornecedor1', 798, 20, cnv_float(20,0)),
        ('telefone_fornecedor2', 818, 20, cnv_float(20,0)),
        ('nome_fornecedor1', 838, 40, cnv_alfa),
        ('nome_fornecedor2', 878, 40, cnv_alfa),
        ('consumidor_final', 918, 1, cnv_alfa),
        ('complemento_endereco', 919, 50, cnv_alfa),
        ('emails_danfe', 969, 100, cnv_alfa),
        ('emails_xml', 1069, 100, cnv_alfa),
        ('rg',1169, 20, cnv_alfa),
        ('orgao_emissor_rg', 1189, 10, cnv_alfa),
        ('data_expedicao_rg', 1199, 8, cnv_date),
        ('reservado8', 1207, 20, cnv_alfa),
    ]

    def __init__(self, raw_line):
        pass

    @property
    def get_data(self):
        return(self._clientes)

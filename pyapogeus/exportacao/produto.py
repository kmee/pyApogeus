# -*- coding: utf-8 -*-

class Produto():

    _template = (
        "{0.codigo_produto: <16}"
        "{0.descricao_produto: <40}"
        "{0.unidade: <3}"
        "{0.reservado1: <3}"
        "{0.descricao_embalagem: <10}"
        "{0.codigo_filial:0>1}"
        "{0.codigo_grupo:0>6}"
        "{0.descricao_grupo: <20}"
        "{0.peso_kg:0>12}"
        "{0.multiplo:0>5}"
        "{0.data_alteracao:0>8}"
        "{0.situacao_resigistro: <1}"
        "{0.observacao_produto: <20}"
        "{0.quantidade_varejo:0>9}"
        "{0.quantidade_multipla_bonificacao:0>9}"
        "{0.quantidade_produtos_bonificacao:0>9}"
        "{0.reservado2:0>5}"
        "{0.reservado3: <1}"
        "{0.reservado4: <5}"
        "{0.alvara: <1}"
        "{0.codigo_similaridade: <10}"
        "{0.permite_ouvidoria: <1}"
        "{0.reservado5: <32}"
    )

    def __init__(self, codigo_produto, descricao_produto, unidade,
    codigo_filial, codigo_grupo, descricao_grupo, peso_kg, multiplo,
    data_alteracao, situacao_resigistro, quantidade_varejo,
    reservado1='', descricao_embalagem='', observacao_produto='',
    quantidade_multipla_bonificacao='', quantidade_produtos_bonificacao='',
    reservado2='', reservado3='', reservado4='', alvara='',
    codigo_similaridade='', permite_ouvidoria='', reservado5=''):

        self.codigo_produto = str(codigo_produto)[:16]
        self.descricao_produto = descricao_produto[:40]
        self.unidade = unidade[:3]
        self.reservado1 = reservado1[:3]
        self.descricao_embalagem = descricao_embalagem[:10]
        self.codigo_filial = codigo_filial
        self.codigo_grupo = codigo_grupo
        self.descricao_grupo = descricao_grupo[:20]
        self.peso_kg = peso_kg
        self.multiplo = multiplo
        self.data_alteracao = data_alteracao.strftime("%d%m%Y")
        self.situacao_resigistro = situacao_resigistro[:1]
        self.observacao_produto = observacao_produto[:20]
        self.quantidade_varejo = quantidade_varejo
        self.quantidade_multipla_bonificacao = quantidade_multipla_bonificacao
        self.quantidade_produtos_bonificacao = quantidade_produtos_bonificacao
        self.reservado2 = reservado2
        self.reservado3 = reservado3[:1]
        self.reservado4 = reservado4[:5]
        self.alvara = alvara[:1]
        self.codigo_similaridade = codigo_similaridade[:10]
        self.permite_ouvidoria = permite_ouvidoria[:1]
        self.reservado5 = reservado5[:32]




        #self.filial = filial
        #self.codigo = codigo
        #self.descricao = descricao[:40]
        #self.uso_futuro = "%-3s" % ''
        #self.descricao_embalagem = descricao_embalagem
        #self.unidade = unidade[:3]
        #self.codigo_grupo = codigo_grupo
        #self.descricao_grupo = descricao_grupo
        #self.peso = peso
        #self.multiplo = multiplo
        #self.data_alteracao = data_alteracao.strftime("%d%m%Y")
        #self.situacao = situacao
        #self.observacao = observacao
        #self.quantidade_varejo = quantidade_varejo
        #self.quantidade_multipla = quantidade_multipla
        #self.quantidade_produtos_bonificacao = quantidade_produtos_bonificacao
        #self.uso_futuro1 = "%05d" % (0)
        #self.uso_futuro2 = "%-1s" % ''
        #self.uso_futuro3 = "%-5s" % ''
        #self.alvara = alvara
        #self.similaridade = similaridade
        #self.ouvidoria = ouvidoria
        #self.uso_futuro4 = "%-32s" % ''

    @property
    def get_line(self):
        return(self._template.format(self))


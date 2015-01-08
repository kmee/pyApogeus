# -*- coding: utf-8 -*-


class Cliente():

    _template = (
        "{0.codigo_cliente:0>10}"
        "{0.razao_social: <45}"
        "{0.nome_fantasia: <30}"
        "{0.endereco: <45}"
        "{0.bairro: <35}"
        "{0.cidade: <25}"
        "{0.uf: <2}"
        "{0.bloqueado: <1}"
        "{0.vendedor1:0>3}"
        "{0.vendedor2:0>3}"
        "{0.vendedor3:0>3}"
        "{0.vendedor4:0>3}"
        "{0.vendedor5:0>3}"
        "{0.tefefone: <20}"
        "{0.fax: <20}"
        "{0.emails: <200}"
        "{0.limite_credito:0>10}"
        "{0.observacao: <100}"
        "{0.observacao_financeira: <100}"
        "{0.tipo_cobranca:0>3}"
        "{0.codigo_pauta_precos: <4}"
        "{0.coluna_preco_pauta:0>2}"
        "{0.codigo_vencimento:0>4}"
        "{0.dias_amais_pagar:0>2}"
        "{0.codigo_filial:0>1}"
        "{0.reservado1: <8}"
        "{0.dias_maximo_vencimento:0>4}"
        "{0.percentual_desconto:0>5}"
        "{0.nome_contato: <30}"
        "{0.data_aniversario:0>4}"
        "{0.data_ultima_visita:0>8}"
        "{0.justificativa_ultima_nao_venda:0>4}"
        "{0.altera_pauta: <1}"
        "{0.altera_cobranca: <1}"
        "{0.altera_coluna: <1}"
        "{0.altera_vencimento: <1}"
        "{0.consumidor_final: <1}"
        "{0.data_alvara:0>8}"
        "{0.fisico_juridico: <1}"
        "{0.cnpj_cpf: <20}"
        "{0.hora_agendada:0>4}"
        "{0.reservado2: <1}"
        "{0.tipo_cliente: <1}"
        "{0.pautas_adicionais: <25}"
        "{0.proximidade: <50}"
        "{0.cliente_simlples: <1}"
        "{0.data_alvara:0>8}"
        "{0.alvara: <15}"
        "{0.data_inclusao:0>8}"
        "{0.cep: <8}"
        "{0.classificacao: <6}"
        "{0.ie: <14}"
        "{0.canal:0>4}"
        "{0.quantidade_checkout:0>4}"
        "{0.numero_endereco: <30}"
        "{0.cpf1:0>14}"
        "{0.cpf2:0>14}"
        "{0.sede_propria: <1}"
        "{0.data_fundacao:0>8}"
        "{0.area_estabelecimento:0>8}"
        "{0.numero_funcionarios:0>6}"
        "{0.telefone_fornecedor1:0>20}"
        "{0.telefone_fornecedor2:0>20}"
        "{0.nome_fornecedor1: <40}"
        "{0.nome_fornecedor2: <40}"
        "{0.complemento: <50}"
        "{0.email_danfe: <100}"
        "{0.email_xml: <100}"
        "{0.valor_frete:0>10}"
        "{0.reservado3: <10}"
        )

    def __init__(self, codigo_cliente, razao_social, endereco, cidade, uf,
         bloqueado, vendedor1, codigo_filial, altera_pauta, altera_cobranca,
         altera_coluna, altera_vencimento, consumidor_final, fisico_juridico,
         cnpj_cpf, nome_fantasia='', bairro='', vendedor2='', vendedor3='',
         vendedor4='', vendedor5='', tefefone='', fax='', emails='',
         limite_credito='', observacao='', observacao_financeira='',
         tipo_cobranca='', codigo_pauta_precos='', coluna_preco_pauta='',
         codigo_vencimento='', dias_amais_pagar='', reservado1='',
         dias_maximo_vencimento='', percentual_desconto='', nome_contato='',
         data_aniversario='', data_ultima_visita='',
         justificativa_ultima_nao_venda='', data_agendamento='', hora_agendada='',
         reservado2='', tipo_cliente='', pautas_adicionais='', proximidade='',
         cliente_simlples='', data_alvara='', alvara='', data_inclusao='',
         cep='', classificacao='', ie='', canal='', quantidade_checkout='',
         numero_endereco='', cpf1='', cpf2='', sede_propria='',
         data_fundacao='', area_estabelecimento='', numero_funcionarios='',
         telefone_fornecedor1='', telefone_fornecedor2='', nome_fornecedor1='',
         nome_fornecedor2='', complemento='', email_danfe='', email_xml='',
         valor_frete='', reservado3=''):

        self.codigo_cliente = codigo_cliente
        self.razao_social = razao_social[:45]
        self.nome_fantasia = nome_fantasia[:30]
        self.endereco = endereco[:45]
        self.bairro = bairro[:45]
        self.cidade = cidade[:25]
        self.uf = uf[:2]
        self.bloqueado = bloqueado[:1]
        self.vendedor1 = vendedor1
        self.vendedor2 = vendedor2
        self.vendedor3 = vendedor3
        self.vendedor4 = vendedor4
        self.vendedor5 = vendedor5
        self.tefefone = tefefone[:20]
        self.fax = fax[:20]
        self.emails = emails[:200]
        self.limite_credito = limite_credito[:10]
        self.observacao = observacao[:100]
        self.observacao_financeira = observacao_financeira[:100]
        self.tipo_cobranca = tipo_cobranca
        self.codigo_pauta_precos = codigo_pauta_precos[:4]
        self.coluna_preco_pauta = coluna_preco_pauta
        self.codigo_vencimento = codigo_vencimento
        self.dias_amais_pagar = dias_amais_pagar
        self.codigo_filial = codigo_filial
        self.reservado1 = ''
        self.dias_maximo_vencimento = dias_maximo_vencimento
        self.percentual_desconto = percentual_desconto
        self.nome_contato = nome_contato[:30]
        self.data_aniversario = data_aniversario
        self.data_ultima_visita = data_ultima_visita
        self.justificativa_ultima_nao_venda = justificativa_ultima_nao_venda
        self.altera_pauta = altera_pauta[:1]
        self.altera_cobranca = altera_cobranca[:1]
        self.altera_coluna = altera_coluna[:1]
        self.altera_vencimento = altera_vencimento[:1]
        self.consumidor_final = consumidor_final[:1]
        self.data_agendamento = data_agendamento
        self.fisico_juridico = fisico_juridico[:1]
        self.cnpj_cpf = cnpj_cpf[:20]
        self.hora_agendada = hora_agendada
        self.reservado2 = ' '
        self.tipo_cliente = tipo_cliente[:1]
        self.pautas_adicionais = pautas_adicionais[:25]
        self.proximidade = proximidade[:50]
        self.cliente_simlples = cliente_simlples[:1]
        self.data_alvara = data_alvara
        self.alvara = alvara[:15]
        self.data_inclusao = data_inclusao
        self.cep = cep[:8]
        self.classificacao = classificacao[:6]
        self.ie = ie[:14]
        self.canal = canal
        self.quantidade_checkout = quantidade_checkout
        self.numero_endereco = numero_endereco[:30]
        self.cpf1 = cpf1
        self.cpf2 = cpf2
        self.sede_propria = sede_propria[:1]
        self.data_fundacao = data_fundacao
        self.area_estabelecimento = area_estabelecimento
        self.numero_funcionarios = numero_funcionarios
        self.telefone_fornecedor1 = telefone_fornecedor1
        self.telefone_fornecedor2 = telefone_fornecedor2
        self.nome_fornecedor1 = nome_fornecedor1[:40]
        self.nome_fornecedor2 = nome_fornecedor2[:40]
        self.complemento = complemento[:50]
        self.email_danfe = email_danfe[:100]
        self.email_xml = email_xml[:100]
        self.valor_frete = valor_frete
        self.reservado3 = reservado3[:10]

    @property
    def get_line(self):
        return(self._template.format(self))
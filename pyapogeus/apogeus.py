# -*- coding: utf-8 -*-
from __future__ import print_function

from pyapogeus.exportacao.cliente import Cliente
from pyapogeus.exportacao.cobranca import Cobranca
from pyapogeus.exportacao.pauta import Pauta
from pyapogeus.exportacao.prazo_pauta import PrazoPauta
from pyapogeus.exportacao.preco import Preco
from pyapogeus.exportacao.produto import Produto
from pyapogeus.exportacao.vencimento import Vencimento
from pyapogeus.exportacao.vendedor import Vendedor

from pyapogeus.importacao.mensagem import Mensagem
from pyapogeus.importacao.nao_venda import NaoVenda
from pyapogeus.importacao.novo_cliente import NovoCliente
from pyapogeus.importacao.pedidos import Pedidos

import glob, os
from time import gmtime, strftime


class Apogeus():
    def __init__(self, filial=1, import_method=1, import_folder=False,
         export_folder=False):
        '''Import Folder = Pasta onde seram lidos os aquivos salvos
        pelo Apogeus

           Export Folder = Pasta onde serão salvos os aquivos com os
        dados gerados da retaguarda.
        '''
        self._filial = filial

        self._import_method = import_method
        self._import_folder = import_folder
        self._export_folder = export_folder

        self._clientes = []
        self._cobrancas = []
        self._pautas = []
        self._prazo_pauta = []
        self._precos = []
        self._produtos = []
        self._vencimentos = []
        self._vendedores = []

    def addProduto(self, args):
        p = Produto(**args)
        self._produtos.append(p.get_line)
        return True

    def addCliente(self, args):
        c = Cliente(**args)
        self._clientes.append(c.get_line)
        return True

    def addCobranca(self, args):
        c = Cobranca(**args)
        self._cobrancas.append(c.get_line)
        return True

    def addPreco(self, args):
        p = Preco(**args)
        self._precos.append(p.get_line)
        return True

    def addVencimento(self, args):
        v = Vencimento(**args)
        self._vencimentos.append(v.get_line)
        return True

    def addVendedor(self, args):
        v = Vendedor(**args)
        self._vendedores.append(v.get_line)
        return True

    def addPauta(self, args):
        p = Pauta(**args)
        self._pautas.append(p.get_line)
        return True

    def addPrazoPauta(self, args):
        pp = PrazoPauta(**args)
        self._prazo_pauta.append(pp.get_line)
        return True

    @property
    def save_tbcli(self):
        return self.writeFile(self._clientes, 'tbcli.txt')

    @property
    def save_tbcob(self):
        return self.writeFile(self._cobrancas, 'tbcob.txt')

    @property
    def save_tbpre(self):
        return self.writeFile(self._precos, 'tbpre.txt')

    @property
    def save_tbpro(self):
        return self.writeFile(self._produtos, 'tbpro.txt')

    @property
    def save_tbprp(self):
        return self.writeFile(self._prazo_pauta, 'tbprp.txt')

    @property
    def save_tbpta(self):
        return self.writeFile(self._pautas, 'tbpta.txt')

    @property
    def save_tbvct(self):
        return self.writeFile(self._vencimentos, 'tbvct.txt')

    @property
    def save_tbven(self):
        return self.writeFile(self._vendedores, 'tbven.txt')

    def writeFile(self, contents, filename):
        try:
            f = open((self._export_folder +'/'+ filename), "w")
            #file.write(contents)
            for line in contents:
                #print(line.encode("ascii", "ignore"), file=f)
                f.write( line.encode("ascii", "ignore") + '\r\n')
            f.close()
            return True
        except IOError:
            return "IOError"


    def getData(self):

        pedidos = Pedidos()
#        naoVenda = NaoVenda()
#        novosClientes = NovosClientes()

        if self._import_method == 1: #arquivos separados por data
            pass
        if self._import_method == 2:
            files = self.readFiles(self._import_folder , 'MT*')
            for f in files:
                for line in f:
                    if line[:2] == '10':
                        print (pedidos.unpack_pedido(line[2:]))
                    if line[:2] == '20':
                        print (pedidos.unpack_item(line[2:]))
                    if line[:2] == '25':
                        print (pedidos.unpack_prazo(line[2:]))
                    if line[:2] == '27':
                        print ("Itens Compostos")
                    if line[:2] == '30':
                        print ("Nao Venda")
                    if line[:2] == '40':
                        print ("Mensagens")
                    if line[:2] == '50':
                        print ("Novos Clientes")
        if self._import_method == 3: #arquivos separados por vendedor
            pass
        if self._import_method == 4: #arquivo unico por tipo de registro
            pass

        data = {
            'pedidos': pedidos.get_data,
            #'nao_venda': naoVenda.get_data,
            #'clientes': novosClientes.get_data,
            #'mensagens': mensagens.get_data,
                }


        return data

    def readFiles(self, folder, filename):
        files = []
        print ('Files', files)
        os.chdir(folder)
        for file_name in glob.glob(filename):
            print (strftime("%X", gmtime()))
            new_name = 'tmp/' + file_name +strftime(".%H%M%S.txt", gmtime())
            os.rename(file_name, new_name)
            f = open(new_name)
            files.append(f.readlines())
            f.close()
        return files
#!/usr/bin/python
# -*- coding: UTF-8 -*-
# Autor: Wandeson Ricardo
# www.wsricardo.blogspot.com/
# Data: 09/2009
# Notas: Implementar recurso para escolha de fonte. -> class windowFonteConfig

import os, sys
import codecs
from tkinter import*
import tkinter
import tkinter.font as tkFont
from tkinter.filedialog import*
from tkinter import tix
#Implementa janela para pesquisa.
#class pesquisa:
        #def __init():
        
#Classe para configurar fonte para o texto.-------------------------------
class windowFonteConfig:
        conf=0
        #Inicializando janela de escolha de fonte-------------------
        def __init__(self,janela):
                self.frame1 = Frame(janela)
                self.frame1.pack()
                self.frame2 = Frame(janela)
                self.frame2.pack()
                self.frame3 = Frame(janela)
                self.frame3.pack()
                
                #Label Fonte
                self.selec = Label(self.frame1, text = "Selecionar fonte: ")
                self.selec.pack()

                #Lista de fontes
                self.scrollbar = Scrollbar(self.frame2, orient = VERTICAL)
                self.listaFonte = Listbox(self.frame2,yscrollcommand = self.scrollbar.set)
                self.scrollbar.config(command = self.listaFonte.yview)
                self.scrollbar.pack(side = RIGHT, fill = BOTH, expand = 1)
                self.listaFonte.pack()

                #Listbox(caixa de lista) para definição
                #do tamanho da fonte.
                #<aqui>

                #Definindo estado da fonte, normal, italico, negrito.
                ##<aqui>
                
                #Botão para confirmação de fonte
                self.botao1 = Button(self.frame3, text="Ok")
                self.botao1.bind("<Button-1>",self.confFonte(1))
                self.botao1.pack(side=LEFT)
                self.botao2 = Button(self.frame3, text="Cancelar")
                self.botao2.bind("<Button-1>",self.confFonte(0))
                self.botao2.pack(side=RIGHT)

                pass
        #---------------------$$$--------------------------------

        #Configura atributos da fonte.-------------------------
        def confFonte(self,conf):
                self.conf = conf
                print("conf run...")
                if conf:
                        print("1")

                else:
                        print("0")
                        
                pass
        def getFonte(self,font):
                self.font = font
                return self.font
        def getSizeFonte(self,sizefont):
                self.sizefont = sizefont
                return self.sizefont
        #----------------------$$$-------------------------------

#----------------------$ Fim da classe para fonte. $---------------------------------

#Classe principal para interface do programa.----------------------------------------
class Interface:
        #arquivo_salvo = 0
        #fechar_arquivo = 0
        #arquivo_novo = 1
        ativ_Caps = 0
        p=0
        shift_press = 0
        #fileName = u''
        i = 0
        def __init__ (self, janela) :
                #Criando interface para o programa. Janelas, botões.
                self.frame = Frame(janela)
                self.frame.pack()
                #self.fileName = u''
                #iniciando variaveis para fonte
                self.sizeFont = 12
                self.nomeFont = "ArgorGotScaqh"
                self.estadoFont = '' #Negrito,italico ou normal. Variavel não utilizada no momento.

                #Constantes
                self.arquivo_salvo = 0
                self.fechar_arquivo = 0
                self.arquivo_novo = 1
                self.fileName = u''
                
                #Create scrollbar. Cria a barra de rolagem para o texto.
                self.sc_b = Scrollbar(self.frame)
                self.sc_b.pack(side=RIGHT,fill=Y)
                
                self.texto = Text(self.frame, wrap= WORD,font = self.nomeFont,yscrollcommand=self.sc_b.set)#,yscrollcommand=s.set)
                self.sc_b.config(command=self.texto.yview)              
                
                self.texto.bind(("<KeyPress-Shift_L>"),self.teclaShift_pressionada)
                #Atalhos
                self.texto.bind(("<KeyPress-Control_L>","<KeyPress-n>"),self.novoA)
                self.texto.bind(("<KeyPress-Control_L>","<KeyPress-o>"),self.abrirA)
                self.texto.bind(("<KeyPress-Control_L>","<KeyPress-s>"),self.salvarA)
                self.texto.bind(("<KeyPress-Control_L>","<KeyPress-e>"),self.fecharPrograma)
                self.texto.bind("<<cut>>",self.recortar)
                self.texto.bind("<<copy>>",self.copiar)
                self.texto.bind("<<paste>>",self.colar)
                self.texto.bind("<<find>>",self.pesquisar)
                self.texto.bind(("<KeyPress-Control_L>","<KeyPress-f>"), self.editarFonte)

                self.texto.pack()
                

                #Definindo fonte para texto
                tkFont.Font(family = self.nomeFont,size=self.sizeFont,weight=tkFont.BOLD)
                
                #Criando menu
                self.create_Menu()
                
                #Adicionado eventos para
                #pressionamento de tecla.
                #Exemplo: control+espaço
                
                # returns 
                pass
        def control_id(self,event):
                print("Control e Space pressionados")
                os.system('echo control space')
                return "Break"
        def tecla_Pressionada(self,event):
                arquivo_salvo = 0
                pass
        
        #Evento para atalhos.----------
        def novoA(self,event):
                self.novo_arquivo()
                pass
        def abrirA(self,event):
                self.abrir_arquivo_Texto()
                
                pass
        def salvarA(self,event):
                self.salvar_como_Texto()
                pass
        def fecharPrograma(self,event):
                self.sair()
                pass
        #-------------------------------                
        def teclaShift_pressionada(self,event):
                self.shift_press = 1
                pass
        
        #Menu file,arquivo-----------------------------------------------------------------. 
        def novo_arquivo(self):
                self.texto.delete(1.0,END)
                self.arquivo_salvo = 0
                self.arquivo_novo = 1
                pass
        def abrir_arquivo_Texto(self) : #ok
                fileDial = LoadFileDialog(raiz)
                loadfile = fileDial.go()
                self.fileName = loadfile
                self.arquivo = codecs.open(self.fileName,encoding='utf-8', mode='r+',buffering=1)
                self.f=self.arquivo.read()
                self.texto.insert(END,self.f)
                #self.novo_arquivo()            
                self.arquivo_salvo = 0
                self.arquivo_novo = 0
                        
                        
                #print loadfile
                #print arquivo
                #print f
                # returns 
                pass

        def salvar_Texto(self) :
                # returns 
                pass

        #Apaga conteudo de arquivo, para atualiza-lo.
        def deletar_conteudo(self,nome_do_arquivo):
                self.arquivo = codecs.open(nome_do_arquivo,encoding='utf-8', mode='r+',buffering=1)
                self.t = self.texto.get(1.0,END)
                self.arquivo.read()                        
                self.arquivo.seek(0)
                self.arquivo.write(self.t)
                pass
        #Salva arquivo.
        def salvar_como_Texto(self):
                if self.arquivo_salvo==0 and self.arquivo_novo==0:
                        #self.t = self.texto.get(1.0,END)
                        #self.arquivo = codecs.open(self.fileName,mode='w',encoding='UTF-8',buffering=1)
                        #self.arquivo.write(self.t)
                        self.deletar_conteudo(self.fileName)
                        self.arquivo_salvo = 1
                else:
                        self.fileDialog = SaveFileDialog(raiz)
                        self.savefile = self.fileDialog.go()
                        #Nome do arquivo
                        self.fileName = self.savefile
                        self.arquivo = codecs.open(self.fileName,encoding='UTF-8',mode='w',buffering=1)
                        self.t = self.texto.get(1.0,END)
                        self.arquivo.write(self.t)
                        self.arquivo_salvo = 1
                        
                #else:
                #       arquivo_salvo = 0
                       
                       
                       
        #---------------------------------------------------------------------------------
                        
        
        def sair(self) :
                #if len(self.texto.get(1.0,END))>1:
                if self.arquivo_salvo==0 and len(self.texto.get(1.0,END))>1:
                        self.fechar_arquivo = 1
                        self.salvar_como_Texto()
                        sys.exit()
                else:
                        sys.exit()
                # returns 
                pass
        #----------------------------------------------------------------------------------------------------------------------
        #Menu edit, editar. Recurso a ser implementado. Implementar recurso para selecionar todo texto. Falta implementar recurso para refazer e desfazer.
        #----------------------------------------------------------------------------------------------------------------------
        def desfazer(self):
                print('desfazer')
                pass
        def refazer(self):
                
                pass

        def recortar(self):
                self.texto.event_generate("<<Cut>>")
                return "break"

        def copiar(self):
                if not self.texto.tag_ranges("sel"):
                    #Não faz nada se não houver seleção.
                    return
                self.texto.event_generate("<<Copy>>")
                return "break"

        def colar(self):
                self.texto.event_generate("<<Paste>>")
                return "break" 
        
        def pesquisar(self,event):
                
                return "break"

        def editarFonte(self):
                menuFonte = Tk()
                windowFonteConfig(menuFonte)
                menuFonte.title("FONTE")
                self.obterFonte(menuFonte)
                #menuFonte.mainloop()
                pass
        def obterFonte(self,fonte):
                self.fonte = fonte
                self.nomeFont = self.fonte.getFont()
                self.sizeFont = self.fonte.getSizeFont()

                pass    
#---------------------------------------------------------------------------------------------------------
        def abrir_Ajuda (self) :
                ajuda = Tk()
                Ajuda(ajuda)
                ajuda.title("SOBRE")
                ajuda.mainloop()
                # returns 
                pass

        def create_Menu(self):
                menu = Menu()
                raiz.config(menu=menu)
                #Filemenu. Menu de arquivo(abrir,novo,salvar,sair).
                filemenu = Menu(menu)
                menu.add_cascade(label="Arquivo",menu=filemenu)
                filemenu.add_command(label="Novo ctrl+n", command=self.novo_arquivo)
                filemenu.add_command(label="Abrir ctrl+a", command=self.abrir_arquivo_Texto)
                filemenu.add_command(label="Salvar ctrl+s", command=self.salvar_como_Texto)
                filemenu.add_separator()
                #Recurso para criação de audio de leitura com espeak desativado.
                #este recurso necessita correções.
                #filemenu.add_command(label="Ler", command=self.falar_Texto)
                #filemenu.add_command(label="Grava Leitura",command=self.grava_Leitura)
                #filemenu.add_separator()
                filemenu.add_command(label="Sair ctrl+e", command=self.sair)
                
                #Menu Editar
                editmenu = Menu(menu)
                menu.add_cascade(label="Editar",menu = editmenu)
                #adicionar copiar,colar e recortar. Este esta faltando correções.
                #Ver codigo do idle python.
                editmenu.add_command(label="Recortar ctrl+x",command = self.recortar)
                editmenu.add_command(label="Copiar ctrl+c", command = self.copiar)
                editmenu.add_command(label="Colar ctrl+v", command = self.colar)
                editmenu.add_separator()
                editmenu.add_command(label="Fonte ctrl+f", command = self.editarFonte)
                """editmenu.add_command(label="Desfazer",command = self.desfazer)
                editmenu.add_command(label="Refazer",command = self.refazer)
                editmenu.add_separator()
                editmenu.add_command(label="Pesquisar",command = self.pesquisar)"""
                #Ajuda
                ajudamenu = Menu(menu)
                menu.add_cascade(label="Ajuda", menu = ajudamenu)
                ajudamenu.add_command(label="Sobre", command = self.abrir_Ajuda)

#----------------Fim da classe Interface-----------------------------------------------

#Classe que mplementa janela de "ajuda".-----------------------------------------------
class Ajuda:
        def __init__ (self,janelaAjuda) :
                self.frameAjuda = Frame(janelaAjuda)
                self.frameAjuda.pack()
                self.frameAjuda2 = Frame(janelaAjuda)
                self.frameAjuda2.pack()
                
                self.info = Label(self.frameAjuda,  text="Programa criado por Wandeson R.\n\n")
                self.info.pack()
                self.info2 = Label(self.frameAjuda2,text="Editor de texto simples EdiTextPy.\nhttps://wsricardo.blogspot.com")
                self.info2.pack()
                
                # returns 
                pass
        #Menssage
        def Mensagem(self) :
                # returns 
                pass
        #Help
        def Ajuda(self) :
                # returns 
                pass
#----------------------$Fim da classe de "Ajuda".$---------------------

#Cria a janela Tk, com Interface.
raiz = Tk()
Interface(raiz)
raiz.title("EditTextPy")
raiz.mainloop()

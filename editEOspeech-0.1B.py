#!/usr/bin/python
# -*- coding: UTF-8 -*-
#Autor: Wandeson Ricardo
#www.kartunoderikardo.blogspot.com/
#Data: 09/2009
import os, sys
import codecs
from Tkinter import*
import Tkinter
import tkFont
from FileDialog import*
import Tix
#from entraDados import*
#from Tkconstants import*
class Interface:
	arquivo_salvo = 0
	ativ_Caps = 0
	p=0
	shift_press = 0
	fileName = ''
	i = 0
	def __init__ (self, janela) :
		self.frame = Frame(janela)
		self.frame.pack()
		self.fileName = ''
		#Create scrollbar. Cria a barra de rolagem para o texto.
		self.sc_b = Scrollbar(self.frame)
		self.sc_b.pack(side=RIGHT,fill=Y)
		
		self.texto = Text(self.frame, wrap= WORD,font = "Times",yscrollcommand=self.sc_b.set)#,yscrollcommand=s.set)
		self.sc_b.config(command=self.texto.yview)
		#Tratando caracteres esperanto.
		self.texto.bind(("<KeyPress-Alt_L>","<KeyPress-x>","<KeyPress-G>"),self.tecla_pressionadaEOg)
		self.texto.bind(("<KeyPress-Alt_L>","<KeyPress-x>","<KeyPress-c>"),self.tecla_pressionadaEOc)
		self.texto.bind(("<KeyPress-Alt_L>","<KeyPress-x>","<KeyPress-s>"),self.tecla_pressionadaEOs)
		self.texto.bind(("<KeyPress-Alt_L>","<KeyPress-x>","<KeyPress-h>"),self.tecla_pressionadaEOh)
		self.texto.bind(("<KeyPress-Alt_L>","<KeyPress-x>","<KeyPress-j>"),self.tecla_pressionadaEOj)
		self.texto.bind(("<KeyPress-Alt_L>","<KeyPress-x>","<KeyPress-u>"),self.tecla_pressionadaEOu)
		#MAIUSCULAS
		self.texto.bind(("<KeyPress-Alt_L>","<KeyPress-Control_L>","<KeyPress-x>","<KeyPress-g>"),self.tecla_pressionadaEOG)
		self.texto.bind(("<KeyPress-Alt_L>","<KeyPress-Control_L>","<KeyPress-x>","<KeyPress-c>"),self.tecla_pressionadaEOC)
		self.texto.bind(("<KeyPress-Alt_L>","<KeyPress-Control_L>","<KeyPress-x>","<KeyPress-s>"),self.tecla_pressionadaEOS)
		self.texto.bind(("<KeyPress-Alt_L>","<KeyPress-Control_L>","<KeyPress-x>","<KeyPress-h>"),self.tecla_pressionadaEOH)
		self.texto.bind(("<KeyPress-Alt_L>","<KeyPress-Control_L>","<KeyPress-x>","<KeyPress-j>"),self.tecla_pressionadaEOJ)
		self.texto.bind(("<KeyPress-Alt_L>","<KeyPress-Control_L>","<KeyPress-x>","<KeyPress-u>"),self.tecla_pressionadaEOU)
		self.texto.bind(("<KeyPress-Control_L>","<KeyPress-space>"),self.control_id)
		#----------------------------------------------------------------------
		#self.texto.bind(("<KeyPress-Alt_L>","<KeyPress-x>","<KeyPress-g>"),self.tecla_pressionadaEOg)
		self.texto.bind(("<KeyPress-Shift_L>"),self.teclaShift_pressionada)
		
		#self.texto.bind
		
		"""if self.shift_press==1:
			self.texto.bind("<KeyPress-caret>",self.tecla_caret)
			
			self.shift_press = 0"""
		self.texto.pack()
		

		#Definindo fonte para texto
		tkFont.Font(family="Times",size=11,weight=tkFont.BOLD)
		
		#Criando menu
		self.create_Menu()
		
		#Adicionado eventos para
		#pressionamento de tecla.
		#Exemplo: control+espaço
		
		# returns 
		pass
	def control_id(self,event):
		print "Control e Space pressionados"
		os.system('echo control space')
		return "Break"
	#Caracteres esperanto------------------------------------------------------------------------------
	def tecla_pressionadaEOg(self,event):
		self.texto.insert(END,u'ĝ')
		
		pass
	def tecla_pressionadaEOc(self,event):
		self.texto.insert(END,u'ĉ')
		
		pass
	def tecla_pressionadaEOs(self,event):
		self.texto.insert(END,u'ŝ')
		
		pass
	def tecla_pressionadaEOh(self,event):
		self.texto.insert(END,u'ĥ')
		
		pass
	def tecla_pressionadaEOj(self,event):
		self.texto.insert(END,u'ĵ')
		
		pass
	def tecla_pressionadaEOu(self,event):
		self.texto.insert(END,u'ŭ')
		
		pass	
	
	def tecla_pressionadaEOG(self,event):
		self.texto.insert(END,u'Ĝ')
		
		pass
	def tecla_pressionadaEOC(self,event):
		self.texto.insert(END,u'Ĉ')
		
		pass
	def tecla_pressionadaEOS(self,event):
		self.texto.insert(END,u'Ŝ')
		
		pass
	def tecla_pressionadaEOH(self,event):
		self.texto.insert(END,u'Ĥ')
		
		pass
	def tecla_pressionadaEOJ(self,event):
		self.texto.insert(END,u'Ĵ')
		
		pass
	def tecla_pressionadaEOU(self,event):
		self.texto.insert(END,u'Ŭ')
		
		pass
	

	#Esperanto--------------------------------------------------------------------------------		
		
	def teclaShift_pressionada(self,event):
		self.shift_press = 1
		pass
	
	#Menu file,arquivo-----------------------------------------------------------------. 
	def novo_arquivo(self):
		self.texto.delete(1.0,END)
		self.arquivo_salvo = 0
		pass
	def abrir_arquivo_Texto (self) :
		fileDial = LoadFileDialog(raiz)
		loadfile = fileDial.go()
		self.fileName = loadfile
		arquivo = codecs.open(loadfile,encoding='utf-8', mode='r+a',buffering=1)
		f=arquivo.read()
		self.novo_arquivo()
		self.texto.insert(END,f)
		self.arquivo_salvo = 0
		#print loadfile
		#print arquivo
		#print f
		# returns 
		pass
	def salvar_Texto (self) :
		# returns 
		pass
	def salvar_como_Texto(self):
		if self.arquivo_salvo:
			self.t = self.texto.get(1.0,END)
			#print self.t
			self.arquivo.write(self.t)	
			
		else:
			self.fileDialog = SaveFileDialog(raiz)
			self.savefile = self.fileDialog.go()
			self.arquivo = codecs.open(self.savefile,encoding='utf-8',mode='w+a',buffering=1)
			self.f = self.arquivo.read()
			self.t = self.texto.get(1.0,END)
			#print self.t
			self.arquivo.write(self.t)
			self.arquivo_salvo=1
			
		pass
	def falar_Texto (self) :
		entrada = '"'+self.fileName+'"'
		if self.arquivo_salvo:
			#Para alterar voz e idioma so seguir a documentação do espeak.
			#Alterar idioma e voz nesta linha abaixo.
			os.system('echo  |  espeak -f %s -vpt+f2' %entrada)
		else:
			print "Save file. Salve arquivo"
		# returns 
		pass
	
	#Ler texto e gravar o aúdio da leitura
	def grava_Leitura(self):
		self.i = self.i+1
		name = "output"+str(self.i) 
		entrada = '"'+self.fileName+'"'
		print "entrada",entrada
		#print"entrada", entrada
		#Correções: Selecionar nome para arquivo audio gerado. 
		#Acrescentar recursso para escolha do idioma.
		os.system('echo | espeak -f "%s"'%entrada +' -w " %s.wav" -vpt+f2 '   %name)
		pass
		
	def salvar_audio_Texto (self,texto) :
		# returns 
		pass
	def sair (self) :
		if len(self.texto.get(1.0,END))>1:
			self.salvar_como_Texto()
			sys.exit()
		else:
			sys.exit()
		# returns 
		pass
	#----------------------------------------------------------------------------------------------------------------------
	#Menu edit, editar. Recurso a ser implementado.
	#----------------------------------------------------------------------------------------------------------------------
	def desfazer(self):
		print 'desfazer'
		pass
	def refazer(self):
		
		pass
	def pesquise(self):
		
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
		
		filemenu = Menu(menu)
		menu.add_cascade(label="Arquivo",menu=filemenu)
		filemenu.add_command(label="Novo", command=self.novo_arquivo)
		filemenu.add_command(label="Abrir", command=self.abrir_arquivo_Texto)
		filemenu.add_command(label="Salvar como", command=self.salvar_como_Texto)
		filemenu.add_command(label="Ler", command=self.falar_Texto)
		filemenu.add_command(label="Grava Leitura",command=self.grava_Leitura)
		filemenu.add_separator()
		filemenu.add_command(label="Sair", command=self.sair)
		
		editmenu = Menu(menu)
		menu.add_cascade(label="Editar",menu=editmenu)
		editmenu.add_command(label="Desfazer",command=self.desfazer)
		editmenu.add_command(label="Refazer",command=self.refazer)
		editmenu.add_separator()
		editmenu.add_command(label="Pesquisar",command=self.pesquise)
		
		ajudamenu = Menu(menu)
		menu.add_cascade(label="Ajuda", menu=ajudamenu)
		ajudamenu.add_command(label="Sobre", command=self.abrir_Ajuda)
		

class Ajuda :
	def __init__ (self,janelaAjuda) :
		self.frameAjuda = Frame(janelaAjuda)
		self.frameAjuda.pack()
		self.frameAjuda2 = Frame(janelaAjuda)
		self.frameAjuda2.pack()
		
		self.info = Label(self.frameAjuda,  text="Programa criado por Wandeson R.")
		self.info.pack()
		self.info2 = Label(self.frameAjuda2,text="Necessita de programa \n para sintese de voz instalado,\nde preferencia Espeak.")
		self.info2.pack()
		self.esperantocaract = Label(self.frameAjuda2, text="""
		Esperanto
		ŝ/ĝ/ĉ/ĵ/ĥ/ŭ = alt_left+x+s/g/c/j/h/u
		Ŝ/Ĝ/Ĉ/Ĵ/Ĥ/Ŭ = alt_Left+Control_Left+x+s/g/c/j/h/u			
		""")
		self.esperantocaract.pack()
		
		# returns 
		pass
	#Menssage
	def Mensagem (self) :
		# returns 
		pass
	#Help
	def Ajuda (self) :
		# returns 
		pass

raiz = Tk()
Interface(raiz)
raiz.title("TexttoSpeech")
raiz.mainloop()

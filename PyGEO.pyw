#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from PyQt4 import QtGui, uic
import os

 
# Cargar nuestro archivo .ui
form_class = uic.loadUiType("maquetado.ui")[0]

class pyGIS(QtGui.QMainWindow, form_class):
	
	def __init__(self, parent=None):
		QtGui.QMainWindow.__init__(self, parent)
		self.setupUi(self)
		########################################
		self.SAVI1_2.triggered.connect(self.SAVI)
		self.NDVI1.triggered.connect(self.NDVI)
		self.button_IAF_LAI.triggered.connect(self.IAF)
		
		
#######################################################################
		self.button_calcular.clicked.connect(self.calcular)
		self.button_punto.clicked.connect(self.punto)
		self.button_1.clicked.connect(self.uno)
		self.button_2.clicked.connect(self.dos)
		self.button_3.clicked.connect(self.tres)
		self.button_4.clicked.connect(self.cuatro)
		self.button_5.clicked.connect(self.cinco)
		self.button_6.clicked.connect(self.seis)
		self.button_7.clicked.connect(self.siete)
		self.button_8.clicked.connect(self.ocho)
		self.button_9.clicked.connect(self.nueve)
		self.button_0.clicked.connect(self.cero)
		
########################################################################
		self.button_suma.clicked.connect(self.suma)
		self.button_resta.clicked.connect(self.resta)
		self.button_division.clicked.connect(self.division)
		self.button_multi.clicked.connect(self.multi)
		self.button_pi.clicked.connect(self.pi)
		self.button_pare_dere.clicked.connect(self.parentesis_derecho)
		self.button_pare_izqui.clicked.connect(self.parentesis_izquierdo)
		self.button_potencia.clicked.connect(self.potencia)
		self.button_borrar.clicked.connect(self.borrar)
		self.button_e.clicked.connect(self.exp)
		self.button_ln_2.clicked.connect(self.Ln)
		self.button_log10.clicked.connect(self.log10)

		
		self.button_cos.clicked.connect(self.cos)
		self.button_sin.clicked.connect(self.sin)
		self.button_tan.clicked.connect(self.tan)
		self.button_igual.clicked.connect(self.igual)
		self.button_capa_a.clicked.connect(self.capa_a)
		self.button_capa_b.clicked.connect(self.capa_b)
		self.button_capa_c.clicked.connect(self.capa_c)
		self.button_limpiar.clicked.connect(self.limpiar)
		self.button_limpiar_todo.clicked.connect(self.limpiar_todo)
		self.button_menor.clicked.connect(self.mayor)
		self.button_mayor.clicked.connect(self.menor)
		self.button_OR.clicked.connect(self.OR)
		self.button_AND.clicked.connect(self.AND)

		self.button_max.clicked.connect(self.maxim)
		self.button_min.clicked.connect(self.minim)
		self.button_sqrt.clicked.connect(self.sqrt)
		self.button_sqrt3.clicked.connect(self.sqrt3)
########################################################################		
		
	def borrar(self):
		anterior = self.lineEdit.text()[:-1]
		self.lineEdit.setText(anterior)
		
	def limpiar(self):
		self.lineEdit.clear()
	
	def limpiar_todo(self):
		self.lineEdit.clear()
		self.lineEdit_A.clear()
		self.lineEdit_B.clear()
		self.lineEdit_C.clear()
		self.lineEdit_salida.clear()
		self.estado.setText("")	
		
		
	def mayor(self):
		actual = self.lineEdit.text()
		self.lineEdit.setText(actual + " > ")
		
	def menor(self):
		actual = self.lineEdit.text()
		self.lineEdit.setText(actual + " < ")
		
	def OR(self):
		actual = self.lineEdit.text()
		self.lineEdit.setText(actual + " or ")
		
	def AND(self):
		actual = self.lineEdit.text()
		self.lineEdit.setText(actual + " and ")						
		
	def capa_a(self):
		actual = self.lineEdit.text()
		self.lineEdit.setText(actual + "A")
	
	def capa_b(self):
		actual = self.lineEdit.text()
		self.lineEdit.setText(actual + "B")
	
	def capa_c(self):
		actual = self.lineEdit.text()
		self.lineEdit.setText(actual + "C")		
			
		
	def punto(self):
		actual = self.lineEdit.text()
		self.lineEdit.setText(actual + ".")


	def uno(self):
		actual = self.lineEdit.text()
		self.lineEdit.setText(actual + "1")
	
	def dos(self):
		actual = self.lineEdit.text()
		self.lineEdit.setText(actual + "2")			
	
	def tres(self):
		actual = self.lineEdit.text()
		self.lineEdit.setText(actual + "3")
			
	def cuatro(self):
		actual = self.lineEdit.text()
		self.lineEdit.setText(actual + "4")
		
	def cinco(self):
		actual = self.lineEdit.text()
		self.lineEdit.setText(actual + "5")
		
	def seis(self):
		actual = self.lineEdit.text()
		self.lineEdit.setText(actual + "6")
		
	def siete(self):
		actual = self.lineEdit.text()
		self.lineEdit.setText(actual + "7")							
		
	def ocho(self):
		actual = self.lineEdit.text()
		self.lineEdit.setText(actual + "8")	
	
	def nueve(self):
		actual = self.lineEdit.text()
		self.lineEdit.setText(actual + "9")
		
	def cero(self):
		actual = self.lineEdit.text()
		self.lineEdit.setText(actual + "0")
#Operaciones############################################################
	def suma(self):
		actual = self.lineEdit.text()
		self.lineEdit.setText(actual + "+")
		
	def resta(self):
		actual = self.lineEdit.text()
		self.lineEdit.setText(actual + "-")
		
	def multi(self):
		actual = self.lineEdit.text()
		self.lineEdit.setText(actual + "*")
		
	def division(self):
		actual = self.lineEdit.text()
		self.lineEdit.setText(actual + "/")
		
	def pi(self):
		actual = self.lineEdit.text()
		self.lineEdit.setText(actual + "pi")
	
	def parentesis_derecho(self):
		actual = self.lineEdit.text()
		self.lineEdit.setText(actual + "(")
	
	def parentesis_izquierdo(self):
		actual = self.lineEdit.text()
		self.lineEdit.setText(actual + ")")
	
	
	def potencia(self):
		actual = self.lineEdit.text()
		self.lineEdit.setText(actual + "**")
												
	def Ln(self):
		actual = self.lineEdit.text()
		self.lineEdit.setText(actual + "log()")
		
	def cos(self):
		actual = self.lineEdit.text()
		self.lineEdit.setText(actual + "cos()")			
			
	def sin(self):
		actual = self.lineEdit.text()
		self.lineEdit.setText(actual + "sin()")
		
	def tan(self):
		actual = self.lineEdit.text()
		self.lineEdit.setText(actual + "tan()")
		
	def igual(self):
		actual = self.lineEdit.text()
		self.lineEdit.setText(actual + "=")			
		
	def exp(self):
		actual = self.lineEdit.text()
		self.lineEdit.setText(actual + "exp**()")
		
	def log10(self):
		actual = self.lineEdit.text()
		self.lineEdit.setText(actual + "log10()")
		
	def maxim(self):
		actual = self.lineEdit.text()
		self.lineEdit.setText(actual + "amax()")
		
	def minim(self):
		actual = self.lineEdit.text()
		self.lineEdit.setText(actual + "amin()")
		
	def sqrt(self):
		actual = self.lineEdit.text()
		self.lineEdit.setText(actual + "sqrt()")
		
	def sqrt3(self):
		actual = self.lineEdit.text()
		self.lineEdit.setText(actual + "sqrt3()")	
				
									
			
			
#Funciones##############################################################
	
	def NDVI(self):
		actual = self.lineEdit.text()
		self.lineEdit.setText(actual + " (A-B)/(A+B)")
				
	
	def IAF(self):
		actual = self.lineEdit.text()
		self.lineEdit.setText(actual + " (((0.69-A)/0.59)/0.91)*(-1) ")
		
	def reflectancia_toa(self):
		actual = self.lineEdit.text()
		self.lineEdit.setText(actual + " (0.00002*A+(-0.100000))/(sin(53.60472025)) ")	
	
	def radiancia_toa(self):
		actual = self.lineEdit.text()
		self.lineEdit.setText(actual + " (0.0003342* A +0.10000)/(sin(53.60472025)) ")
		
	def temperatura_toa_b10(self):
		actual = self.lineEdit.text()
		self.lineEdit.setText(actual + " (1321.0789/log((774.8853/A)+1)) ")
		
	def temperatura_toa_b11(self):
		actual = self.lineEdit.text()
		self.lineEdit.setText(actual + " (1321.0789/log((774.8853/A)+1)) ")		
	
	def SAVI(self):
		actual = self.lineEdit.text()
		self.lineEdit.setText(actual + " ((A-B)*(1+0.5))/(A+B+0.5)")


	def calcular(self):
		actual = str(self.lineEdit.text())
		A = str(self.lineEdit_A.text())
		B = str(self.lineEdit_B.text())
		C = str(self.lineEdit_C.text())
		salida = str(self.lineEdit_salida.text())
		bandaA = A
		bandaB = B
		bandaC = C
		outfile = salida 
		EQ = actual
		
		if (A == "" and B == "" and C == ""):
			self.estado.setText( "Por favor ingrese las capas")
		elif (A != "" and B == "" and C == ""):
			sentencia = " gdal_calc.py -A "+bandaA+".tif --outfile="+ salida +".tif --calc=" + '"' + EQ + '"'
			self.estado.setText( "Procesando capas, esto puede llevar unos minutos...")
			os.system(sentencia)
			self.estado.setText( "Proceso finalizado con exito")
		elif (A == "" and B != "" and C == ""):
			sentencia = " gdal_calc.py -B "+bandaB+".tif --outfile="+ salida +".tif --calc=" + '"' + EQ + '"'
			self.estado.setText( "Procesando capas, esto puede llevar unos minutos...")
			os.system(sentencia)
			self.estado.setText( "Proceso finalizado con exito")
		elif (A == "" and B == "" and C != ""):
			sentencia = " gdal_calc.py -C "+bandaC+".tif --outfile="+ salida +".tif --calc=" + '"' + EQ + '"'
			self.estado.setText( "Procesando capas, esto puede llevar unos minutos...")
			os.system(sentencia)
			self.estado.setText( "Proceso finalizado con exito")
		elif (A == "" and B != "" and C != ""):
			sentencia = " gdal_calc.py -B "+bandaB+".tif -C "+bandaC+".tif --outfile="+ salida +".tif --calc=" + '"' + EQ + '"'
			self.estado.setText( "Procesando capas, esto puede llevar unos minutos...")
			os.system(sentencia)
			self.estado.setText( "Proceso finalizado con exito")
		elif (A !="" and B != "" and C ==""):
			sentencia = " gdal_calc.py -A "+bandaA+".tif -B "+bandaB+".tif --outfile="+ salida +".tif --calc=" + '"' + EQ + '"'
			self.estado.setText("Procesando capas, esto puede llevar unos minutos...")
			os.system(sentencia)
			self.estado.setText( "Proceso finalizado con exito")
		elif (A !="" and B != "" and C !=""):	
			sentencia = " gdal_calc.py -A "+bandaA+".tif -B "+bandaB+".tif  -C "+bandaC+".tif  --outfile="+ salida +".tif --calc=" + '"' + EQ + '"'
			self.estado.setText("Procesando capas, esto puede llevar unos minutos...")
			os.system(sentencia)
			self.estado.setText("Proceso finalizado con exito")
		else:
			self.estado.setText(" A ocurrido un error")		

		
	

app = QtGui.QApplication(sys.argv)
MyWindow = pyGIS(None)
MyWindow.show()
app.exec_()

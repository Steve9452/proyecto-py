# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Sesion.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
from PyQt5.QtWidgets import QMessageBox

def fnMensaje( sMensaje, sInformacion):
        msg= QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText(sMensaje)
        msg.setInformativeText(sInformacion)
        msg.setWindowTitle("Login")
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()
        return


class Ui_dlgSesion(object):
    db_name='database.db'
    def setupUi(self, dlgSesion):
        dlgSesion.setObjectName("dlgSesion")
        dlgSesion.resize(400, 300)

        self.groupBox = QtWidgets.QGroupBox(dlgSesion)
        self.groupBox.setGeometry(QtCore.QRect(10, 20, 371, 201))
        self.groupBox.setObjectName("groupBox")


        self.labelUsuario = QtWidgets.QLabel(self.groupBox)
        self.labelUsuario.setGeometry(QtCore.QRect(20, 30, 91, 31))
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(14)
        self.labelUsuario.setFont(font)
        self.labelUsuario.setObjectName("labelUsuario")
        


        self.labelContrasena = QtWidgets.QLabel(self.groupBox)
        self.labelContrasena.setGeometry(QtCore.QRect(20, 70, 131, 31))
        #font = QtGui.QFont()
        #font.setFamily("MS Reference Sans Serif")
        #font.setPointSize(14)
        self.labelContrasena.setFont(font)
        self.labelContrasena.setObjectName("labelContrasena")


        self.labelNombre = QtWidgets.QLabel(self.groupBox)
        self.labelNombre.setGeometry(QtCore.QRect(20, 110, 131, 31))
        #font = QtGui.QFont()
        #font.setFamily("MS Reference Sans Serif")
        #font.setPointSize(14)
        self.labelNombre.setFont(font)
        self.labelNombre.setObjectName("labelNombre")


        self.labelRol = QtWidgets.QLabel(self.groupBox)
        self.labelRol.setGeometry(QtCore.QRect(20, 150, 131, 31))
        #font = QtGui.QFont()
        #font.setFamily("MS Reference Sans Serif")
        #font.setPointSize(14))
        self.labelRol.setFont(font)
        self.labelRol.setObjectName("labelRol")  


        self.lineUsuario = QtWidgets.QLineEdit(self.groupBox)
        self.lineUsuario.setGeometry(QtCore.QRect(150, 40, 191, 21))
        #font = QtGui.QFont()
        #font.setFamily("OCR A Extended")
        font.setPointSize(9)
        self.lineUsuario.setFont(font)
        self.lineUsuario.setText("")
        self.lineUsuario.setMaxLength(20)
        self.lineUsuario.setObjectName("lineUsuario")
        #self.lineUsuario.keyPressEvent = self.keyPressEvent


        #self.lineUsuario.textChanged.connect(self.fnCambiosline)#Dectetar cambios en lineas

        self.lineUsuario.returnPressed.connect(self.fnProcesaEnter)# Procesado de tecla enter


        self.lineContrasena = QtWidgets.QLineEdit(self.groupBox)
        self.lineContrasena.setGeometry(QtCore.QRect(150, 80, 191, 21))
        #font = QtGui.QFont()
        #font.setFamily("OCR A Extended")
        #font.setPointSize(9)
        self.lineContrasena.setFont(font)
        self.lineContrasena.setText("")
        self.lineContrasena.setMaxLength(20)
        self.lineContrasena.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineContrasena.setObjectName("lineContrasena")

        #self.lineContrasena.textChanged.connect(self.fnCambiosline)#Dectetar cambios en lineas

        self.lineContrasena.returnPressed.connect(self.fnProcesaEnter) # Procesado de tecla enter
        #self.get_log()

        self.lineNombre = QtWidgets.QLineEdit(self.groupBox)
        self.lineNombre.setEnabled(False)
        self.lineNombre.setGeometry(QtCore.QRect(150, 120, 191, 21))
        #font = QtGui.QFont()
        #font.setFamily("OCR A Extended")
        font.setPointSize(12)
        self.lineNombre.setFont(font)
        self.lineNombre.setMaxLength(20)
        self.lineNombre.setObjectName("lineNombre")


        self.lineRol = QtWidgets.QLineEdit(self.groupBox)
        self.lineRol.setEnabled(False)
        self.lineRol.setGeometry(QtCore.QRect(150, 160, 191, 21))
        #font = QtGui.QFont()
        #font.setFamily("OCR A Extended")
        #font.setPointSize(9)
        self.lineRol.setFont(font)
        self.lineRol.setMaxLength(20)
        self.lineRol.setObjectName("lineRol")




        self.pushButtonAccept = QtWidgets.QPushButton(dlgSesion)
        self.pushButtonAccept.setGeometry(QtCore.QRect(190, 230, 161, 41))
        #self.pushButtonAccept.clicked.connect(self.fnEvento)
        #font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonAccept.setFont(font)
        icon = QtGui.QIcon.fromTheme("accept")
        self.pushButtonAccept.setIcon(icon)
        self.pushButtonAccept.setObjectName("pushButtonAccept")
        self.pushButtonAccept.setAutoDefault(False)
        self.pushButtonAccept.setDefault(False)
        #self.pushButtonAccept.keyPressEvent()
        self.pushButtonAccept.clicked.connect(self.fnAceptar)
        #self.pushButtonAccept.clicked.connect(self.validarLog) #Test

        self.pushButtonCancel = QtWidgets.QPushButton(dlgSesion)
        self.pushButtonCancel.setGeometry(QtCore.QRect(20, 230, 161, 41))

        #font = QtGui.QFont()
        #font.setPointSize(11)
        #font.setBold(True)
        #font.setWeight(75)

        self.pushButtonCancel.setFont(font)
        icon = QtGui.QIcon.fromTheme("accept")
        self.pushButtonCancel.setIcon(icon)
        self.pushButtonCancel.setObjectName("pushButtonCancel") 
        self.pushButtonCancel.setAutoDefault(False)
        self.pushButtonCancel.setDefault(False) 
        self.pushButtonCancel.clicked.connect(self.fnCancelar)#Manda un mensaje a consola
        


        self.retranslateUi(dlgSesion)
        
        QtCore.QMetaObject.connectSlotsByName(dlgSesion)

    def retranslateUi(self, dlgSesion):    # Textos dentro de los widdgets
        _translate = QtCore.QCoreApplication.translate
        dlgSesion.setWindowTitle(_translate("dlgSesion", "Inicio de sesion"))
        self.groupBox.setTitle(_translate("dlgSesion", "Credenciales"))
        self.labelUsuario.setText(_translate("dlgSesion", "Usuario:"))
        self.labelContrasena.setText(_translate("dlgSesion", "Contraseña:"))
        self.lineNombre.setText(_translate("dlgSesion", "No asignado"))
        self.labelNombre.setText(_translate("dlgSesion", "Nombre:"))
        self.labelRol.setText(_translate("dlgSesion", "Rol:"))
        self.lineRol.setText(_translate("dlgSesion", "No asignado"))
        self.pushButtonAccept.setText(_translate("dlgSesion", "Aceptar"))
        self.pushButtonCancel.setText(_translate("dlgSesion", "Cancelar"))


#Funciones
    def fnProcesaEnter(self):
        #print("Has presionado enter")
        if (self.lineUsuario.hasFocus()):
            #print("Foco a Contrasena")
            self.lineContrasena.setFocus()
        elif (self.lineContrasena.hasFocus()):
            #print("Cambio a Aceptar")
            self.fnAceptar()
            #if ((len(self.lineUsuario.text())) > 0 and len(self.lineContrasena.text()) > 0 ): #TEST
            #    self.fnAceptar()


    #funcion para dectar evento de presion de tecla
    def keyPressEvent(self,event):
        #print("Se ha presionado una tecla",event.text())
        #if (self.lineUsuario.hasFocus()):
        
        return QtWidgets.QLineEdit.keyPressEvent(self.lineUsuario,event)#retorna el valor de la tecla presionada



    def fnCancelar(self):
        print("Has presionado Cancelar")
        self.pushButtonCancel.clicked.connect(quit)#Cierra la ventana

    def fnAceptar(self):
        if (self.validarLog()):
            #print("Usuario: ",self.lineUsuario.text())
            #print("Password: ",self.lineContrasena.text())
            self.validarDatosLog()


    def fnCambiosline(self):
        if (self.lineUsuario.hasFocus()):
            print("Cambio de texto en usuario")
            #print(self.lineUsuario.text())#.text()Escribe lo que este en el lineEdit
            
        else:
            print("Cambio de texto en password")



    def fnEvento(self):
        print("Evento detectado")
        #self.lineContrasena.setFocus()#Setea el focus 
    
  

    def run_query(self, query, parameters = ()):
        #conn = sqlite3.connect('db_name.db')
        #c = conn.cursor()
        #result= c.execute(query, parameters)
        #conn.commit()
        #conn.close()
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            result = cursor.execute(query, parameters)
            conn.commit()
        return result
    
    def validarDatosLog(self): #Pedir datos a database y guardar en array text, password
       query = 'SELECT * FROM login ORDER BY permiss'
       db_rows = self.run_query(query)
       text= ''
       password= ''
       name=''
       permiss = 0
       for row in db_rows:
           
           text= row[0]
           password= row[1]
           permiss= row[2]
           name= row[3]
           if (self.lineUsuario.text() == text):
               if(self.lineContrasena.text() == password):                   
                   self.lineUsuario.setEnabled(False)
                   self.lineContrasena.setEnabled(False)
                   self.pushButtonAccept.setEnabled(False)
                   self.pushButtonCancel.setEnabled(False)
                   #print(permiss,name)
                   self.logStatus(permiss,name)
                   fnMensaje("Sesion iniciada satisfactoriamente ","Presione aceptar para iniciar el programa (VENTANA TEMPORAL)")#TEMPORAL verificar validacion de datos
                   
                    
                   return True              
           print("DATA: " ,text, password)
       fnMensaje("Fallo inicio de sesion","Usuario o contraseña incorrectos ")
       return False

    def logStatus(self,permiss,name):
        _translate = QtCore.QCoreApplication.translate
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(85, 85, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        self.lineNombre.setPalette(palette)
        self.lineRol.setPalette(palette)

        if(permiss == 0):
            #print("es admin")
            self.lineNombre.setText(_translate("dlgSesion", name))
            self.lineRol.setText(_translate("dlgSesion", "Administrador"))
        else:
            #print("es user")
            self.lineNombre.setText(_translate("dlgSesion", name))
            self.lineRol.setText(_translate("dlgSesion", "Esclavo "))
            

    def validarLog(self): #Funcion para validar que los linEdit no esten vacios
        sMensaje = ""
        #print(len(self.lineUsuario.text()))
        if (len(self.lineUsuario.text()) == 0):
            #print("Entro")
            sMensaje = "Usuario \n"
            self.lineUsuario.setFocus()
        
        if (len(self.lineContrasena.text()) == 0):
            if(len(sMensaje) ==0):
                self.lineContrasena.setFocus()
            sMensaje = sMensaje + "Contraseña "
        if(len(sMensaje) > 0 ):
            sMensaje= "Revise los siguientes datos : \n" +sMensaje
            fnMensaje(sMensaje,"El usuario y la contraseña no pueden quedar vacios")
            self.lineUsuario.clear()
            return False
        else:
            print("Usuario y contrasena ingresados ")
            return True




#main
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    dlgSesion = QtWidgets.QDialog()
    ui = Ui_dlgSesion()
    ui.setupUi(dlgSesion)
    dlgSesion.show()
    sys.exit(app.exec_())




#       SQL
"""def get_log(self): #Pedir datos a database y guardar en array text, password
       query = 'SELECT * FROM login ORDER BY permiss'
       db_rows = self.run_query(query)
       text= ['']
       password= ['']
       for row in db_rows:
           i=0
           #print(row)
           text[i]= row[0]
           #text= row[0]
           #password= row[1]
           password[i]= row[1]
           print(text[i], password[i])
           i+1"""
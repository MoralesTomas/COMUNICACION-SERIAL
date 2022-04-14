# para la comunicacion serial
import serial
import time

#para la interfaz
import sys
from PyQt5 import uic
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QApplication,QMessageBox

arduino = serial.Serial('COM4', 9600)
time.sleep(2)


class ejemplo_GUI(QMainWindow):

    def __init__(self):
        super().__init__()
        uic.loadUi("interfaz//interfazui.ui", self)
        self.arreglo = [[2,2,2],[2,2,2],[2,2,2]]
        self.B00.clicked.connect(self.B00_)
        self.B01.clicked.connect(self.B01_)
        self.B02.clicked.connect(self.B02_)

        self.B10.clicked.connect(self.B10_)
        self.B11.clicked.connect(self.B11_)
        self.B12.clicked.connect(self.B12_)

        self.B20.clicked.connect(self.B20_)
        self.B21.clicked.connect(self.B21_)
        self.B22.clicked.connect(self.B22_)

        self.reset.clicked.connect(self.reseteo)
        self.jugador_Actual = 1

    #Primera fila

    def B00_(self):
        if self.jugador_Actual == 1:
            self.B00.setText("X")
            self.B00.setStyleSheet("background-color : #00FF32") 
            self.jugador_Actual = 2
            self.txtJugador.setText("2")
            #metodo envio datos para el jugador 1
            # tablero,posA,posB,posC,FilaSubA,FilaSubB
            cadena = '0,1,0,0,0,0'
            arduino.write(cadena.encode('ascii'))
            self.arreglo[0][0] = 0
        else:
            self.B00.setText("O")
            self.B00.setStyleSheet("background-color : #FF0F00") 
            self.jugador_Actual = 1
            self.txtJugador.setText("1")
            #metodo envio datos para el jugador 2
            # tablero,FilaSubA,FilaSubB,ColumnaSubA,ColumnaSubB
            cadena = '1,0,0,0,0'
            arduino.write(cadena.encode('ascii'))
            self.arreglo[0][0] = 1
        self.B00.setEnabled(False)
        self.revision()

    def B01_(self):
        if self.jugador_Actual == 1:
            self.B01.setText("X")
            self.B01.setStyleSheet("background-color : #00FF32") 
            self.jugador_Actual = 2
            self.txtJugador.setText("2")
            #metodo envio datos para el jugador 1
            # tablero,posA,posB,posC,FilaSubA,FilaSubB
            cadena = '0,0,1,0,0,0'
            arduino.write(cadena.encode('ascii'))
            self.arreglo[0][1] = 0
        else:
            self.B01.setText("O")
            self.B01.setStyleSheet("background-color : #FF0F00") 
            self.jugador_Actual = 1
            self.txtJugador.setText("1")
            #metodo envio datos para el jugador 2
            # tablero,FilaSubA,FilaSubB,ColumnaSubA,ColumnaSubB
            cadena = '1,0,0,0,1'
            arduino.write(cadena.encode('ascii'))
            self.arreglo[0][1] = 1
        self.B01.setEnabled(False)
        self.revision()

    def B02_(self):
        if self.jugador_Actual == 1:
            self.B02.setText("X")
            self.B02.setStyleSheet("background-color : #00FF32") 
            self.jugador_Actual = 2
            self.txtJugador.setText("2")
            #metodo envio datos para el jugador 1
            # tablero,posA,posB,posC,FilaSubA,FilaSubB
            cadena = '0,0,0,1,0,0'
            arduino.write(cadena.encode('ascii'))
            self.arreglo[0][2] = 0
        else:
            self.B02.setText("O")
            self.B02.setStyleSheet("background-color : #FF0F00") 
            self.jugador_Actual = 1
            self.txtJugador.setText("1")
            #metodo envio datos para el jugador 2
            # tablero,FilaSubA,FilaSubB,ColumnaSubA,ColumnaSubB
            cadena = '1,0,0,1,0'
            self.arreglo[0][2] = 1
        self.B02.setEnabled(False)
        self.revision()
    
    # Segunda fila

    def B10_(self):
        if self.jugador_Actual == 1:
            self.B10.setText("X")
            self.B10.setStyleSheet("background-color : #00FF32") 
            self.jugador_Actual = 2
            self.txtJugador.setText("2")
            #metodo envio datos para el jugador 1
            # tablero,posA,posB,posC,FilaSubA,FilaSubB
            cadena = '0,1,0,0,0,1'
            arduino.write(cadena.encode('ascii'))
            self.arreglo[1][0] = 0
        else:
            self.B10.setText("O")
            self.B10.setStyleSheet("background-color : #FF0F00") 
            self.jugador_Actual = 1
            self.txtJugador.setText("1")
            #metodo envio datos para el jugador 2
            # tablero,FilaSubA,FilaSubB,ColumnaSubA,ColumnaSubB
            cadena = '1,0,1,0,0'
            arduino.write(cadena.encode('ascii'))
            self.arreglo[1][0] = 1
        self.B10.setEnabled(False)
        self.revision()
    
    def B11_(self):
        if self.jugador_Actual == 1:
            self.B11.setText("X")
            self.B11.setStyleSheet("background-color : #00FF32") 
            self.jugador_Actual = 2
            self.txtJugador.setText("2")
            #metodo envio datos para el jugador 1
            # tablero,posA,posB,posC,FilaSubA,FilaSubB
            cadena = '0,0,1,0,0,1'
            arduino.write(cadena.encode('ascii'))
            self.arreglo[1][1] = 0
        else:
            self.B11.setText("O")
            self.B11.setStyleSheet("background-color : #FF0F00") 
            self.jugador_Actual = 1
            self.txtJugador.setText("1")
            #metodo envio datos para el jugador 2
            # tablero,FilaSubA,FilaSubB,ColumnaSubA,ColumnaSubB
            cadena = '1,0,1,0,1'
            arduino.write(cadena.encode('ascii'))
            self.arreglo[1][1] = 1
        self.B11.setEnabled(False)
        self.revision()
    
    def B12_(self):
        if self.jugador_Actual == 1:
            self.B12.setText("X")
            self.B12.setStyleSheet("background-color : #00FF32") 
            self.jugador_Actual = 2
            self.txtJugador.setText("2")
            #metodo envio datos para el jugador 1
            # tablero,posA,posB,posC,FilaSubA,FilaSubB
            cadena = '0,0,0,1,0,1'
            arduino.write(cadena.encode('ascii'))
            self.arreglo[1][2] = 0
        else:
            self.B12.setText("O")
            self.B12.setStyleSheet("background-color : #FF0F00") 
            self.jugador_Actual = 1
            self.txtJugador.setText("1")
            #metodo envio datos para el jugador 2
            # tablero,FilaSubA,FilaSubB,ColumnaSubA,ColumnaSubB
            cadena = '1,0,1,1,0'
            arduino.write(cadena.encode('ascii'))
            self.arreglo[1][2] = 1
        self.B12.setEnabled(False)
        self.revision()

    # Tercera fila
    def B20_(self):
        if self.jugador_Actual == 1:
            self.B20.setText("X")
            self.B20.setStyleSheet("background-color : #00FF32") 
            self.jugador_Actual = 2
            self.txtJugador.setText("2")
            #metodo envio datos para el jugador 1
            # tablero,posA,posB,posC,FilaSubA,FilaSubB
            cadena = '0,1,0,0,1,0'
            arduino.write(cadena.encode('ascii'))
            self.arreglo[2][0] = 0
        else:
            self.B20.setText("O")
            self.B20.setStyleSheet("background-color : #FF0F00") 
            self.jugador_Actual = 1
            self.txtJugador.setText("1")
            #metodo envio datos para el jugador 2
            # tablero,FilaSubA,FilaSubB,ColumnaSubA,ColumnaSubB
            cadena = '1,1,0,0,0'
            arduino.write(cadena.encode('ascii'))
            self.arreglo[2][0] = 1
        self.B20.setEnabled(False)
        self.revision()
    
    def B21_(self):
        if self.jugador_Actual == 1:
            self.B21.setText("X")
            self.B21.setStyleSheet("background-color : #00FF32") 
            self.jugador_Actual = 2
            self.txtJugador.setText("2")
            #metodo envio datos para el jugador 1
            # tablero,posA,posB,posC,FilaSubA,FilaSubB
            cadena = '0,0,1,0,1,0'
            arduino.write(cadena.encode('ascii'))
            self.arreglo[2][1] = 0
        else:
            self.B21.setText("O")
            self.B21.setStyleSheet("background-color : #FF0F00") 
            self.jugador_Actual = 1
            self.txtJugador.setText("1")
            #metodo envio datos para el jugador 2
            # tablero,FilaSubA,FilaSubB,ColumnaSubA,ColumnaSubB
            cadena = '1,1,0,0,1'
            arduino.write(cadena.encode('ascii'))
            self.arreglo[2][1] = 1
        self.B21.setEnabled(False)
        self.revision()
    
    def B22_(self):
        if self.jugador_Actual == 1:
            self.B22.setText("X")
            self.B22.setStyleSheet("background-color : #00FF32") 
            self.jugador_Actual = 2
            self.txtJugador.setText("2")
            #metodo envio datos para el jugador 1
            # tablero,posA,posB,posC,FilaSubA,FilaSubB
            cadena = '0,0,0,1,1,0'
            arduino.write(cadena.encode('ascii'))
            self.arreglo[2][2] = 0
        else:
            self.B22.setText("O")
            self.B22.setStyleSheet("background-color : #FF0F00") 
            self.jugador_Actual = 1
            self.txtJugador.setText("1")
            #metodo envio datos para el jugador 2
            # tablero,FilaSubA,FilaSubB,ColumnaSubA,ColumnaSubB
            cadena = '1,1,0,1,0'
            arduino.write(cadena.encode('ascii'))
            self.arreglo[2][2] = 1
        self.B22.setEnabled(False)
        self.revision()

    def revision(self):
        # primero revisar en linea recta.
        for i in range(3):
            if self.arreglo[i][0] == 0 and self.arreglo[i][1] == 0 and self.arreglo[i][2] == 0:
                # mostrar mensaje J1
                QMessageBox.information(self, "FIN DE LA PARTIDA","El jugador 1 gana la partida.\n")
                self.reseteo()
                return
            elif self.arreglo[i][0] == 1 and self.arreglo[i][1] == 1 and self.arreglo[i][2] == 1:
                # mostrar mensaje J2
                QMessageBox.information(self, "FIN DE LA PARTIDA","El jugador 2 gana la partida.\n")
                self.reseteo()
                return
            
        # ahora con las lineas en vertical
        for i in range(3):
            if self.arreglo[0][i] == 0 and self.arreglo[1][i] == 0 and self.arreglo[2][i] == 0:
                # mostrar mensaje J1
                QMessageBox.information(self, "FIN DE LA PARTIDA","El jugador 1 gana la partida.\n")
                self.reseteo()
                return
            elif self.arreglo[0][i] == 1 and self.arreglo[1][i] == 1 and self.arreglo[2][i] == 1:
                # mostrar mensaje J2
                QMessageBox.information(self, "FIN DE LA PARTIDA","El jugador 2 gana la partida.\n")
                self.reseteo()
                return
        # ahora las diagonales.

        if self.arreglo[0][0] == 0 and self.arreglo[1][1] == 0 and self.arreglo[2][2] == 0:
            # mostrar mensaje J1
            QMessageBox.information(self, "FIN DE LA PARTIDA","El jugador 1 gana la partida.\n")
            self.reseteo()
            return
        if self.arreglo[0][0] == 1 and self.arreglo[1][1] == 1 and self.arreglo[2][2] == 1:
            # mostrar mensaje J2
            QMessageBox.information(self, "FIN DE LA PARTIDA","El jugador 2 gana la partida.\n")
            self.reseteo()
            return

        if self.arreglo[0][2] == 0 and self.arreglo[1][1] == 0 and self.arreglo[2][0] == 0:
            # mostrar mensaje J1
            QMessageBox.information(self, "FIN DE LA PARTIDA","El jugador 1 gana la partida.\n")
            self.reseteo()
            return

        if self.arreglo[0][2] == 1 and self.arreglo[1][1] == 1 and self.arreglo[2][0] == 1:
            # mostrar mensaje J2
            QMessageBox.information(self, "FIN DE LA PARTIDA","El jugador 2 gana la partida.\n")
            self.reseteo()
            return

    def reseteo(self):
        self.B00.setText("")
        self.B01.setText("")
        self.B02.setText("")
        self.B10.setText("")
        self.B11.setText("")
        self.B12.setText("")
        self.B20.setText("")
        self.B21.setText("")
        self.B22.setText("")

        self.B00.setStyleSheet("background-color : #e3e3e3")
        self.B01.setStyleSheet("background-color : #e3e3e3")
        self.B02.setStyleSheet("background-color : #e3e3e3")
        self.B10.setStyleSheet("background-color : #e3e3e3")
        self.B11.setStyleSheet("background-color : #e3e3e3")
        self.B12.setStyleSheet("background-color : #e3e3e3")
        self.B20.setStyleSheet("background-color : #e3e3e3")
        self.B21.setStyleSheet("background-color : #e3e3e3")
        self.B22.setStyleSheet("background-color : #e3e3e3")

        self.B00.setEnabled(True)
        self.B01.setEnabled(True)
        self.B02.setEnabled(True)
        self.B10.setEnabled(True)
        self.B11.setEnabled(True)
        self.B12.setEnabled(True)
        self.B20.setEnabled(True)
        self.B21.setEnabled(True)
        self.B22.setEnabled(True)

        self.jugador_Actual = 1

        for i in range(3):
            for j  in range(3):
                self.arreglo[i][j] = 2
        self.txtJugador.setText("1")

        # apagando las luces pero entrando en el tablero del jugador 2
        cadena = '1,0,0,0,0'
        arduino.write(cadena.encode('ascii'))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    GUI = ejemplo_GUI()
    GUI.show()
    sys.exit(app.exec_())
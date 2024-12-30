
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QAction, QLineEdit, QMessageBox,QTableView,QTableWidget,QTableWidgetItem,QSlider
# importing QTimer
from PyQt5.QtCore import QTimer
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
# import QPlainTextEdit
from PyQt5.QtWidgets import QPlainTextEdit
# import label
from PyQt5.QtWidgets import QLabel
from compiler import Compiler
from  computer import Register, Memory, Computer
import pickle
def create_computer(program):
    computer = Computer()
    compiler = Compiler(program)
    program_start = compiler.load(computer.ram)
    computer.run(program_start)

    return computer
class App(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = 'Assembler'
        self.left = 10
        self.top = 10
        self.width = 1050
        self.height =705
        self.initUI()
    
    def initUI(self):
        self.init_ = False
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
    

        self.code_tb = QPlainTextEdit(self)
        self.code_tb.move(0, 100)
        self.code_tb.resize(300,600)
        # sc label
        self.sc_l = QLabel('SC:',self)
        self.sc_l.move((1400//3-190 +30), 180) 
        # seting a line edit for label
        self.sc_le = QLineEdit(self)
        self.sc_le.move((1400//3-190 +60), 180)
        self.sc_le.resize(50,30)
        self.sc_le.setReadOnly(True)
        # PC label
        self.pc_l = QLabel('PC:',self)
        self.pc_l.move((1400//3-190 +115), 180)
        # seting a line edit for label
        self.pc_le = QLineEdit(self)
        self.pc_le.move((1400//3-190 +145), 180)
        self.pc_le.resize(100,30)
        self.pc_le.setReadOnly(True)
        # AR label
        self.ar_l = QLabel('AR:',self)
        self.ar_l.move((1400//3-190 +250), 180)
        # seting a line edit for label
        self.ar_le = QLineEdit(self)
        self.ar_le.move((1400//3-190 +280), 180)
        self.ar_le.resize(100,30)
        self.ar_le.setReadOnly(True)
        # new line in labels
        # IR label
        self.ir_l = QLabel('IR:',self)
        self.ir_l.move((1400//3-190 +30), 215)
        # seting a line edit for label
        self.ir_le = QLineEdit(self)
        self.ir_le.move((1400//3-190 +60), 215)
        self.ir_le.resize(100,30)
        self.ir_le.setReadOnly(True)
        # DR label
        self.dr_l = QLabel('DR:',self)
        self.dr_l.move((1400//3-190 +165), 215)
        # seting a line edit for label
        self.dr_le = QLineEdit(self)
        self.dr_le.move((1400//3-190 +195), 215)
        self.dr_le.resize(100,30)
        self.dr_le.setReadOnly(True)
        # AC label
        self.ac_l = QLabel('AC:',self)
        self.ac_l.move((1400//3-190 +300), 215)
        # seting a line edit for label
        self.ac_le = QLineEdit(self)
        self.ac_le.move((1400//3-190 +325), 215)
        self.ac_le.resize(100,30)
        self.ac_le.setReadOnly(True)
        # new line in labels
        # TR label
        self.tr_l = QLabel('TR:',self)
        self.tr_l.move((1400//3-190 +30), 250)
        # seting a line edit for label
        self.tr_le = QLineEdit(self)
        self.tr_le.move((1400//3-190 +60), 250)
        self.tr_le.resize(100,30)
        self.tr_le.setReadOnly(True)
        # INPR label
        self.inpr_l = QLabel('INPR:',self)
        self.inpr_l.move((1400//3-190 +165), 250)
        # seting a line edit for label
        self.inpr_le = QLineEdit(self)
        self.inpr_le.move((1400//3-190 +205), 250)
        self.inpr_le.resize(100,30)
        self.inpr_le.setReadOnly(True)
        # OUTR label
        self.outr_l = QLabel('OUTR:',self)
        self.outr_l.move((1400//3-190 +310), 250)
        # seting a line edit for label
        self.outr_le = QLineEdit(self)
        self.outr_le.move((1400//3-190 +355), 250)
        self.outr_le.resize(100,30)
        self.outr_le.setReadOnly(True)
        # new line in labels
        # the labels are I, S,E,R
        # I label
        self.i_l = QLabel('I:',self)
        self.i_l.move((1400//3-190 +30), 285)
        # seting a line edit for label
        self.i_le = QLineEdit(self)
        self.i_le.move((1400//3-190 +45), 285)
        self.i_le.resize(30,30)
        self.i_le.setReadOnly(True)
        # S label
        self.s_l = QLabel('S:',self)
        self.s_l.move((1400//3-190 +80), 285)
        # seting a line edit for label
        self.s_le = QLineEdit(self)
        self.s_le.move((1400//3-190 +95), 285)
        self.s_le.resize(30,30)
        self.s_le.setReadOnly(True)
        # E label
        self.e_l = QLabel('E:',self)
        self.e_l.move((1400//3-190 +130), 285)
        # seting a line edit for label
        self.e_le = QLineEdit(self)
        self.e_le.move((1400//3-190 +145), 285)
        self.e_le.resize(30,30)
        self.e_le.setReadOnly(True)

        # R label
        self.r_l = QLabel('R:',self)
        self.r_l.move((1400//3-190 +180), 285)
        # seting a line edit for label
        self.r_le = QLineEdit(self)
        self.r_le.move((1400//3-190 +195), 285)
        self.r_le.resize(30,30)
        self.r_le.setReadOnly(True)
        # new line in labels
        # the labels are IEN, FGI, FGO
        # lable IEN
        self.ien_l = QLabel('IEN:',self)
        self.ien_l.move((1400//3-190 +30), 320)
        # seting a line edit for label
        self.ien_le = QLineEdit(self)
        self.ien_le.move((1400//3-190 +60), 320)
        self.ien_le.resize(30,30)
        self.ien_le.setReadOnly(True)
        # lable FGI
        self.fgi_l = QLabel('FGI:',self)
        self.fgi_l.move((1400//3-190 +95), 320)
        # seting a line edit for label
        self.fgi_le = QLineEdit(self)
        self.fgi_le.move((1400//3-190 +125), 320)
        self.fgi_le.resize(30,30)
        self.fgi_le.setReadOnly(True)
        # lable FGO
        self.fgo_l = QLabel('FGO:',self)
        self.fgo_l.move((1400//3-190 +160), 320)
        # seting a line edit for label
        self.fgo_le = QLineEdit(self)
        self.fgo_le.move((1400//3-190 +195), 320)
        self.fgo_le.resize(30,30)
        self.fgo_le.setReadOnly(True)
        # new line
        # label Ins
        self.ins_l = QLabel('Instruction:',self)
        self.ins_l.move((1400//3-190 +30), 420)
        # seting a line edit for label
        self.ins_le = QLineEdit(self)
        self.ins_le.move((1400//3-190 +110), 420)
        self.ins_le.resize(340,30)
        self.ins_le.setReadOnly(True)

        # Next push button
        self.next_pb = QPushButton('Next',self)
        self.next_pb.move((1400//3-190 +30), 500)
        self.next_pb.resize(100,30)
        self.next_pb.clicked.connect(self.next_clicked)
        # Play push button
        self.play_pb = QPushButton('Play',self)
        self.play_pb.move((1400//3-190 +135), 500)
        self.play_pb.resize(100,30)
        self.play_pb.clicked.connect(self.play_clicked)
        # Stop push button
        self.pause_pb = QPushButton('Stop',self)
        self.pause_pb.move((1400//3-190 +240), 500)
        self.pause_pb.resize(100,30)
        self.pause_pb.clicked.connect(self.stop_clicked)
        #log label
        self.log_l = QLabel('Logs:',self)
        self.log_l.move((1400//3-190 +30), 550)
        
        # log text box
        self.log_tb = QPlainTextEdit(self)
        self.log_tb.move((1400//3-190 +70), 550)
        self.log_tb.resize(250,100)
        self.log_tb.setReadOnly(True)

        # displaying a table on the right side of the window
        self.tableWidget = QTableWidget(self)
        # seting a column for table
        self.tableWidget.setColumnCount(2)
        # seting a row for table
        self.tableWidget.setRowCount(4096)
        self.tableWidget.move((1200-450), 30)
        self.tableWidget.resize(219,600)
        # seting name for columns
        self.tableWidget.setHorizontalHeaderLabels(['Line number','Hex'])
        self.tableWidget.verticalHeader().setVisible(False)

        for i in range(4096):
        
            self.tableWidget.setItem(i,0,QTableWidgetItem(str(hex(i))[2:].zfill(3)))
        # label speed
        self.sc_l = QLabel('Speed:',self)
        self.sc_l.move((1400//3-190 +60), 462) 
        
        # creating a slider selection with speed label
        self.speed_value = 5
        self.speed_sl = QSlider(Qt.Horizontal,self)
        self.speed_sl.move((1400//3-190 +110), 470)
        self.speed_sl.resize(260,20)
        self.speed_sl.setMinimum(1)
        self.speed_sl.setMaximum(10)
        self.speed_sl.setValue(5)
        self.speed_sl.valueChanged[int].connect(self.speed_changed)
       
        




        
        

        # self.pc_le = QLineEdit(self)
        # self.pc_le.move((1400//3 +140), 180)
        # self.pc_le.resize(100,30)



        self.assemble_butt = QPushButton('Assemble', self)
        self.assemble_butt.move(5,10)
        self.assemble_butt.resize(100,50)
        self.help_butt = QPushButton('Help', self)
        self.help_butt.move(130,10)
        self.help_butt.resize(100,50)
        self.assemble_butt.clicked.connect(self.assemble_clicked)
        self.help_butt.clicked.connect(self.help_clicked)
        self.show()
    def update_params(self):
        if self.init_:
            self.ram = pickle.load(self.varibles_f)
            self.ar = pickle.load(self.varibles_f)
            self.pc = pickle.load(self.varibles_f)
            self.dr = pickle.load(self.varibles_f)
            self.ac = pickle.load(self.varibles_f)
            self.ir = pickle.load(self.varibles_f)
            self.tr = pickle.load(self.varibles_f)
            self.inpr = pickle.load(self.varibles_f)
            self.outr = pickle.load(self.varibles_f)
            self.sc = pickle.load(self.varibles_f)
            self.e = pickle.load(self.varibles_f)
            self.s = pickle.load(self.varibles_f)
            self.r = pickle.load(self.varibles_f)
            self.ien = pickle.load(self.varibles_f)
            self.fgi = pickle.load(self.varibles_f)
            self.fgo = pickle.load(self.varibles_f)
    def update_ram_table(self):
        index = self.tableWidget.model().index(self.pc.word, 1)
        self.tableWidget.scrollTo(index)
        self.tableWidget.selectRow(self.pc.word)
        
        if self.init_:
            for i in range(4096):
                self.tableWidget.setItem(i,1,QTableWidgetItem(str(hex(self.ram.read(i)))[2:].zfill(4)))
                
    def update_le_text(self):
        if self.init_:
            self.ar_le.setText(str(hex(self.ar.word))[2:].zfill(self.ar.bits // 4))
            self.pc_le.setText(str(hex(self.pc.word))[2:].zfill(self.pc.bits // 4))
            self.dr_le.setText(str(hex(self.dr.word))[2:].zfill(self.dr.bits // 4))
            self.ac_le.setText(str(hex(self.ac.word))[2:].zfill(self.ac.bits // 4))
            self.ir_le.setText(str(hex(self.ir.word))[2:].zfill(self.ir.bits // 4))
            self.tr_le.setText(str(hex(self.tr.word))[2:].zfill(self.tr.bits // 4))
            self.inpr_le.setText(str(hex(self.inpr.word))[2:].zfill(self.inpr.bits // 4))
            self.outr_le.setText(str(hex(self.outr.word))[2:].zfill(self.outr.bits // 4))
            self.sc_le.setText(str(hex(self.sc.word))[2:].zfill(self.sc.bits // 4))
            self.e_le.setText(str(hex(self.e.word))[2:])
            self.s_le.setText(str(hex(self.s.word))[2:])
            self.r_le.setText(str(hex(self.r.word))[2:])
            self.ien_le.setText(str(hex(self.ien.word))[2:].zfill(self.ien.bits // 4))
            self.fgi_le.setText(str(hex(self.fgi.word))[2:].zfill(self.fgi.bits // 4))
            self.fgo_le.setText(str(hex(self.fgo.word))[2:].zfill(self.fgo.bits // 4))
    def update_ins(self):
        if self.init_:
            if self.i < len(self.log_f):
                self.ins_le.setText(self.log_f[self.i])
                self.i = self.i + 1
            if  self.i == len(self.log_f):
                self.init_ = False     
                if hasattr(self,'timer'):
                    self.timer.stop()  
                    print('Yes') 
        else:
            if hasattr(self,'timer'):
                self.timer.stop()  
    def init(self):

        self.init_ = True
        self.i = 0
        self.log_f = open('log.txt','r')
        self.log_f = self.log_f.read().split('\n')[:-1]
        self.varibles_f = open('varibles.pickle','rb')
        self.update_params()
        self.update_ram_table()
        self.update_le_text()
        self.update_ins()





           
               

    @pyqtSlot()
    def assemble_clicked(self):
        # copy the content of code_tb to a variable
        # write any exception message in log_le
        try:
            code = self.code_tb.toPlainText()
            computer = create_computer(code)
            self.comp = computer
            computer.log_f.close()
            computer.varibles_f.close()
            self.init()
            self.log_tb.setPlainText('Assembled successfully')
        except Exception as e:
            # how to write the error message in log_tb (QPlainTextEdit)
            self.log_tb.setPlainText(str(e))    

    @pyqtSlot()
    def help_clicked(self):
        QMessageBox.question(self, 'Help', "Write your code in the left text box section\nThen push the assemble buttom\n Use next & play buttom to step instructons", QMessageBox.Ok, QMessageBox.Ok)
    @pyqtSlot()
    def next_clicked(self):
        self.update_params()
        self.update_ram_table()
        self.update_le_text()
        self.update_ins()
    @pyqtSlot()
    def play_clicked(self):
        # in this function you should call next_clicked() every 0.1 seconds
        # you should stop the loop when the program is finished
        # you should also stop the loop when the user clicks on the stop button
        # code
        self.timer = QTimer()
        self.timer.timeout.connect(self.next_clicked)
        self.timer.start(1000//int(self.speed_value))

        
        
    @pyqtSlot()
    def stop_clicked(self):
        self.timer.stop()
    @pyqtSlot()
    def speed_changed(self):
        # how to get the value of slider(speed_sl) 


        self.speed_value = self.speed_sl.value()

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())

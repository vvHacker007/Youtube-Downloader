from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import pytube
import video_downloader
import file_converter
import lxml
from lxml import etree
import urllib
import os



  
class Ui_MainWindow(QtWidgets.QWidget):
    def setupUi(self, MainWindow):
        MainWindow.resize(1280, 1024)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
  
        self.pushButton1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton1.setGeometry(QtCore.QRect(70,50,180,30))

        self.pushButton2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton2.setGeometry(QtCore.QRect(70,120,180,30))

        self.pushButton3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton3.setGeometry(QtCore.QRect(55,190,210,30))
  
        # For displaying confirmation message along with user's info. 
        self.label = QtWidgets.QLabel(self.centralwidget)    
        self.label.setGeometry(QtCore.QRect(170, 40, 201, 111))
  
        # Keeping the text of label empty initially.       
        self.label.setText("")     
  
        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
  
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton1.setText(_translate("MainWindow", "Download YouTube Videos"))
        self.pushButton1.clicked.connect(self.input_video_link)

        self.pushButton2.setText(_translate("MainWindow", "Download YouTube Playlist"))
        self.pushButton2.clicked.connect(self.input_playlists_link)

        self.pushButton3.setText(_translate("MainWindow", "Download YouTube Videos in MP3"))
        self.pushButton3.clicked.connect(self.input_video_mp3_link)
          
    def input_video_link(self):
        link, done1 = QtWidgets.QInputDialog.getText(self, 'Input Dialog', 'Enter the link:') 
  
        qualities = ['low', 'medium', 'high', 'very high']
        quality, done2 = QtWidgets.QInputDialog.getItem(self, 'Input Dialog', 'Select Video Quality:', qualities)
  
        if done1 and done2:
            video_title = video_downloader.download_video(link,quality)
            MainWindow.resize(900, 450)
            self.label.setGeometry(QtCore.QRect(150, 150, 450, 450))
            self.label.setText('Video Downloaded Successfully\nName: ' +str(video_title)+'\nQuality: '+str(quality)+'\nVideo Link: '+str(link))   
            # Hide the pushbutton after inputs provided by the use.
            self.pushButton1.hide()   
            self.pushButton2.hide()
            self.pushButton3.hide() 
    
    
    def input_playlists_link(self):
        link, done1 = QtWidgets.QInputDialog.getText(self, 'Input Dialog', 'Enter the link:') 
        qualities = ['low', 'medium', 'high', 'very high']
        quality, done2 = QtWidgets.QInputDialog.getItem(self, 'Input Dialog', 'Select Video Quality:', qualities)
        if done1 and done2:
            videos_title = video_downloader.download_playlist(link, quality)
            MainWindow.resize(900, 900)
            self.label.setGeometry(QtCore.QRect(150, 150, 450, 450))
            self.label.setText('Video Downloaded Successfully\nName: ' +str(videos_title)+'\nQuality'+str(quality)+'\nVideo Link'+str(link))   
            self.pushButton1.hide()   
            self.pushButton2.hide()
            self.pushButton3.hide()

    def input_video_mp3_link(self):
        link, done1 = QtWidgets.QInputDialog.getText(self, 'Input Dialog', 'Enter the link:') 
        qualities =['low', 'medium', 'high', 'very high']
        quality, done2 = QtWidgets.QInputDialog.getItem(self, 'Input Dialog', 'Select Video Quality:', qualities)
  
        if done1 and done2:
            filename = video_downloader.download_video(link, 'low')
            file_converter.convert_to_mp3(filename)
            os.remove(filename)
            MainWindow.resize(900, 450)
            self.label.setGeometry(QtCore.QRect(150, 150, 450, 450))
            self.label.setText('Video Downloaded Successfully!!\nName: ' +str(filename)+'\nQuality'+str(quality)+'\nVideo Link'+str(link))   
            self.pushButton1.hide()   
            self.pushButton2.hide()
            self.pushButton3.hide()     
                
               
               
if __name__ == "__main__": 
    app = QtWidgets.QApplication(sys.argv) 
    MainWindow = QtWidgets.QMainWindow() 
    ui = Ui_MainWindow() 
    ui.setupUi(MainWindow) 
    MainWindow.show()
    sys.exit(app.exec_()) 
from PySide2.QtWidgets import *
from ui_main import Ui_MainWindow
import sys
from pytube import YouTube, Playlist

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Youtube Downloader")
        self.btn_donwload.clicked.connect(self.yt_downloader)


    def yt_downloader(self):

        video_url = self.txt_link.text()
        if self.rb_video.isChecked():
            YouTube(video_url).streams.first().download()

            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("Audio baixado com sucesso!")
            msg.exec_()

        elif self.rb_audio.isChecked():
            YouTube(video_url).streams.filter(only_audio=True).first().download()

            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("Audio baixado com sucesso!")
            msg.exec_()
        elif self.rb_playlist.isChecked():
            play = Playlist(video_url)

            for video in play.videos:
                video.streams.first().download()

            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("Playlist baixada com sucesso!")
            msg.exec_()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()
import sys
import os
import threading
import yt_dlp
import re
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QFileDialog, QComboBox, QProgressBar

class YouTubeDownloader(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("YouTube Downloader")
        self.setGeometry(500, 200, 400, 300)

        layout = QVBoxLayout()

        self.url_label = QLabel("YouTube URL:")
        layout.addWidget(self.url_label)

        self.url_input = QLineEdit()
        layout.addWidget(self.url_input)

        self.quality_label = QLabel("Select Quality:")
        layout.addWidget(self.quality_label)

        self.quality_combo = QComboBox()
        self.quality_combo.addItems(["Best", "1080p", "720p", "Audio (MP3)"])
        layout.addWidget(self.quality_combo)

        self.select_button = QPushButton("Select Download Folder")
        self.select_button.clicked.connect(self.select_folder)
        layout.addWidget(self.select_button)

        self.download_button = QPushButton("Download")
        self.download_button.clicked.connect(self.start_download)
        layout.addWidget(self.download_button)

        self.progress_bar = QProgressBar()
        layout.addWidget(self.progress_bar)

        self.status_label = QLabel("")
        layout.addWidget(self.status_label)

        self.setLayout(layout)
        self.download_folder = os.getcwd()

    def select_folder(self):
        folder = QFileDialog.getExistingDirectory(self, "Select Folder")
        if folder:
            self.download_folder = folder

    def start_download(self):
        url = self.url_input.text()
        quality = self.quality_combo.currentText()
        if url:
            self.status_label.setText("Downloading...")
            threading.Thread(target=self.download_video, args=(url, quality), daemon=True).start()

    def download_video(self, url, quality):
        ydl_opts = {
            'outtmpl': os.path.join(self.download_folder, '%(title)s.%(ext)s'),
            'progress_hooks': [self.update_progress],
        }

        if quality == "Audio (MP3)":
            ydl_opts['format'] = 'bestaudio/best'
            ydl_opts['postprocessors'] = [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }]
        elif quality == "1080p":
            ydl_opts['format'] = 'bestvideo[height<=1080]+bestaudio/best'
        elif quality == "720p":
            ydl_opts['format'] = 'bestvideo[height<=720]+bestaudio/best'
        else:
            ydl_opts['format'] = 'best'

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

        self.status_label.setText("Download Complete!")

    def update_progress(self, d):
        if d['status'] == 'downloading':
            percent = d.get('_percent_str', '0%')
            # Remove ANSI codes and %
            percent = re.sub(r'\x1b\[[0-9;]*m', '', percent).replace('%', '').strip()
            try:
                self.progress_bar.setValue(int(float(percent)))  # convert to float, then int
            except ValueError:
                pass

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = YouTubeDownloader()
    window.show()
    sys.exit(app.exec_())

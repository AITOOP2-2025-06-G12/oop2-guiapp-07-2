import sys
from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout
from button_record import button_record
from button_transcribe import button_transcribe
from button_save import button_save

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("ボタンだけのGUI")
        self.setGeometry(100, 100, 300, 200)

        layout = QVBoxLayout()

        # ボタンを作成
        self.button_record = QPushButton("録音")
        self.button_transcribe = QPushButton("文字起こし")
        self.button_save = QPushButton("保存")

        # ボタンをレイアウトに追加
        layout.addWidget(self.button_record)
        layout.addWidget(self.button_transcribe)
        layout.addWidget(self.button_save)

        self.setLayout(layout)

        # ボタンにイベントを設定（例としてクリック時に print）
        self.button_record.clicked.connect(button_record)
        self.button_transcribe.clicked.connect(button_transcribe)
        self.button_save.clicked.connect(button_save)

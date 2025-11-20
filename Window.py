import sys
from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout

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
        self.button_record.clicked.connect(lambda: print("録音ボタンが押されました"))
        self.button_transcribe.clicked.connect(lambda: print("文字起こしボタンが押されました"))
        self.button_save.clicked.connect(lambda: print("保存ボタンが押されました"))


from PySide6.QtWidgets import QWidget, QPushButton, QVBoxLayout
from button_record import ButtonRecord
from button_transcribe import ButtonTranscribe
from button_save import ButtonSave

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("ボタンだけのGUI")
        self.setGeometry(100, 100, 300, 200)

        # ボタンクラスのインスタンス
        self.recorder = ButtonRecord()
        self.transcriber = ButtonTranscribe()
        self.saver = ButtonSave()

        # 文字起こし結果を保持
        self.transcribed_text = ""

        # レイアウト
        layout = QVBoxLayout()

        # ボタン
        self.button_record = QPushButton("録音")
        self.button_transcribe = QPushButton("文字起こし")
        self.button_save = QPushButton("保存")

        layout.addWidget(self.button_record)
        layout.addWidget(self.button_transcribe)
        layout.addWidget(self.button_save)
        self.setLayout(layout)

        # シグナル接続（重要：lambda を使って bool を渡さない）
        self.button_record.clicked.connect(lambda: self.recorder.button_record())
        self.button_transcribe.clicked.connect(lambda: self.on_transcribe_clicked())
        self.button_save.clicked.connect(lambda: self.on_save_clicked())

    def on_transcribe_clicked(self):
        self.transcribed_text = self.transcriber.transcribe_audio()

    def on_save_clicked(self):
        if self.transcribed_text:
            self.saver.outputTextFile(self.transcribed_text)
        else:
            print("文字起こしが行われていません。")

import sys
from PySide6.QtWidgets import QApplication
from Window import MainWindow  # 上記ファイルをインポート

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
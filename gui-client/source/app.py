from PySide2.QtCore import QTimer, QUrl
from PySide2.QtGui import QIcon
from PySide2.QtWebEngineWidgets import QWebEngineView
from PySide2.QtWidgets import QApplication, QMainWindow


def load_config(filename: str):
    from json import load
    with open(filename, 'r') as file:
        config = load(file)
    return config


def reload():
    window.webEngineView.load(QUrl(window.config['web-app-url']))


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        from os import getenv
        self.config = load_config(getenv('CONFIG_PATH', 'config/app.json'))

        self.setWindowTitle(self.config['window-title'])
        self.setMinimumSize(self.config['minimum-width'], self.config['minimum-height'])
        self.setWindowIcon(QIcon(f"{self.config['static-dir']}/flavicon.ico"))

        self.webEngineView = QWebEngineView()
        self.setCentralWidget(self.webEngineView)
        self.webEngineView.load(QUrl(self.config['web-app-url']))


if __name__ == '__main__':
    from sys import exit

    app = QApplication(['', '--no-sandbox'])
    window = MainWindow()

    timer = QTimer()
    timer.setInterval(window.config["reload-interval"])
    timer.timeout.connect(reload)
    timer.start()

    window.resize(window.screen().availableGeometry().width() * 2 / 3,
                  window.screen().availableGeometry().height() * 2 / 3)
    window.show()

    exit(app.exec_())

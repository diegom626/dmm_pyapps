#!/usr/bin/env python
import sys
from PyQt5.QtWebEngineWidgets import QWebEnginePage
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QUrl
from bs4 import BeautifulSoup


class Client(QWebEnginePage):
    def __init__(self, url):
        self.app = QApplication(sys.argv)
        QWebEnginePage.__init__(self)
        self.html = ''
        self.loadFinished.connect(self._loadFinished)
        self.load(QUrl(url))
        self.app.exec_()

    def _loadFinished(self):
        self.html = self.toHtml(self.Callable)
        print('Carga completa')

    def Callable(self, html_str):
        self.html = html_str
        self.app.quit()


link = Client("https://www.correos.cl/SitePages/seguimiento/seguimiento.aspx?envio=RC310424679DE")
soup = BeautifulSoup(link.html, 'html.parser')
tracking = soup.find("table", {"class": "tracking"})
print(tracking)

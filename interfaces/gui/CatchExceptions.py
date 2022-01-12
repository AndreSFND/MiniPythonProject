import sys
from PyQt5 import QtWidgets

# Catches all exceptions and print them into a message box
def catch_exceptions(t, val, tb):
    QtWidgets.QMessageBox.critical(None, 'An error ocurred', '{}'.format(val))
    
sys.excepthook = catch_exceptions
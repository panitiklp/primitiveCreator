from PySide6 import QtCore, QtGui, QtWidgets
from shiboken6 import wrapInstance
import maya.OpenMayaUI as omui
import os

ICON_PATH = os.path.join(os.path.dirname(__file__), 'icons').replace('\\', '/')
print(ICON_PATH)

class PrimitiveCreatorDialog(QtWidgets.QDialog):
	def __init__(self, parent=None):
		super().__init__(parent)

		self.resize(300, 300)
		self.setWindowTitle('😊 Primitive Creator')

		self.mainLayout = QtWidgets.QVBoxLayout()
		self.setLayout(self.mainLayout)

		self.primListWidget = QtWidgets.QListWidget()
		self.primListWidget.setIconSize(QtCore.QSize(30,30))
		self.mainLayout.addWidget(self.primListWidget)

		self.buttonLayout = QtWidgets.QHBoxLayout()
		self.mainLayout.addLayout(self.buttonLayout)

		self.createButton = QtWidgets.QPushButton('🌻Create')
		self.cancelButton = QtWidgets.QPushButton('❌Cancel')
		self.buttonLayout.addWidget(self.createButton)
		self.buttonLayout.addWidget(self.cancelButton)

		self.initPrimitiveItems()

	def initPrimitiveItems(self):
		primitives = ['cone', 'cube', 'sphere', 'torus']
		for prim in primitives:
			item = QtWidgets.QListWidgetItem(prim)
			item.setIcon(QtGui.QIcon(os.path.join(ICON_PATH, '{0}.png'.format(prim))))
			self.primListWidget.addItem(item)

def run():
	global ui
	try:
		ui.close()
	except:
		pass

	ptr = wrapInstance(int(omui.MQtUtil.mainWindow()), QtWidgets.QWidget)
	ui = PrimitiveCreatorDialog(parent=ptr)
	ui.show()
"""
Le but de l'exercice est d'afficher le mot 'Bonjour'
a l'aide de la methode 'afficher_mot' quand on clique sur
le bouton 'Print Bonjour!' et d'afficher 'Au revoir' quand
on clique sur le bouton 'Print Au Revoir!'
"""

from PySide6 import QtWidgets


class MainUi(QtWidgets.QWidget):
	def __init__(self):
		super(MainUi, self).__init__()
		
		self.setWindowTitle('Printer')

		main_layout = QtWidgets.QHBoxLayout(self)
		button = QtWidgets.QPushButton('Print Bonjour!')
		button2 = QtWidgets.QPushButton('Print Au revoir!')
		main_layout.addWidget(button)
		main_layout.addWidget(button2)

		button.clicked.connect(lambda: self.afficher_mot('Bonjour'))
		button2.clicked.connect(lambda: self.afficher_mot('Au revoir'))

	def afficher_mot(self, mot):
		print(mot)

if __name__ == '__main__':
	app = QtWidgets.QApplication([])
	win = MainUi()
	win.show()
	app.exec()

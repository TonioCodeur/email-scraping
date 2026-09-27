"""
Le but de l'exercice est d'afficher le resultat
de l'addition de la case 'a' avec la case 'b' dans
la case 'c'.

Pour afficher du texte a l'interieur de la case 'c'
vous aurez besoin d'utiliser: c.setText('texte a afficher')
"""


from PySide6 import QtWidgets


class MainUi(QtWidgets.QWidget):
	def __init__(self):
		super(MainUi, self).__init__()
		
		self.setWindowTitle('Calculatrice')

		main_layout = QtWidgets.QHBoxLayout(self)
		button = QtWidgets.QPushButton('Calcul')
		a = QtWidgets.QLineEdit('1')
		b = QtWidgets.QLineEdit('5')
		label_plus = QtWidgets.QLabel('+')
		c = QtWidgets.QLineEdit()
		label_egal = QtWidgets.QLabel('=')
		main_layout.addWidget(a)
		main_layout.addWidget(label_plus)
		main_layout.addWidget(b)
		main_layout.addWidget(label_egal)
		main_layout.addWidget(c)
		main_layout.addWidget(button)

		c.setText('...')

		button.clicked.connect(lambda: c.setText(str(int(a.text()) + int(b.text()))))

if __name__ == '__main__':
	app = QtWidgets.QApplication([])
	win = MainUi()
	win.show()
	app.exec()

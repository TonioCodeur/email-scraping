import sys

from PySide6 import QtWidgets

couleur_bouton = (255, 0, 0)
couleur_bouton_dict = {'rouge': 255, 'vert': 0, 'bleu': 0}

class InterfaceBasique(QtWidgets.QPushButton):
	def __init__(self, text='Clique!'):
		super(InterfaceBasique, self).__init__(text)

		# self.setStyleSheet('background-color: rgb({},{},{})'.format(couleur_bouton[0], couleur_bouton[1], couleur_bouton[2]))
		# self.setStyleSheet('background-color: rgb({},{},{})'.format(*couleur_bouton))
		self.setStyleSheet('background-color: rgb({rouge},{vert},{bleu})'.format(**couleur_bouton_dict))
		self.show()


app = QtWidgets.QApplication([])
bouton = InterfaceBasique()
bouton.show()
sys.exit(app.exec())

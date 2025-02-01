from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import Qt
from random import shuffle

card_width, card_height = 600, 500
win_card = QWidget()
win_card.resize(card_width, card_height)
win_card.move(300,300)
win_card.setWindowTitle('Memory Card')

btn_Menu = QPushButton('Menu')
btn_Sleep = QPushButton('Widpochinok')
bot_Minutes = QSpinBox()
bot_Minutes.setValue(30)
btn_OK = QPushButton('Widpowisti')
lb_Question = QLabel('')

RadioGroupBox = QGroupBox("Warianti widpowidi")
RadioGroupBox = QButtonGroup()

rbtn_1 = QRadioButton('')
rbtn_2 = QRadioButton('')
rbtn_3 = QRadioButton('')
rbtn_4 = QRadioButton('')

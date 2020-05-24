# Botshelo Nokoane
# OXO Game GUI
# 17/05/2020

import sys  
import os
import qstylizer.style
from PyQt5.QtWidgets import *  # imports pyqt modules
from PyQt5.QtCore import *  # imports pyqt modules
from PyQt5.QtGui import *  # imports pyqt modules

class OXO_GUI(QWidget):  # Stock inherits from the Qwidget
    def __init__(self, parent=None):  # parent defines parent widget
        QWidget.__init__(self, parent)  # Super class instuctor
        self.setWindowTitle("O X O Client")  # Set window title
        self.setGeometry(390, 90, 610, 500)  # setting window geometries
        self.setPalette(QPalette(QColor("#498f7f")))
        
        # set the X and O Icons
        self.oIcon = QIcon("nought.gif")
        self.xIcon = QIcon("cross.gif")
        
        # set window icon and color
        icon = QIcon()
        icon.addPixmap(QPixmap("game_icon.png"))
        self.setWindowIcon(icon)  # set window icon

        # create header 
        self.header = QLabel("TenElevenGames OXO")
        self.header.setFont(QFont("Arial",22,5))
        self.header.setAlignment(Qt.AlignCenter)
        
        # create server button label
        self.server_label = QLabel("server:")
        self.server_label.setFont(QFont("Monospace",13,5))
        self.server_lineEdit = QLineEdit()
        self.server_lineEdit.setFont(QFont("Monospace",13,5))
        self.server_lineEdit.setPlaceholderText("enter server") 
        self.connect_btn = QPushButton("connect")
        self.connect_btn.setFont(QFont("Monospace",13,5))
        
        # create game and message headers
        self.the_game_label = QLabel("-----The Game-----")
        self.the_game_label.setAlignment(Qt.AlignCenter)
        self.the_game_label.setFont(QFont("Monospace",13,5))
        self.messages_label = QLabel("-----Messages from the server-----")
        self.messages_label.setAlignment(Qt.AlignCenter)
        self.messages_label.setFont(QFont("Monospace",13,5))
        self.header_hbox = QHBoxLayout()
        self.header_hbox.addWidget(self.the_game_label)
        self.header_hbox.addWidget(self.messages_label)
        """ header hbox widget """
        self.header_hbox_widget = QWidget()
        self.header_hbox_widget.setLayout(self.header_hbox)
        
        # insert server label and buttons
        self.horizontal = QGridLayout()
        self.horizontal.addWidget(self.header,0,1,1,1)
        self.horizontal.addWidget(self.server_label,1,0)
        self.horizontal.addWidget(self.server_lineEdit,1,1)
        self.horizontal.addWidget(self.connect_btn,1,2)
        self.horizontal.setAlignment(Qt.AlignTop)  # align the grid layout at the top
        """ Horizontal QWidget  """
        self.horizontal_widget = QWidget()
        self.horizontal_widget.setLayout(self.horizontal)  
        
                
        # set up widget for Text message 
        self.server_messages = QTextEdit("valid move")  # the text set on this textedit is for display and will be removed moving on to the next assignment
        self.server_messages.setFont(QFont("Arial",13,5))
        self.server_messages.setStyleSheet("background-color: white")   
        self.server_messages.setReadOnly(True)
        
        # players character and score board display
        self.my_shape = QPushButton()
        self.my_shape.setText("")
        self.my_shape.setEnabled(True)
        self.my_shape.setFixedSize(50,50)
        self.my_shape.setIconSize(QSize(50,50))
        self.my_shape.setIcon(self.xIcon)  # the icon set on this push button is just for display and will be removed moving to the next assignment
        self.my_shape.setStyleSheet("background-color: white")
        
        self.my_shape_label = QLabel("My shape")
        self.my_shape_label.setEnabled(False)
        self.my_shape_label.setFont(QFont("Arial",15,5))
        self.score_label = QLabel("Score:")
        self.score_label.setFont(QFont("Arial",15,5))
        self.character_x = QLabel("Player X==>")
        self.character_x.setAlignment(Qt.AlignCenter)
        self.character_x.setFont(QFont("Arial",15,5))
        self.score_x = QLabel("7")
        self.score_x.setFont(QFont("Arial",15,5))
        self.character_y = QLabel("Player O==>")
        self.character_y.setAlignment(Qt.AlignCenter)
        self.character_y.setFont(QFont("Arial",15,5))
        self.score_y = QLabel("4")
        self.score_y.setFont(QFont("Arial",15,5))
        
        # create score board and players character layout
        self.player_grid = QGridLayout()
        self.player_grid.addWidget(self.my_shape_label,0,0)
        self.player_grid.addWidget(self.my_shape,0,1)
        self.player_grid.addWidget(self.score_label,1,0)
        self.player_grid.addWidget(self.character_x,2,0)
        self.player_grid.addWidget(self.score_x,2,1)
        self.player_grid.addWidget(self.character_y,3,0)
        self.player_grid.addWidget(self.score_y,3,1)
        """ player_grid widget """
        self.player_grid_widget = QWidget()
        self.player_grid_widget.setLayout(self.player_grid)
        
        # vertical box for server messages and player_grid
        self.vertical = QVBoxLayout()
        self.vertical.addWidget(self.server_messages)
        self.vertical.addWidget(self.player_grid_widget)
        """ vertcial widget """
        self.vertical_widget = QWidget()
        self.vertical_widget.setLayout(self.vertical)
        
        # create Gird board game for buttons
        self.board_game = QGridLayout()
        self.board_game.setContentsMargins(0,0,0,0)
        self.board_game.setSpacing(0)
        self.object_name, self.row = 0, 0
        while self.row <= 2:
            for self.column in range(3):
                self.button = QToolButton()
                self.button.setText("")
                self.button.setFixedSize(100,100)
                self.button.setObjectName(str(self.object_name))   
                self.button.setStyleSheet("background: white")
                self.button.setIconSize(QSize(100, 100))
                if self.object_name%2 == 0:
                    self.button.setIcon(self.xIcon)
                else:
                    self.button.setIcon(self.oIcon) 
                self.board_game.addWidget(self.button, self.row, self.column, 1, 1)
                self.object_name += 1  # increment each object name
            self.row += 1
        """ Board game QWidget """
        self.board_game_widget = QWidget()
        self.board_game_widget.setLayout(self.board_game)  
        
        # create new_game and exit button
        self.new_game = QPushButton("new game")
        self.new_game.setFixedSize(90,20)
        self.new_game.setFont(QFont("Monospace",13,5))
        self.exit = QPushButton("exit")
        self.exit.setFixedSize(90,20)
        self.exit.setFont(QFont("Monospace",13,5))
        
        self.grid_buttons = QGridLayout()
        self.grid_buttons.addWidget(self.new_game,0,3)
        self.grid_buttons.addWidget(self.exit,0,4)
        """ grid_buttons QWidget """
        self.grid_buttons_widget = QWidget()
        self.grid_buttons_widget.setLayout(self.grid_buttons)
        
        # HBox for the board game and text messages
        self.board_message = QHBoxLayout()
        self.board_message.addWidget(self.board_game_widget)
        self.board_message.setSpacing(7)
        self.board_message.addWidget(self.vertical_widget)  # Add a QWidget containing the self.log and a players information
        """ baord_message QWidget """
        self.board_message_widget = QWidget()
        self.board_message_widget.setLayout(self.board_message)  #
        
        # Insert widgets into vertical box
        self.main_layout = QVBoxLayout()
        self.main_layout.addWidget(self.horizontal_widget)
        self.main_layout.addWidget(self.header_hbox_widget)
        self.main_layout.addWidget(self.board_message_widget)
        self.main_layout.addWidget(self.grid_buttons_widget)
        self.main_layout_widget = QWidget()
        self.main_layout_widget.setLayout(self.main_layout)
        
        # set main UI Layout
        self.ui = QVBoxLayout()
        self.ui.addWidget(self.main_layout_widget)
        self.setLayout(self.ui)

        # Style the widgets on the main window
        css = qstylizer.style.StyleSheet()
        
        # Style the Button games
        css.QToolButton.setValues(
            border="2px solid grey",
            marginLeft = "2px",
            marginRight = "2px",
            marginBottom = "2px",
            borderRadius="7px",
        )
        
        # style the Push Button
        css.QPushButton.pressed.setValues(
            border="2px solid black"
        )
        
        # Style the Button games
        css.QToolButton.pressed.setValues(
            border="3px solid black",
            padding="5px",
        )
        
        # style the Text Edit
        css.QTextEdit.setValues(
            borderRadius="7px",
            marginLeft = "2px",
            border="2px solid grey",
        )
        
        # style the Q labels
        css.QLabel.setValues(
            color = "black",
            marginLeft="6px"
        )
        
        # style the QWidget
        css.QWidget.setValues(
            backgroundColor="#5ce0c2",
            borderRadius="10px"
        )
        
        # style the connect button
        css.QPushButton.setValues(
            border="2px solid gray",
            paddingLeft="2px",
            paddingRight="2px"
        )
        
        css.QLineEdit.setValues(
            border="2px solid gray",
            paddingLeft="2px",
            paddingRight="2px"
        )
        
        self.main_layout_widget.setStyleSheet(css.toString()) # set the style sheet
        
        self.allButtons = self.board_game_widget.findChildren(QToolButton)
        for button in self.allButtons:
            button.setStyleSheet("background: white")
            
def run_app():
    app = QApplication(sys.argv)  # creates necessary app object
    window = OXO_GUI()  # Instance of Demo class
    window.show()   # Show instance of Demo
    sys.exit(app.exec_())  # start executing main app event loop and return value to the exit system

if __name__ == "__main__":
    run_app()




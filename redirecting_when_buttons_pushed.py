import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QHBoxLayout, QLabel, QLineEdit, QTextEdit
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt

class ContentWindow(QMainWindow):
    def __init__(self, title, content):
        super().__init__()
        self.setWindowTitle(title)
        self.setFixedSize(800, 600)

        # Layout for the content window
        layout = QVBoxLayout()
        label = QLabel(content, self)
        label.setAlignment(Qt.AlignCenter)
        layout.addWidget(label)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('ΚΑΛΩΣ ΗΡΘΕΣ "ΟΝΟΜΑ ΧΡΗΣΤΗ"')

        # Vertical menu bar
        self.menu_layout = QVBoxLayout()
        self.add_menu_button('ΑΡΧΙΚΗ', 'Home Page', 'This is the home page content.')
        self.add_menu_button('CHAT', 'Chat Page', 'This is the chat page content.')
        self.add_menu_button('ΒΟΗΘΕΙΑ', 'Help Page', 'This is the help page content.')
        self.add_menu_button('ΙΑΤΡΙΚΟ ΠΡΟΦΙΛ', 'Medical Profile Page', 'This is the medical profile page content.')
        self.add_menu_button('ΠΟΡΤΟΦΟΛΙ ΥΓΕΙΑΣ', 'Health Wallet Page', 'This is the health wallet page content.')
        self.add_menu_button('ΕΠΙΚΟΙΝΩΝΙΑ', 'Contact Page', 'This is the contact page content.')
        exit_button = QPushButton('ΕΞΟΔΟΣ')
        exit_button.clicked.connect(self.close_application)
        self.menu_layout.addWidget(exit_button)
        self.menu_layout.addStretch()  # Add stretch to push menu items to the top

        # Create a widget to contain the menu
        self.menu_widget = QWidget()
        self.menu_widget.setLayout(self.menu_layout)

        # Set the menu widget's minimum width to cover 1/5 of the window
        menu_width = self.frameGeometry().width() // 5
        self.menu_widget.setMinimumWidth(menu_width)

        # Set background color of menu widget to light green
        self.menu_widget.setStyleSheet("background-color: #CDEAC0;")

        # Content layout
        content_layout = QVBoxLayout()

        # Greeting message
        greeting_label = QLabel('Welcome, ΟΝΟΜΑ ΧΡΗΣΤΗ!', self)
        greeting_label.setAlignment(Qt.AlignCenter)
        greeting_label.setStyleSheet("font-size: 20px; font-weight: bold;")
        content_layout.addWidget(greeting_label)

        # Two boxes at the bottom center
        bottom_layout = QHBoxLayout()
        box1 = QLineEdit(self)
        box2 = QTextEdit(self)
        box1.setMinimumSize(200, 50)
        box2.setMinimumSize(200, 50)
        bottom_layout.addWidget(box1)
        bottom_layout.addWidget(box2)
        content_layout.addLayout(bottom_layout)

        # Combine menu and content layouts using QHBoxLayout
        main_layout = QHBoxLayout()
        main_layout.addWidget(self.menu_widget)
        main_layout.addLayout(content_layout)

        main_widget = QWidget()
        main_widget.setLayout(main_layout)
        self.setCentralWidget(main_widget)

        # Set the fixed size of the window
        self.setFixedSize(1200, 600)  # Adjust the width and height as needed

    def add_menu_button(self, text, window_title, window_content):
        button = QPushButton(text, self)
        button.clicked.connect(lambda: self.open_content_window(window_title, window_content))
        self.menu_layout.addWidget(button)

    def open_content_window(self, title, content):
        self.content_window = ContentWindow(title, content)
        self.content_window.show()

    def close_application(self):
        QApplication.instance().quit()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

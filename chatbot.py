# importing the necessary libraries
import wikipedia
from PyQt5.QtWidgets import QTextEdit,QApplication, QLineEdit,QPushButton, QVBoxLayout, QWidget, QLabel
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
import sys

class WikipediaChatbot(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Wikipedia Chatbot")
        self.setGeometry(100, 100, 600, 400)

        # basic layout 
        
        self.label = QLabel("Enter your question")
        self.input_field =QLineEdit()
        self.button = QPushButton("Search")
        self.output = QTextEdit()
        self.output.setReadOnly(True)
        #setting width of the search button
        self.button.setFixedWidth(120)
        #layouts 
        
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.label)
        self.layout.addWidget(self.input_field)
        # aligning the button to the center
        self.layout.addWidget(self.button, alignment=Qt.AlignHCenter)
        
        self.layout.addWidget(self.output)
        self.setLayout(self.layout)
        
        #setting the font
        font = QFont()
        font.setPointSize(13)
        self.label.setFont(font)
        self.input_field.setFont(font)
        self.button.setFont(font)
        self.output.setFont(font)
        # Setting background color
        self.setStyleSheet("background-color: black;")
        self.label.setStyleSheet("color: white;")
        self.input_field.setStyleSheet("background-color: white; color: black;")
        self.button.setStyleSheet("background-color: #4CAF50; color: white;")
        self.output.setStyleSheet("background-color: white; color: black;") 
        
        # linking the button with the search function
        self.button.clicked.connect(self.search_wikipedia)
        
    def search_wikipedia(self):
        question = self.input_field.text().strip()
            
        if not question:
                self.output.setText('Please enter a question.')
        else:
            try:
                    #searching for the question on wikipedia
                answer = wikipedia.summary(question)
                self.output.setText(answer)
            except wikipedia.exceptions.DisambiguationError as e:
                self.output.setText(f"Disambiguation error: {e.options}")
            except wikipedia.exceptions.PageError:
                self.output.setText("Page not found. Please try another question.")
                    
# Running the application
if __name__ == "__main__":
    app =QApplication(sys.argv)
    chatbot = WikipediaChatbot()
    chatbot.show()
    sys.exit(app.exec_())

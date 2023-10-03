import sys
import PyQt5
import flask
import cx_Oracle
# from PyQt5.QtCore import *
# from PyQt5.QtGui import *
# from PyQt5.QtWidgets import *

# PyQt5 UI
class CreateUserWindow(pyqt5.QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        # UI elements
        self.username_label = pyqt5.QtWidgets.QLabel("Username:")
        self.username_input = pyqt5.QtWidgets.QLineEdit()
        self.password_label = pyqt5.QtWidgets.QLabel("Password:")
        self.password_input = pyqt5.QtWidgets.QLineEdit()
        self.create_user_button = pyqt5.QtWidgets.QPushButton("Create User")
        self.view_users_button = pyqt5.QtWidgets.QPushButton("View Users")

        # Layout
        layout = pyqt5.QtWidgets.QVBoxLayout()
        layout.addWidget(self.username_label)
        layout.addWidget(self.username_input)
        layout.addWidget(self.password_label)
        layout.addWidget(self.password_input)
        layout.addWidget(self.create_user_button)
        layout.addWidget(self.view_users_button)

        self.setLayout(layout)

        # Connect button to create_user() function
        self.create_user_button.clicked.connect(self.create_user)
        self.view_users_button.clicked.connect(self.view_users)

    def create_user(self):
        # Get username and password from UI elements
        username = self.username_input.text()
        password = self.password_input.text()

        # Connect to Oracle database
        connection = cx_Oracle.connect("username", "password", "localhost:1521/XEPDB1")

        # Create user in database
        cursor = connection.cursor()
        cursor.execute("CREATE USER {} IDENTIFIED BY {}".format(username, password))

        # Commit changes
        connection.commit()

        # Close connection
        connection.close()

        # Display success message
        pyqt5.QtWidgets.QMessageBox.information(self, "Create User", "User {} created successfully!".format(username))

    def view_users(self):
        # Connect to Oracle database
        connection = cx_Oracle.connect("username", "password", "localhost:1521/XEPDB1")

        # Query all users in database
        cursor = connection.cursor()
        cursor.execute("SELECT username FROM users")

        # Get results
        users = cursor.fetchall()

        # Close connection
        connection.close()

        # Display users in UI
        user_list = pyqt5.QtWidgets.QListWidget()
        for user in users:
            user_list.addItem(user[0])

        # Add user list to layout
        layout = pyqt5.QtWidgets.QVBoxLayout()
        layout.addWidget(user_list)

        # Create new window to display user list
        user_list_window = pyqt5.QtWidgets.QMainWindow()
        user_list_window.setLayout(layout)

        # Show window
        user_list_window.show()

# Flask API
app = flask.Flask(__name__)

@app.route("/create_user", methods=["POST"])
def create_user():
    # Get username and password from request body
    username = flask.request.json["username"]
    password = flask.request.json["password"]

    # Connect to Oracle database
    connection = cx_Oracle.connect("username", "password", "localhost:1521/XEPDB1")

    # Create user in database
    cursor = connection.cursor()
    cursor.execute("CREATE USER {} IDENTIFIED BY {}".format(username, password))

    # Commit changes
    connection.commit()

    # Close connection
    connection.close()

    # Return success response
    return flask.jsonify({"success": True})

# PyQt5 and Flask connection
if __name__ == "__main__":
    app.run(debug=True)

    app_window = CreateUserWindow()
    app_window.show()

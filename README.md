﻿# Python-ChatApp
 A Basic ChatApp built using python, Flask-SocketIO, HTML, CSS and a little JavaScript

**Features**

- Real-time chat functionality using Flask-SocketIO

- Basic frontend with HTML, CSS, and JavaScript

- No database integration as the main focus of this project was on core Python and WebSockets.

**Installation**

Clone the repository:

git clone https://github.com/iamshubhp/Python-ChatApp.git
cd Python-ChatApp

Create and activate a virtual environment (optional but recommended):

python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate

Install dependencies:
pip install -r requirements.txt

**Running the Application**
gunicorn --worker-class eventlet -w 1 wsgi:app

**Tutorial Video**
you can check out the tutorial video by following this link and pictures are uploaded below.
https://github.com/user-attachments/assets/adc2d368-237f-4674-8b41-354dbfe076b2

**App Images**
![image](https://github.com/user-attachments/assets/2bb372bb-ce22-4b34-8a36-165110a5d7c1)

![image](https://github.com/user-attachments/assets/eaca5679-3062-4177-8173-41c5a3b1ec7d)

That is all thankyou for visiting! 

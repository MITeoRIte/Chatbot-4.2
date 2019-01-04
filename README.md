# Setup and Running of Chatbot 4.2

## Training files
1. Go to a folder which contains utf-8 text files that you plan to train the bot with, and copy the path of the folder the text files are stored in.

2. Go to `chatbot/polls/views.py` and replace the pathname in `os.listdir(pathname)` with the one you've copied previously.

## Run the Chatbot
1. Open Terminal and `cd` to the `chatbot` folder.

2. Run `python manage.py runserver`.

This trains the bot with the text files you have provided and runs the chatbot locally.

3. Open a browser and go to `localhost:8080/polls/newgetmail`

Tadah!! You have successfully ran the Django based Chatbot




# Modification of the Chatbot

## You can:

1. Train the chatbot with a larger dataset (with more text files)

2. Remove the Machine Learning Chatbot and replace it with your own (look at `views.py`)

3. Add/ Remove/ Modify links of the chatbot

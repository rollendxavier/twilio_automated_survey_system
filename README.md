# Twilio Automated Survey System
This is a simple Flask application that uses Twilio's Voice Response and Gather functionalities to conduct a survey over a phone call.

## Overview

The application consists of three main routes:

1. `/survey`: This is the entry point of the survey. The user is welcomed and given options to answer two questions or end the survey.
2. `/gather`: This route handles the user's input from the keypad. Depending on the input, it asks one of the two questions or ends the survey.
3. `/record`: This route handles the recording of the user's verbal response to the questions.

## How it Works

When a call is made to the Twilio number associated with this application, the `/survey` route is triggered. The user is welcomed and given three options, each corresponding to a digit they can press on their phone's keypad.

The `/gather` route is then triggered, which checks the digit pressed by the user. If the user presses '1' or '2', they are asked a question and their response is recorded. If the user presses '3', the survey ends.

The `/record` route handles the recording of the user's response. If a recording is received, the user is thanked and given options to return to the main menu, go to the second question, or retry if no answer was received.

## Running the Application

To run the application, simply execute the Python script. Ensure that Flask and Twilio's Python SDK are installed in your environment.

```python
python app.py
```
## Complete Reference
For a complete reference, please visit the Twilio Blog.

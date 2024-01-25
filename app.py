from flask import Flask, request, Response
from twilio.twiml.voice_response import VoiceResponse, Gather


app = Flask(__name__)


@app.route("/survey", methods=['GET', 'POST'])
def survey():
    response = VoiceResponse()
    gather = Gather(numDigits=1, action='/gather', timeout=10)
    gather.say("Welcome to our survey. Press 1 for question one, 2 for question two, or 3 to end the survey.")
    response.append(gather)
    response.redirect('/survey')
    return Response(str(response), mimetype='text/xml')


@app.route('/gather', methods=['GET', 'POST'])
def gather():
    response = VoiceResponse()
    if 'Digits' in request.values:
        choice = request.values['Digits']
        if choice == '1':
            response.say("Thank you for your response.")
            response.say("Question one: On a scale of 1 to 5, how would you rate our service?")
            response.record(maxLength=10, timeout=5, action='/record')
        elif choice == '2':
            response.say("Thank you for your response.")
            response.say("Question two: On a scale of 1 to 5, how likely are you to recommend us to a friend?")
            response.record(maxLength=10, timeout=5, action='/record')
        elif choice == '3':
            response.say("Thank you for participating in our survey.")
            response.hangup()
        else:
            response.say("Sorry, I didn't understand that choice.")
            response.redirect('/survey')
    return Response(str(response), mimetype='text/xml')


@app.route('/record', methods=['GET', 'POST'])
def record():
    response = VoiceResponse()
    if 'RecordingUrl' in request.values:
        response.say("Thank you for your response.")
        response.gather(numDigits=1, action='/gather', timeout=10)
        response.hangup()  # Hang up after saying thank you
    else:
        response.say("No recording received, please try again.")
        response.redirect('/gather')
    return Response(str(response), mimetype='text/xml')


app.run(debug=True)

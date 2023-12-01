from flask import Flask, render_template, request, jsonify
import speech_transcriber as transcribe
from vertex_ai_component import notify
import os 

app = Flask(__name__)
PROJECT_ID = "<YOUR PROJECT_ID>"

@app.route('/')
def index():
    return render_template('home.html')

@app.route("/process", methods = ["GET"])
def process_notify():
    file_destination = "<PATH>/input_{}.mp3".format(request.args.get("track"))
    print(f"Received File Destination: {file_destination}")

    transcibe_response = transcribe.transcribe_file_with_auto_punctuation(file_destination)
    
    transcribe_response_text = str()
    for result in transcibe_response.results:
        alternative = result.alternatives[0]
        transcribe_response_text += " " + alternative.transcript
    print(f"Transcribed Text: {transcribe_response_text}")

    notify_response = notify(transcribe_response_text, PROJECT_ID)
    print(f"Notify Response: {notify_response}")

    return jsonify({"content": notify_response})

if __name__ == '__main__':
    app.run(debug=True, port=8080, host='0.0.0.0')



from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/emotionDetector')
def emotionDetector():
    text_to_analyze = request.args.get("textToAnalyze")
    text = emotion_detector(text_to_analyze)
    if text['dominant_emotion'] is None:
        return "Invalid text! Please try again!."
    text = f"For the given statement, the system response is {text}."
    return text

app.run(host = '0.0.0.0', port = 5000)
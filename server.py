"""Module Docstring because it has to be here."""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/")
def render_index_page():
    """renders the index page"""
    return render_template('index.html')

@app.route("/emotionDetector")
def sent_detector():
    """sends the stuff to the detector"""
    text_to_analyse = request.args.get('textToAnalyse')
    response = emotion_detector(text_to_analyse)

    anger = response['anger']
    disgust = response['disgust']
    fear = response['fear']
    joy = response['joy']
    sadness = response['sadness']
    dominant_emotion = response['dominant_emotion']

    emotions = (anger, disgust, fear, joy, sadness, dominant_emotion)
    if emotions == 0:
        return None

    if dominant_emotion is None:
        return "Invalid input! Please try again."

    s1 = "For the given statement, the system response is 'anger': {emotions[0]},"
    s2 = "'disgust': {emotions[1]}, 'fear': {emotions[2]}, 'joy': {emotions[3]},"
    s3 = "and 'sadness': {emotions[4]}. The dominant emotion is {emotions[5]}."
    return s1 + " " + s2 + " " + s3

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

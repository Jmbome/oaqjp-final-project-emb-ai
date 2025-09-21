# server.py
import json
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector


app = Flask(__name__)

@app.route("/")
def render_index_page():
    """Renders the main index page."""
    return render_template('index.html')

@app.route("/emotionDetector")
def emotion_detector():
    """
    Handles GET requests to the emotionDetector endpoint.
    It takes text from the query parameters, runs it through the
    emotion_detector, and returns the formatted response.
    """
    text_to_analyze = request.args.get('textToAnalyze')
    
    # Check for empty text and return a specific message
    if not text_to_analyze:
        return "Invalid text! Please try again!."
    
    # Call the emotion detection function
    response = emotion_detector(text_to_analyze)
    
    # Check for an error response from the emotion_detector function
    if response is None:
        return "An error occurred during emotion detection."
        
    # Extract emotion scores and the dominant emotio
    anger_score = response['anger']
    disgust_score = response['disgust']
    fear_score = response['fear']
    joy_score = response['joy']
    sadness_score = response['sadness']
    dominant_emotion = response['dominant_emotion']
    
    # Check if a dominant emotion was detected
    if dominant_emotion is None:
        return f"Invalid text! Please try again!."
        
    # Format the output string as requested
    output_string = (
        f"For the given statement, the system response is 'anger': {anger_score}, "
        f"'disgust': {disgust_score}, 'fear': {fear_score}, 'joy': {joy_score}, "
        f"and 'sadness': {sadness_score}. The dominant emotion is {dominant_emotion}."
    )
    
    return output_string

if __name__ == "__main__":
    app.run(debug=True, port=5000)




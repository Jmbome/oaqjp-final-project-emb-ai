from flask import Flask, request, json, jsonify
import requests

app = Flask(__name__)

@app.route('/', methods=['POST'])
def emotion_detector(text_to_analyze):

    if not text_to_analyze:
        # Return dictionary with None values for blank entries
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }

    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = { "raw_document": { "text": text_to_analyze } }


    try:
        response = requests.post(url, headers=headers, json=input_json)

        # Check for bad status code (e.g., 400)
        if response.status_code == 400:
            return {
                'anger': None,
                'disgust': None,
                'fear': None,
                'joy': None,
                'sadness': None,
                'dominant_emotion': None
            }

        response.raise_for_status()

        # Convert the JSON response text into a Python dictionary
        response_dict = json.loads(response.text)

        # Extract the required set of emotions from the nested dictionary
        emotion_scores = response_dict['emotionPredictions'][0]['emotion']
            
        # Find the dominant emotion (key with the highest value).
        dominant_emotion = max(emotion_scores, key=emotion_scores.get)

        output_dict = {
                'anger': emotion_scores['anger'],
                'disgust': emotion_scores['disgust'],
                'fear': emotion_scores['fear'],
                'joy': emotion_scores['joy'],
                'sadness': emotion_scores['sadness'],
                'dominant_emotion': dominant_emotion
            }

        return output_dict

        ## python3 -m pip install requests ##

    except (requests.exceptions.RequestException, json.JSONDecodeError, KeyError, IndexError) as e:
            print(f"An error occurred: {e}")
            return {
                'anger': None,
                'disgust': None,
                'fear': None,
                'joy': None,
                'sadness': None,
                'dominant_emotion': None
            }
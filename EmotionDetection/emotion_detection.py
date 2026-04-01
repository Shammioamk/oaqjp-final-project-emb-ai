import requests
import json

def emotion_detector(text_to_analyse):
    """
    Sends the input text to the Watson Emotion Detection API
    and returns a dictionary with emotion scores and dominant emotion.
    """
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyse } }

    # Send POST request
    response = requests.post(url, json=myobj, headers=header)

    # Convert the response text to a dictionary
    resp_dict = json.loads(response.text)

    # Extract the first emotion prediction
    emotions = resp_dict['emotionPredictions'][0]['emotion']

    # Find the dominant emotion (highest score)
    dominant_emotion = max(emotions, key=emotions.get)

    # Return formatted dictionary
    return {
        'anger': emotions['anger'],
        'disgust': emotions['disgust'],
        'fear': emotions['fear'],
        'joy': emotions['joy'],
        'sadness': emotions['sadness'],
        'dominant_emotion': dominant_emotion
    }
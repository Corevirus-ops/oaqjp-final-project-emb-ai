""" For use of the Emotion Predict function of the Watson NLP Library """
import requests
import json

def emotion_detector(text_to_analyze):
    """Predicts Emotion of Text using text_to_analyze"""
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyze } }
    response = requests.post(url = url, headers = headers, json = myobj)
    formatted_response = json.loads(response.text)
    emote = formatted_response['emotionPredictions'][0]['emotion']
    anger_score = emote['anger']
    disgust_score = emote['disgust']
    fear_score = emote['fear']
    joy_score = emote['joy']
    sadness_score = emote['sadness']
    high_score = -1000
    for emotion in emote:
        if float(emote[emotion]) > high_score:
            high_score = float(emote[emotion])
            dominant_emotion = emotion
    
    return {
'anger': anger_score,
'disgust': disgust_score,
'fear': fear_score,
'joy': joy_score,
'sadness': sadness_score,
'dominant_emotion': dominant_emotion
}



import requests
import json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyze } }
    response = requests.post(url, json = myobj, headers=headers)

    formatted_response = json.loads(response.text)

    if response.status_code == 200:
        emotions = formatted_response['emotionPredictions'][0]['emotion']
        dominant_emotion = max(emotions, key=emotions.get) 
        emotion_dic = emotions
        emotion_dic['dominant_emotion'] = dominant_emotion
    elif response.status_code == 400:
        emotion_dic = {'anger': None, 'disgust': None, 
        'fear': None, 'joy': None , 'sadness': None, 
        'dominant_emotion': None}

    return emotion_dic
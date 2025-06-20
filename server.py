''' Executing this function initiates the application of sentiment
    analysis to be executed over the Flask channel and deployed on
    localhost:5000.
'''

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_analyzer():
    ''' This code receives the text from the HTML interface and 
        runs sentiment analysis over it using sentiment_analysis()
        function. The output returned shows the label and its confidence 
        score for the provided text.
    '''
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')
    # Pass the text to the sentiment_analyzer function and store the response
    response = emotion_detector(text_to_analyze)
    # Extract the label and score from the response
    ang = response['anger']
    disg = response['disgust']
    fear = response['fear']
    joy = response['joy']
    sad = response['sadness']
    dom_em = response['dominant_emotion']

    if dom_em is None:
        return "Invalid text! Please try again!"

    return f"""For the given statement, the system response is 'anger': {ang},
    'disgust': {disg}, 'fear': {fear}, 'joy': {joy}, and 'sadness':{sad}.
    The dominant emotion is <b>{dom_em}</b>"""

@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
    
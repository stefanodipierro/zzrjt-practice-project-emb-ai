# sentiment_analysis.py is a program that takes a text file as input and outputs the sentiment of the text

# Import the necessary libraries
import requests

def sentiment_analyzer(text_to_analyse):
    url = 'https://sn-watson-sentiment-bert.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/SentimentPredict'
    headers = {"grpc-metadata-mm-model-id": "sentiment_aggregated-bert-workflow_lang_multi_stock"}
    myobj = {"raw_document": {"text": text_to_analyse}}
    response = requests.post(url, json=myobj, headers=headers)
    return response.text

# The function can now be called using:
# result = sentiment_analyzer("I love this new technology.")
# print(result)

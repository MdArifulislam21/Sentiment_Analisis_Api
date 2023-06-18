import torch
from transformers import AutoModelForSequenceClassification, AutoTokenizer
from rest_framework.decorators import api_view
from rest_framework.response import Response


# Load the pre-trained sentiment analysis model and tokenizer
model_name = "finiteautomata/bertweet-base-sentiment-analysis"
model = AutoModelForSequenceClassification.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)



@api_view(['POST'])
def analyze_view(request):
    """
        API view method for sentiment analysis.

        This method accepts a POST request with a JSON payload containing the text to analyze.
        It performs sentiment analysis using the "setfit-ft-sentinent-eval" model from Hugging Face Transformers.
        The predicted sentiment is returned as a response.

        Args:
            request (Request): The incoming HTTP request object.

        Returns:
            Response: A JSON response containing the predicted sentiment.

        Example POST request payload:
        {
            "text": "I just watched an amazing movie. The plot was captivating, the acting was outstanding, and the cinematography was breathtaking. I couldn't take my eyes off the screen!"
        }

        Example response:
        {
            "sentiment": "positive"
        }
    """
    if request.method == 'POST':
        try:
            # Extract the text from the request payload
            text = request.data.get('text', '')
            
            # Tokenize the input text and prepare it for model input
            encoded_input = tokenizer(text, padding=True, truncation=True, return_tensors='pt')
            input_ids = encoded_input['input_ids']
            attention_mask = encoded_input['attention_mask']

            # Perform sentiment analysis using the pre-trained model
            with torch.no_grad():
                logits = model(input_ids, attention_mask=attention_mask).logits
                predicted_labels = torch.argmax(logits, dim=1)

            # Map the predicted label to sentiment label
            sentiment_labels = ['negative', 'neutral', 'positive']
            predicted_sentiment = sentiment_labels[predicted_labels.item()]
            
            # Return the predicted sentiment as a JSON response
            return Response({'sentiment': predicted_sentiment}, status=200)

        except KeyError:
            return Response({'error': 'Invalid request payload'}, status=400)
        
        except Exception as e:
            return Response({'error': str(e)}, status=500)
    else:
        return Response({'error': 'Invalid request payload'}, status=405)


# Sentiment Analisis Api

## Used tools Django, Django Rest Framework, transformers 

------
## To run this project you have to follow some steps.

#### **Step No 1.**

#### Clone the hole project from [Sentiment Analisis Api](https://github.com/MdArifulislam21/Sentiment_Analisis_Api.git)
```
git clone https://github.com/MdArifulislam21/Sentiment_Analisis_Api.git
```

#### Step No 2.

#### install virtualenv  
#### for linux 
```
python3 -m pip install --user virtualenv
```

```
python3 -m venv env
 ```


``` 
source env/bin/activate
```

#### for windows 
 ```
py -m pip install --user virtualenv
 ```
 ```
py -m venv env
 ```
 ```
.\env\Scripts\activate
 ```


#### after that run 
```
pip install -r requirements.txt
```

#### And run the command: 
 ```
python manage.py runserver
```


## Api Documentation 

## Api Url: http://127.0.0.1:8000/analyze/

>
        API view method for sentiment analysis.

        This method accepts a POST request with a JSON payload containing the text to analyze.
        It performs sentiment analysis using the "setfit-ft-sentinent-eval" model from Hugging Face Transformers.
        The predicted sentiment is returned as a response.

        Args:
            request: The incoming HTTP request object.

        Returns:
            A JSON response containing the predicted sentiment.

        Example POST request payload:
        {
            "text": "I just watched an amazing movie. The plot was captivating, the acting was outstanding, and the cinematography was breathtaking. I couldn't take my eyes off the screen!"
        }

        Example response:
        {
            "sentiment": "positive"
        }

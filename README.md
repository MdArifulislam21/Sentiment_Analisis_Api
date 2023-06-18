# Sentiment Analisis Api

## Used tools Django, Django Rest Framework, transformers 

------
## To run this project you have to follow some steps.

#### **Step No 1.**

#### Clone the hole project from [Sentiment Analisis Api](https://github.com/MdArifulislam21/Sentiment_Analisis_Api.git)

#### Step No 2.

> install virtualenv  
> for linux 
 ````python3 -m pip install --user virtualenv```
 ````python3 -m venv env```
 ````source env/bin/activate````

> for windows 
 ````py -m pip install --user virtualenv```
 ````py -m venv env```
 ````.\env\Scripts\activate````


> after that run ````pip install -r requirements.txt````

> And run the command: ````python manage.py runserver````


## Api Documentation 

## Api Url: http://127.0.0.1:8000/analyze/

> input into the Content:
{
    "text" : "You are awesome, Thank You!"
}


> Response:
{
    "sentiment": "positive"
}


# Full Stack Trivia API Backend

## Getting Started

### Installing Dependencies

#### Python 3.7

Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

#### Virtual Enviornment

We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organaized. Instructions for setting up a virual enviornment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

#### PIP Dependencies

Once you have your virtual environment setup and running, install dependencies by naviging to the `/backend` directory and running:

```bash
pip install -r requirements.txt
```

This will install all of the required packages we selected within the `requirements.txt` file.

##### Key Dependencies

- [Flask](http://flask.pocoo.org/)  is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) is the Python SQL toolkit and ORM we'll use handle the lightweight sqlite database. You'll primarily work in app.py and can reference models.py. 

- [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/#) is the extension we'll use to handle cross origin requests from our frontend server. 

## Database Setup
With Postgres running, restore a database using the trivia.psql file provided. From the backend folder in terminal run:
```bash
psql trivia < trivia.psql
```

## Running the server

From within the `backend` directory first ensure you are working using your created virtual environment.

To run the server, execute:

```bash
export FLASK_APP=flaskr
export FLASK_ENV=development
flask run
```

Setting the `FLASK_ENV` variable to `development` will detect file changes and restart the server automatically.

Setting the `FLASK_APP` variable to `flaskr` directs flask to use the `flaskr` directory and the `__init__.py` file to find the application. 

## Tasks

One note before you delve into your tasks: for each endpoint you are expected to define the endpoint and response data. The frontend will be a plentiful resource because it is set up to expect certain endpoints and response data formats already. You should feel free to specify endpoints in your own way; if you do so, make sure to update the frontend or you will get some unexpected behavior. 

1. Use Flask-CORS to enable cross-domain requests and set response headers. 
2. Create an endpoint to handle GET requests for questions, including pagination (every 10 questions). This endpoint should return a list of questions, number of total questions, current category, categories. 
3. Create an endpoint to handle GET requests for all available categories. 
4. Create an endpoint to DELETE question using a question ID. 
5. Create an endpoint to POST a new question, which will require the question and answer text, category, and difficulty score. 
6. Create a POST endpoint to get questions based on category. 
7. Create a POST endpoint to get questions based on a search term. It should return any questions for whom the search term is a substring of the question. 
8. Create a POST endpoint to get questions to play the quiz. This endpoint should take category and previous question parameters and return a random questions within the given category, if provided, and that is not one of the previous questions. 
9. Create error handlers for all expected errors including 400, 404, 422 and 500. 

REVIEW_COMMENT

This README is missing documentation of your endpoints. Below is an example for your endpoint to get all categories. Please use it as a reference for creating your documentation and resubmit your code. 

Endpoints
GET '/categories'
GET '/questions'
DELETE '/questions/<id>'
POST '/questions/<id>'
POST '/questions/search'
GET '/categories/<id>/questions'
POST '/quizzes'

GET '/categories'
- Fetches a dictionary of categories in which the keys are the ids and the value is the corresponding string of the category
- Request Arguments: None
- Returns: An object with a single key, categories, that contains a object of id: category_string key:value pairs. 
```
{
    1: 'Science', 
    2: 'Art', 
    3: 'Geography', 
    4: 'History', 
    5: 'Entertainment', 
    6: 'Sports'
}

```

GET '/questions'

- Fetches a tupel with dictionaries of questions
- Request Arguments: None
- Returns: A tupel with objects with key:value pairs for id, the question, the answer, the category and difficulty.

```
[
    {
        'id': 2, 'question': 'What movie earned Tom Hanks his third straight Oscar nomination, in 1996?', 
        'answer': 'Apollo 13', 
        'category': 5, 
        'difficulty': 4
    }, 
    {
        'id': 4, 'question': 'What actor did author Anne Rice first denounce, then praise in the role of her beloved Lestat?', 
        'answer': 'Tom Cruise', 
        'category': 5, 
        'difficulty': 4
    },
    ... ]

```

DELETE '/questions/<id>'

- Fetches a tupel with dictionaries of questions 
- Request Arguments: the question ID to be deleted acquired from the front-end when the delete button is clicked
- Returns: A tupel with objects with key:value pairs without the deleted question object

```
[
    {
        'id': 2, 'question': 'What movie earned Tom Hanks his third straight Oscar nomination, in 1996?', 
        'answer': 'Apollo 13', 
        'category': 5, 
        'difficulty': 4
    }, 
    {
        'id': 4, 'question': 'What actor did author Anne Rice first denounce, then praise in the role of her beloved Lestat?', 
        'answer': 'Tom Cruise', 
        'category': 5, 
        'difficulty': 4
    }, 
    {
        'id': 5, 'question': "Whose autobiography is entitled 'I Know Why the Caged Bird Sings'?", 
        'answer': 'Maya Angelou', 
        'category': 4, 
        'difficulty': 2
    },  
    ... ]

```
POST '/questions/<id>'

- Posts a tupel with dictionaries of questions
- Request Arguments: an object with the new question, answer, difficulty and category as acquired from the front-end
- Returns: A tupel with objects with key:value pairs for all the questions including the new question added
```
[
    {
        'id': 2, 'question': 'What movie earned Tom Hanks his third straight Oscar nomination, in 1996?', 
        'answer': 'Apollo 13', 
        'category': 5, 
        'difficulty': 4
    }, 
    {
        'id': 4, 'question': 'What actor did author Anne Rice first denounce, then praise in the role of her beloved Lestat?', 
        'answer': 'Tom Cruise', 
        'category': 5, 
        'difficulty': 4
    }, 
    * new question ... *
    {
        'id': 5, 'question': "Whose autobiography is entitled 'I Know Why the Caged Bird Sings'?", 
        'answer': 'Maya Angelou', 
        'category': 4, 
        'difficulty': 2
    }, 
    ... ]

```

POST '/questions/search'

- Posts a tupel with dictionaries of questions
- Request Arguments: a searchTerm acquired from the FE
- Returns: A tupel with objects with key:value pairs for all the questions in which the searchTerm can be found

```
searchTerm = "Africa"
[
    {
        'id': 13, 'question': 'What is the largest lake in Africa?', 
        'answer': 'Lake Victoria', 
        'category': 3, 
        'difficulty': 2
    }, 
    {
        'id': 37, 'question': 'How many countries are in Africa?', 
        'answer': '54', 
        'category': 3, 
        'difficulty': 4
    }
]
```

GET '/categories/<id>/questions'

- Posts a tupel with dictionaries of questions
- Request Arguments: the catergory ID as acquired by the FE when a category is clicked on
- Returns: A tupel with objects with key:value pairs for all the questions in the category clicked on

```
category = Sports
[
    {
        'id': 10, 'question': 'Which is the only team to play in every soccer World Cup tournament?', 
        'answer': 'Brazil', 
        'category': 6, 
        'difficulty': 3
    }, 
    {
        'id': 11, 'question': 'Which country won the first ever soccer World Cup in 1930?', 
        'answer': 'Uruguay', 
        'category': 6, 
        'difficulty': 4
    }
]
```

POST '/quizzes'

- Posts a tupel with dictionaries of questions
- Request Arguments: the quiz category and the previous questions asked
- Returns: An object with key:value pairs for a random question in in the quiz, not previousely asked.

```
category = Art
{
    'id': 16, 
    'question': 'Which Dutch graphic artist–initials M C was a creator of optical illusions?', 
    'answer': 'Escher', 
    'category': 2, 
    'difficulty': 1
}
```



## Testing
To run the tests, run
```
dropdb trivia_test
createdb trivia_test
psql trivia_test < trivia.psql
python test_flaskr.py
```
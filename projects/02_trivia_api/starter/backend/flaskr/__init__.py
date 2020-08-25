import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import random

from models import setup_db, Question, Category

QUESTIONS_PER_PAGE = 10

def paginate_questions(request, selection):
    page = request.args.get('page', 1, type=int)
    start = (page - 1) * QUESTIONS_PER_PAGE
    end = start + QUESTIONS_PER_PAGE
    questions = [question.format() for question in selection]
    current_questions = questions[start:end]

    return current_questions

def create_app(test_config=None):
  # create and configure the app
  app = Flask(__name__)
  setup_db(app)
  CORS(app, resources={"/": {"origins": "*"}})


  # CORS Headers 
  @app.after_request
  def after_request(response):
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization,true')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
    return response


  @app.route('/categories')
  def retrieve_categories():
    all_categories = Category.query.order_by(Category.id).all()
    categories = {}
    for category in all_categories:
      categories[category.id] = category.type

    if categories is None:
      abort(404)
    
    return jsonify({
        'success': True,
        'categories': categories
    })


  @app.route('/questions')
  def retrieve_questions():
    selection = Question.query.order_by(Question.id).all()
    current_questions = paginate_questions(request, selection)

    if len(current_questions) == 0:
      abort(404)

    try:
      all_categories = Category.query.order_by(Category.id).all()
      categories = {}
      for category in all_categories:
        categories[category.id] = category.type
      

      return jsonify({
        'success': True,
        'questions': current_questions,
        'total_questions': len(Question.query.all()),
        'categories': categories
        })
    except:
      abort(422)


  @app.route('/questions/<int:question_id>', methods=['DELETE'])
  def delete_question(question_id):

    question = Question.query.filter(Question.id == question_id).one_or_none()
    if question is None:
      abort(404)

    try:

      question.delete()
      selection = Question.query.order_by(Question.id).all()
      current_questions = paginate_questions(request, selection)

      all_categories = Category.query.order_by(Category.id).all()
      categories = {}
      for category in all_categories:
        categories[category.id] = category.type
      
      return jsonify({
        'success': True,
        'questions': current_questions,
        'total_questions': len(Question.query.all()),
        'categories': categories
      })

    except:
      abort(422)


  @app.route('/questions', methods=['POST'])
  def add_question():
    body = request.get_json()

    new_question = body.get('question'),
    new_answer = body.get('answer'),
    new_difficulty = body.get('difficulty'),
    new_category = body.get('category')

    if ((new_question is None) or (new_answer is None) or (new_difficulty is None) or (new_category is None)):
      abort(422)

    try:
      question = Question(question=new_question, answer=new_answer, difficulty=new_difficulty, category=new_category)
      question.insert()
      selection = Question.query.order_by(Question.id).all()
      current_questions = paginate_questions(request, selection)

      all_categories = Category.query.order_by(Category.id).all()
      categories = {}
      for category in all_categories:
        categories[category.id] = category.type

      return jsonify({
        'success': True,
        'questions': current_questions,
        'total_questions': len(Question.query.all()),
        'categories': categories
      })

    except:
      abort(422)


  @app.route('/questions/search', methods=['POST'])
  def search_questions():

    body = request.get_json()
    searchTerm = body.get('searchTerm', None)

    if searchTerm is None:
      abort(404)

    try:
      selection = Question.query.filter(Question.question.ilike(f'%{searchTerm}%')).all()
      current_questions = paginate_questions(request, selection)

      if selection is None:
        abort(404)

      return jsonify({
        'success': True,
        'questions': current_questions,
        'total_questions': len(current_questions)
        })

    except:
      abort(422)


  @app.route('/categories/<int:category_id>/questions')
  def retrieve_category(category_id):
    
    category = Category.query.filter(Category.id == category_id).one_or_none()
    selection = Question.query.order_by(Question.id).all()

    if category is None:
      abort(404)

    show_questions = []

    try:

      for question in selection:
        if category_id == question.category:
          show_questions.append(question.format())
      
      return jsonify({
        'success': True,
        'questions': show_questions,
        'total_questions': len(Question.query.all())
        })

    except:
      abort(422)


  @app.route('/quizzes', methods=['POST'])
  def retrieve_quiz():

    body = request.get_json()

    quiz_category = body.get('quiz_category')
    previous_questions = body.get('previous_questions')


    if quiz_category is None or previous_questions is None:
      abort(404)

    if quiz_category['id'] == 0:
      remaining_questions = Question.query.filter(
        Question.id.notin_((previous_questions))).all()
    else:
      remaining_questions = Question.query.filter_by(category=quiz_category['id']).filter(Question.id.notin_((previous_questions))).all()
    
    new_question = remaining_questions[random.randrange(0, len(remaining_questions))].format() if len(remaining_questions) > 0 else None
 
    return jsonify({
      'success': True,
      'question': new_question,
      'previousQuestions': previous_questions,
    })

  @app.errorhandler(400)
  def bad_request(error):
    return jsonify({
      'success': False,
      'error': False,
      'message': 'Request not understood due to malformed syntax.'
    }), 400

  @app.errorhandler(404)
  def not_found(error):
    return jsonify({
      'success': False,
      'error': False,
      'message': 'No matching request found.'
    }), 404

  @app.errorhandler(422)
  def unprocessable(error):
    return jsonify({
      'success': False,
      'error': False,
      'message': 'Unable to process the contained instructions.'
    }), 422


  @app.errorhandler(500)
  def internal_server_error(error):
    return jsonify({
      'success': False,
      'error': False,
      'message': 'Encountered an unexpected condition which prevented it from fulfilling the request.'
    }), 500
  
  return app

    
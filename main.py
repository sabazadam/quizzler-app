from question_model import Question
from quiz_brain import QuizBrain
import requests
import ui


question_data = requests.get("https://opentdb.com/api.php?amount=10&category=17&difficulty=easy&type=boolean").json()
question_bank = question_data["results"]



quiz = QuizBrain(question_bank)
UI = ui.QuizInterface(quiz)





print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")

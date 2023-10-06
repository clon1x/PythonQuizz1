from data import Data
from quiz_brain import QuizBrain


question_bank = Data(number_of_questions=12, difficulty='', category='')
question_bank.query_data()

print(f'Response code: {question_bank.get_response_code()}')
print(question_bank.get_questions())

brain = QuizBrain(question_bank.get_questions())

while brain.more_questions():
    q = brain.next_question()

print(f"You completed the Quizz! Your final score is {brain.score}/{brain.index}")
from question import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for question in question_data:
    question_bank.append(Question(text=question["text"], answer=question["answer"]))
    
del question
del question_data

brain = QuizBrain(question_bank)

while brain.more_questions():
    q = brain.next_question()

print(f"You completed the Quizz! Your final score is {brain.score}/{brain.index}")
from random import shuffle

from question import Question


def get_answers(question):
    answers = [{"text": question.correct_answer, "ok": True}]
    for answer in question.incorrect_answers:
        answers.append({"text": answer, "ok": False})
    shuffle(answers)
    return answers


def make_answers_text(answers):
    answers_text = ''
    for i in range(len(answers)):
        answers_text += f'\n{i+1}: {answers[i]["text"]}'
    return answers_text


class QuizBrain:
    questions: list[Question]

    def __init__(self, questions_list):
        self.index = 0
        self.score = 0
        self.questions = questions_list

    def more_questions(self):
        return self.index < len(self.questions)

    def next_question(self):
        question = self.questions[self.index]
        self.index += 1

        answers = get_answers(question)
        answers_text = make_answers_text(answers)

        print(f'Q.{self.index}: {question.text}')
        print(answers_text)

        # substract 1 to get the index
        answer_index = -1 + int(input(f"Write the number of the correct answer: 1-{len(answers)}: "))

        self.check_answer(answer_index, answers)

        print(f'The correct answer was: {question.correct_answer}.')
        print(f'Your current score is: {self.score}/{self.index}\n')

    def check_answer(self, index, answers):
        if answers[index]["ok"]:
            self.score += 1
            print('You got it right!')
        else:
            print('Wrong answer!')

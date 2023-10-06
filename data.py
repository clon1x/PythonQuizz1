import requests

from question import Question


class Data:
    number_of_questions: int
    difficulty: str
    category: str
    question_data: list[dict]
    response_code: int

    def __init__(self, number_of_questions, difficulty, category):
        self.question_data = []
        self.number_of_questions = number_of_questions
        self.difficulty = difficulty
        self.category = category

    def query_data(self):
        payload = {
            'amount': self.number_of_questions,
            'type': 'multiple',
            'category': self.category,
            'difficulty': self.difficulty
        }

        r = requests.get(f'https://opentdb.com/api.php?', params=payload)
        json = r.json()
        self.response_code = int(json["response_code"])
        self.question_data = json["results"]

    def get_questions(self):

        questions = []

        for entry in self.question_data:
            questions.append(
                Question(
                    text=entry["question"],
                    correct_answer=entry["correct_answer"],
                    incorrect_answers=entry["incorrect_answers"]))

        return questions

    def get_response_code(self):
        return self.response_code
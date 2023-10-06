# -*- coding: utf-8 -*-

class Question:
    correct_answer: str
    incorrect_answers: list[str]

    def __init__(self, text, correct_answer, incorrect_answers):
        self.text = text
        self.correct_answer = correct_answer
        self.incorrect_answers = incorrect_answers

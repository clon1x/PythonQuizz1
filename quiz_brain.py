class QuizBrain:
    
    def __init__(self, questions_list):
        self.index = 0
        self.score = 0
        self.questions = questions_list
        
    def more_questions(self):
        return self.index < len(self.questions)

    def next_question(self):
        question = self.questions[self.index]
        self.index += 1
        prompt = f'Q.{self.index}: {question.text}. (True/False)?: '
        
        answer = input(prompt)
        
        if answer == question.answer:
            self.score += 1
            print('You got it right!')
        else:
            print('Wrong answer!')

        print(f'The correct answer was: {question.answer}.')
        print(f'Your current score is: {self.score}/{self.index}\n')

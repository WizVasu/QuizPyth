# question.py
class Question:
    def __init__(self, question_text, answer):
        self.question_text = question_text
        self.answer = answer

    def check_ans(self, user_ans):
        return user_ans == self.answer

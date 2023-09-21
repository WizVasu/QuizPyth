import question

class Quiz:
    def __init__(self, questions):
        self.questions = questions
        self.current_question_index = 0
        self.score = 0

    def next_question(self):
        if self.current_question_index >= len(self.questions):
            return None

        current_question = self.questions[self.current_question_index]
        self.current_question_index += 1
        return current_question

    def check_ans(self, user_ans):
        current_question = self.questions[self.current_question_index - 1]
        is_correct = current_question.check_ans(user_ans)

        if is_correct:
            self.score += 2
        else:
            self.score -= 1

        return is_correct

    def do_questions_remain(self):
        return self.current_question_index < len(self.questions)

    def get_score(self):
        return self.score
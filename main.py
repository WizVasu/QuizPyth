import question  # Import the Question class from the question module
import quiz

def load_questions_from_file(filename):
    with open(filename, "r") as f:
        questions_data = f.readlines()

    questions = []
    for question_line in questions_data:
        question_text, answer = question_line.strip().split(",")
        questions.append(question.Question(question_text, answer))  # Use 'question.Question'

    return questions

def start_quiz():
    my_quiz = quiz.Quiz(load_questions_from_file("questions.txt"))

    while my_quiz.do_questions_remain():
        current_question = my_quiz.next_question()

        if current_question is None:
            break

        print(current_question.question_text)
        user_ans = input("Answer: ")

        is_correct = my_quiz.check_ans(user_ans)

        if is_correct:
            print("Correct!")
        else:
            print("Incorrect. The correct answer is:", current_question.answer)

    print("Your final score is:", my_quiz.get_score())

if __name__ == "__main__":
    start_quiz()

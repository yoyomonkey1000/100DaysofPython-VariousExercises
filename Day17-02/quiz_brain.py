# ask user a question
# check if answer is right

class QuizBrain:

    def __init__(self, questionbank):
        self.question_number = 0
        self.question_list = questionbank
        self.score = 0


    def check_answer(self, user_answer, actual_answer):
        if user_answer.lower() == actual_answer.lower():
            print("You got it correct!")
            self.score += 1
        else:
            print("You got it wrong!")
        print(f"The actual answer is {actual_answer} and your score is {self.score}/{self.question_number}")
        print("\n")


    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        answer = input(f"Q{self.question_number}: {current_question.text} (True/False) ")
        self.check_answer(answer, current_question.answer)

    def still_has_questions(self):
        return self.question_number < len(self.question_list)















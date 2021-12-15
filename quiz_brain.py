class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_ans = input(f"Ques.{self.question_number}: {current_question.text} Your answer(True/False):")
        self.check_ans(user_ans, current_question.answer)

    def check_ans(self, user_ans, correct_ans):
        if user_ans.lower() == correct_ans.lower():
            self.score += 1
            print("Correct Answer!")
        else:
            print("That's wrong.")
        print(f"Your score: {self.score}/{self.question_number}")
        print("\n")



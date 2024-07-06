class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list
        self.current_question = None

    def still_has_questions(self):
        """Check if there are more questions in the quiz."""
        return self.question_number < len(self.question_list)

    def next_question(self):
        """Move to the next question in the quiz."""
        if self.still_has_questions():
            self.current_question = self.question_list[self.question_number]
            self.question_number += 1
            return self.current_question["question"]
        else:
            return None

    def check_answer(self, user_answer):
        """Check the user's answer against the correct answer."""
        correct_answer = self.current_question["correct_answer"]
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            return True
        else:
            return False

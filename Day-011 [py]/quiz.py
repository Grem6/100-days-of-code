question_data = [
    {"text": "A slug's blood is green.", "answer": "True"},
    {"text": "The loudest animal is the African Elephant.", "answer": "False"},
    {"text": "Approximately one quarter of human bones are in the feet.", "answer": "True"},
    {"text": "The total surface area of a human lungs is the size of a football pitch.", "answer": "True"},
    {"text": "In West Virginia, USA, if you accidentally hit an animal with your car, you are free to take it home to eat.", "answer": "True"},
    {"text": "In London, UK, if you happen to die in the House of Parliament, you are entitled to a state funeral.", "answer": "False"},
    {"text": "It is illegal to pee in the Ocean in Portugal.", "answer": "True"},
    {"text": "You can lead a cow down stairs but not up stairs.", "answer": "False"},
    {"text": "Google was originally called 'Backrub'.", "answer": "True"},
    {"text": "Buzz Aldrin's mother's maiden name was 'Moon'.", "answer": "True"},
    {"text": "No piece of square dry paper can be folded in half more than 7 times.",
        "answer": "False"},
    {"text": "A few ounces of chocolate can to kill a small dog.", "answer": "True"}
]

question_bank = []


class Question:
    def __init__(self, text, answer):
        self.text = text
        self.answer = answer


class Quizzer:

    def __init__(self, questionlist):
        self.questionNo = 0
        self.score =0
        self.questionList = questionlist

    def nextQuestion(self):
        currentQ = self.questionList[self.questionNo]
        self.questionNo +=1
        answer = input(f"Q.{self.questionNo}: {currentQ.text} (True/False)")
        self.checkAnswer(answer,currentQ.answer)

    def stillHasQuestions(self):
        return self.questionNo < len(self.questionList)
    
    def checkAnswer(self, answer, correctanswer):
        if answer.lower() == correctanswer.lower():
            self.score+=1
            print('You got it right!')
            print(f"Your current score is: {self.score}")
            print('\n')
        else:
            self.score-=1
            print('you got it wrong')
        print(f"the correct answer: {answer}")
        

        

for i in range(len(question_data)):
    i = Question(question_data[i]['text'], question_data[i]['answer'])
    question_bank.append(i)

quiz = Quizzer(question_bank)

while quiz.stillHasQuestions():
    quiz.nextQuestion() 
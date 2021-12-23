class Question:
    def __init__(self, question, ans1, ans2, ans3, ans4, correctAns):
        self.__question = question
        self.__ans1 = ans1
        self.__ans2 = ans2
        self.__ans3 = ans3
        self.__ans4 = ans4
        self.__correctAns = correctAns

    # set methods
    def setQuestion(self, question):
        self.__question = question

    def setAns1(self, ans1):
        self.__ans1 = ans1

    def setAns2(self, ans2):
        self.__ans2 = ans2

    def setAns3(self, ans3):
        self.__ans3 = ans3

    def setAns4(self, ans4):
        self.__ans4 = ans4

    def setCorrectAns(self, correctAns):
        self.__correctAns = correctAns

    # get methods
    def getQuestion(self):
        return self.__question

    def getAns1(self):
        return self.__ans1

    def getAns2(self):
        return self.__ans2

    def getAns3(self):
        return self.__ans3

    def getAns4(self):
        return self.__ans4

    def getCorrectAns(self):
        return self.__correctAns



    def __str__(self):
        result = self.getQuestion() + '\n' + \
            'Option 1 - ' + self.getAns1() + '\n' + \
            'Option 2 - ' + self.getAns2() + '\n' + \
            'Option 3 - ' + self.getAns3() + '\n' + \
            'Option 4 - ' + self.getAns4()
        return result

    def rightAnswer (self, answer):
        return answer == self.getCorrectAns()
from django.db import models

class User(models.Model):
    username = models.CharField(unique=True, max_length=200)
    email = models.EmailField(unique=True, max_length=200)
    password = models.CharField(max_length=200)
    
    def __str__(self):
        return self.username

class Question(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name="choices")
    answer = models.CharField(max_length=200)
    
    def __str__(self):
        return self.answer
    


class Vote(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name="votes",null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="votes")
    choice = models.ForeignKey(Choice, on_delete=models.CASCADE, related_name="votes")
    timestamp = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return str(self.question.name)+"-" + str(self.user.username) +"-" + str(self.choice.answer)


# #relationship
# votes to Question
# vote to Choices
# vote to User

# vote on question
# choice have a Question
# user can vote
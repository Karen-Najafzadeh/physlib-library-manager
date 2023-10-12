from django.db import models

class Treasury(models.Model):
    balance = models.IntegerField(default=0)
    cash = models.IntegerField(default=0)
    credit = models.IntegerField(default=0)

    def __str__(self) -> str:
        return f"{self.balance}"

class Income(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    cost = models.IntegerField(default=0)
    cash = 'cash'
    credit = 'credit'
    type_choices = (
        (cash, 'cash'),
        (credit, 'credit'),
    )
    type = models.CharField(max_length=6, choices = type_choices)
    def __str__(self) -> str:
        return f"{self.cost} ريال for {self.title}"

class Expence(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    cost = models.IntegerField(default=0)
    cash = 'cash'
    credit = 'credit'
    type_choices = (
        (cash, 'cash'),
        (credit, 'credit'),
    )
    type = models.CharField(max_length=6, choices = type_choices)
    def __str__(self) -> str:
        return f"{self.cost} ريال for {self.title}"
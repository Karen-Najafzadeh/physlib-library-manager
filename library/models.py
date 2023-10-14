from django.db import models

class Member(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    student_number = models.CharField(max_length=255, null=True, blank=True, unique=True)
    phone_number = models.CharField(max_length=255)
    financial_balance = models.IntegerField(default=0)
    email = models.EmailField()

    student = 'student'
    teacher = 'teacher'
    occupation_choices = (
        (student, 'student'),
        (teacher, 'teacher'),
    )

    occupation = models.CharField(max_length=7, choices=occupation_choices)

    def __str__(self) -> str:
        return f"id ={self.id} {self.first_name} {self.last_name}/ student number = {self.student_number}"

class Book(models.Model):
    
    name = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    date_borrowed = models.DateField(null=True, blank=True)
    borrower = models.ForeignKey(Member, null=True, blank=True, on_delete=models.SET_NULL, related_name='books')
    date_to_be_returned = models.DateField(null=True, blank=True)
    
    quantum = 'quantum'
    solid = 'solid'
    astro = 'astro'
    genre_choices = (
        (quantum, 'quantum'),
        (solid, 'solid'),
        (astro, 'astro'),
    )
    genre = models.CharField(max_length=255,choices = genre_choices)
    shelf = models.PositiveIntegerField()
    def __str__(self) -> str:
        return f"{self.name} {self.author} id = {self.id}"

class Locker(models.Model):
    number = models.PositiveIntegerField(primary_key=True)
    student = models.OneToOneField(Member,null=True, blank=True, on_delete=models.SET_NULL)
    cost = models.PositiveIntegerField()
    date_rented = models.DateField(blank=True, null=True)
    date_expires = models.DateField(blank=True, null=True)

    def __str__(self) -> str:
        return f"locker number{self.number}"
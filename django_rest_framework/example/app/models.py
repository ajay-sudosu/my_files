from tabnanny import verbose
from django.db import models

# Create your models here.
class Category(models.Model):
    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=225)

    def __str__(self):
        return self.name


class Quiz(models.Model):
    class Meta:
        verbose_name_plural = 'Quizes'
        verbose_name = 'Quiz'

    category = models.ForeignKey(Category,default=1,on_delete=models.DO_NOTHING,related_name='category')
    title = models.CharField(max_length=225,blank=True,null=True)
    date_created = models.DateTimeField(auto_now_add=True,blank=True,null=True)
    
    def __str__(self):
        return self.title


class Updated(models.Model):
    class Meta:
        abstract = True
        
    date_updated = models.DateTimeField(verbose_name='Last Updated',blank=True,null=True,auto_now_add=True)


class Question(Updated):
    levels = (
       ('Easy', ('Easy')),
       ('Medium', ('Medium')),
       ('Hard', ('Hard')),
    )
    class Meta:
        verbose_name_plural = 'Questions'
        verbose_name = 'Question'
    
    
    category = models.ForeignKey(Category,default=1,on_delete=models.DO_NOTHING,related_name='ques_category')
    quiz = models.ForeignKey(Quiz,default=1,on_delete=models.DO_NOTHING,related_name='questions')
    date_created = models.DateTimeField(auto_now_add=True,verbose_name='Date Created',blank=True,null=True)
    question_name = models.CharField(max_length=255,verbose_name='question',blank=True,null=True)
    difficulty = models.CharField(max_length=255,choices=levels,default='Easy',verbose_name='Difficulty Level',blank=True,null=True)

    def __str__(self):
        return self.question_name

from django.db import models

# Create your models here.
class PersonalMemo(models.Model):

    title = models.CharField(max_length=100)
    memoDescription = models.CharField(max_length=200)
    lastEditDate = models.DateTimeField('    ', auto_now=True)
    # date = models.CharField(max_length=100)

    # foreignkey 설정할 때 web에서 primary key의 name으로 보여주게됨. but db에는 id로 저장됨
    # 아니면 primary key 그대로 1번 2번 이렇게 보임.
    def __str__(self):
        return self.title
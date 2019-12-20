from django.db import models

# Create your models here.
# python manage.py makemigrations  此时数据库还没有生成数据表
# python manage.py migrate
# python manage.py runserver


class Grades(models.Model):
    gname = models.CharField(max_length=20)
    gdate = models.DateField()
    ggirlnum = models.IntegerField()
    gboynum = models.IntegerField()
    isDelete = models.BooleanField()

    def __str__(self):
        return self.gname


class Students(models.Model):
    sname = models.CharField(max_length=20)
    sgender = models.BooleanField(default=True)
    sage = models.IntegerField()
    scontend = models.CharField(max_length=20)
    isDelete = models.BooleanField(default=False)
    sgrade = models.ForeignKey("Grades", on_delete=models.CASCADE)  # 2.0以上外键还要加一个参数

    def __str__(self):
        return self.sname
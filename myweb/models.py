from django.db import models
from datetime import datetime

# Create your models here.

#myweb_pic
class Pic(models.Model):  
    name = models.CharField(max_length=32)
    picname = models.CharField(max_length=32)
    addtime=models.DateTimeField(default=datetime.now)

    def picinsert(self,request,filename):
        self.name = request.POST['name']
        self.picname = filename
        self.addtime= datetime.now
        self.save()

    #class Meta:
    #    db_table = "myweb_pic"  # 更改表名 

class Stu(models.Model): 
    name = models.CharField(max_length=16)
    age = models.IntegerField()
    sex = models.CharField(max_length=1)
    classid = models.CharField(max_length=8)

    class Meta:
        db_table = "stu"  # 更改表名
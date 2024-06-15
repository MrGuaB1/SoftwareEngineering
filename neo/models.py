from django.db import models

'''
用户表
@ username: 用户名
@ password: 密码
@ email: 邮箱
@ permission: 权限，0为普通用户，1为养殖户，2为管理员
'''
class User(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    email = models.EmailField()
    permission = models.IntegerField(default=0)

'''
@ Year：年
@ Date：年月日
@ Latin_Name：鱼群名
@ Count：统计数量
@ Mean_Length：平均长度
@ Mean_Weight：平均重量
'''
class FishInfo(models.Model):
    year = models.IntegerField()
    date = models.DateField()
    latin_name = models.CharField(max_length=30)
    count = models.IntegerField()
    mean_length = models.FloatField()
    mean_weight = models.FloatField()



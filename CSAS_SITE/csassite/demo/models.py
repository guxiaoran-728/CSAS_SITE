from django.db import models

# Create your models here.
class Msg(models.Model):
    name = models.CharField(max_length=200, null=True, verbose_name='漏洞名称')
    link = models.CharField(max_length=1000, null=True, verbose_name='漏洞路径')
    objects = models.Manager

    class Meta:
        verbose_name = '数据'
        verbose_name_plural = verbose_name
    def __str__(self):
        if self.name:
            return self.name

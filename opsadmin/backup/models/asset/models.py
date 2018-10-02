from django.db import models

# Create your models here.

class Host(models.Model):
    hostname = models.CharField(max_length=30,verbose_name="主机名",unique=True)
    mac = models.CharField(max_length=40,verbose_name="MAC地址")
    outer_ip = models.CharField(verbose_name="外网地址",max_length=40,blank=True,null=True) # 如果使用GenericIPAddressField类型,在插入的时候会报错,后续解决一下
    os_platform = models.CharField(max_length=20,verbose_name="系统平台")
    os_type = models.CharField(max_length=20,verbose_name="操作系统")
    os_version = models.CharField(max_length=20,verbose_name="系统版本")
    os_kernel = models.CharField(max_length=30,verbose_name="内核版本")
    cpu_arch = models.CharField(max_length=30,verbose_name="CPU架构")
    cpu_physical_num = models.IntegerField(verbose_name="CPU物理核心数")
    cpu_logical_num = models.IntegerField(verbose_name="CPU逻辑核心数")
    mem_total = models.CharField(verbose_name="内存大小",max_length=30)

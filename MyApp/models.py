from django.db import models


# Create your models here.


class DB_tucao(models.Model):
    user = models.CharField(max_length=30, null=True)  # 吐槽人名字
    text = models.CharField(max_length=1000, null=True)  # 内容
    ctime = models.DateTimeField(auto_now=True)  # 时间

    def __str__(self):
        return self.text + str(self.ctime)

    class Meta:
        verbose_name = '吐槽信息'
        verbose_name_plural = verbose_name


class DB_home_href(models.Model):
    name = models.CharField(max_length=30, null=True)
    href = models.CharField(max_length=2000, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '首页传送门'
        verbose_name_plural = verbose_name


class DB_project(models.Model):
    name = models.CharField(max_length=100, null=True, verbose_name='项目名称')
    remark = models.CharField(max_length=1000, null=True, verbose_name='项目备注')
    user = models.CharField(max_length=15, null=True, verbose_name='项目创建者名称')
    other_user = models.CharField(max_length=15, null=True, verbose_name='其他创建者')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '项目信息'
        verbose_name_plural = verbose_name


class DB_apis(models.Model):
    project_id = models.CharField(max_length=10, null=True, verbose_name='项目id')
    name = models.CharField(max_length=100, null=True, verbose_name='接口名字')
    api_method = models.CharField(max_length=10, null=True, verbose_name='请求方式')
    api_url = models.CharField(max_length=1000, null=True, verbose_name='url')
    api_header = models.CharField(max_length=1000, null=True, verbose_name='请求头')
    api_login = models.CharField(max_length=10, null=True, verbose_name='是否带登陆态')
    api_host = models.CharField(max_length=100, null=True, verbose_name='域名')
    des = models.CharField(max_length=100, null=True, verbose_name='描述')
    body_method = models.CharField(max_length=20, null=True, verbose_name='请求体编码格式')
    api_body = models.CharField(max_length=1000, null=True, verbose_name='请求体')
    result = models.TextField(null=True, verbose_name='返回体')  # 因为长度巨大，所以用大文本方式存储
    sign = models.CharField(max_length=10, null=True, verbose_name='是否验签')
    file_key = models.CharField(max_length=50, null=True, verbose_name='文件key')
    file_name = models.CharField(max_length=50, null=True, verbose_name='文件名')
    public_header = models.CharField(max_length=1000, null=True, verbose_name='全局变量-请求头')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '接口信息'
        verbose_name_plural = verbose_name

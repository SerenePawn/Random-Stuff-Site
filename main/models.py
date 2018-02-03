from django.db import models
from django.contrib.auth.models import User
from base64 import b16encode


def upload_location(i, imgname):
    enc = b16encode(imgname.encode('utf-8'))
    enc = enc.decode('utf-8')
    return '%s/%s/%s' % (enc[:2], enc[2:4], imgname)

class Goods(models.Model):
    goods_name = models.CharField(max_length=64)
    goods_pic = models.ImageField(default='default_pic', upload_to=upload_location)
    goods_price = models.FloatField(default=99.9)
    goods_amount = models.IntegerField(default=1488)
    goods_description = models.TextField()
    goods_producer = models.CharField(max_length=32)
    goods_producer_url = models.URLField(null=True, blank=True)

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return self.goods_name

class GoodsComments(models.Model):
    comment_related = models.ForeignKey(Goods, on_delete=models.CASCADE)
    comment_text = models.CharField(max_length=800)
    comment_by = models.ForeignKey(User)
    comment_date = models.DateField(auto_now=True)

    def __str__(self):
        return self.comment_text


class GoodsRate(models.Model):
    rate_related = models.ForeignKey(Goods, on_delete=models.CASCADE)
    rate_count = models.IntegerField(default=0)

    def __str__(self):
        return self.rate_related


class GoodsGallery(models.Model):
    goods_related = models.ForeignKey(Goods, on_delete=models.CASCADE, related_name='gallery')
    goods_gallery_pic = models.ImageField(blank=True, null=True)

    def __str__(self):
        return self.goods_related


class Feedback(models.Model):
    feedback_subject = models.CharField(max_length=40)
    feedback_text = models.CharField(max_length=2000)
    feedback_by = models.ForeignKey(User, on_delete=models.CASCADE)
    feedback_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.feedback_text
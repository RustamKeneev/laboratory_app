from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from django.db.models.signals import post_delete
from django.dispatch import receiver
from django.utils.safestring import mark_safe
from django_resized import ResizedImageField

TYPE_N_A = (
    (u'news', u'Новость'),
    (u'article', u'Статья'),
)

TYPE_L_M = (
    (u'laboratory', u'Лаборатория'),
    (u'med_center', u'Медицинские центры'),
)


class NewsAndArticle(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название')
    type = models.CharField(max_length=200, verbose_name='Тип', choices=TYPE_N_A)
    short_description = models.TextField(null=True, verbose_name='Краткое описание')
    description = RichTextUploadingField(verbose_name='Описание')
    image = ResizedImageField(upload_to='news_and_article/', verbose_name='Фото', size=[1450, 1450])
    date = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.title

    def image_tag(self):
        return mark_safe('<img src={} width="50" />'.format(self.image.url))

    image_tag.short_description = 'Изображение'

    def image_tag_normal(self):
        return mark_safe('<img src={} width="300" />'.format(self.image.url))

    image_tag_normal.short_description = 'Изображение'


@receiver(post_delete, sender=NewsAndArticle)
def submission_delete(sender, instance, **kwargs):
    instance.image.delete(False)


class LaboratoryAndMedCenter(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название')
    type = models.CharField(max_length=200, verbose_name='Тип', choices=TYPE_L_M)
    address = models.CharField(max_length=200, verbose_name='адресс', null=True, blank=True)
    short_description = models.TextField(null=True, verbose_name='Краткое описание')
    description = RichTextUploadingField(verbose_name='Описание')
    image = ResizedImageField(upload_to='laboratory_and_med_center/', verbose_name='Фото', size=[1450, 1450])
    date = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.title

    def image_tag(self):
        return mark_safe('<img src={} width="50" />'.format(self.image.url))

    image_tag.short_description = 'Изображение'

    def image_tag_normal(self):
        return mark_safe('<img src={} width="300" />'.format(self.image.url))

    image_tag_normal.short_description = 'Изображение'


@receiver(post_delete, sender=LaboratoryAndMedCenter)
def submission_delete(sender, instance, **kwargs):
    instance.image.delete(False)


class HealthyEating(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название')
    short_description = models.TextField(null=True, verbose_name='Краткое описание')
    description = RichTextUploadingField(verbose_name='Описание')
    image = ResizedImageField(upload_to='healthy_eating/', verbose_name='Фото', size=[1450, 1450])
    date = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.title

    def image_tag(self):
        return mark_safe('<img src={} width="50" />'.format(self.image.url))

    image_tag.short_description = 'Изображение'

    def image_tag_normal(self):
        return mark_safe('<img src={} width="300" />'.format(self.image.url))

    image_tag_normal.short_description = 'Изображение'


@receiver(post_delete, sender=HealthyEating)
def submission_delete(sender, instance, **kwargs):
    instance.image.delete(False)


class Partner(models.Model):
    website = models.URLField(verbose_name='Ccылка на веб сайт')
    image = ResizedImageField(upload_to='partner/', verbose_name='Фото', size=[1450, 1450])
    date = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.website

    def image_tag(self):
        return mark_safe('<img src={} width="50" />'.format(self.image.url))

    image_tag.short_description = 'Изображение'

    def image_tag_normal(self):
        return mark_safe('<img src={} width="300" />'.format(self.image.url))

    image_tag_normal.short_description = 'Изображение'


@receiver(post_delete, sender=Partner)
def submission_delete(sender, instance, **kwargs):
    instance.image.delete(False)


class Slider(models.Model):
    website = models.URLField(verbose_name='Ccылка на веб сайт')
    image = ResizedImageField(upload_to='slider/', verbose_name='Фото(1440x400)', size=[1450, 1450])
    date = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.website

    def image_tag(self):
        return mark_safe('<img src={} width="50" />'.format(self.image.url))

    image_tag.short_description = 'Изображение'

    def image_tag_normal(self):
        return mark_safe('<img src={} width="300" />'.format(self.image.url))

    image_tag_normal.short_description = 'Изображение'


@receiver(post_delete, sender=Slider)
def submission_delete(sender, instance, **kwargs):
    instance.image.delete(False)


class Banner(models.Model):
    image = ResizedImageField(upload_to='slider/', verbose_name='Фото', size=[1450, 1450])
    date = models.DateTimeField(auto_now_add=True, null=True)

    def image_tag(self):
        return mark_safe('<img src={} width="50" />'.format(self.image.url))

    image_tag.short_description = 'Изображение'

    def image_tag_normal(self):
        return mark_safe('<img src={} width="300" />'.format(self.image.url))

    image_tag_normal.short_description = 'Изображение'


@receiver(post_delete, sender=Banner)
def submission_delete(sender, instance, **kwargs):
    instance.image.delete(False)


class Contact(models.Model):
    phone = models.CharField(max_length=20, verbose_name='Телефон', )
    email = models.EmailField(max_length=200, )
    whatsapp = models.CharField(max_length=20, null=True, blank=True, )
    instagram = models.URLField(max_length=200, null=True, blank=True, )
    telegram = models.URLField(max_length=200, null=True, blank=True, )
    facebook = models.URLField(max_length=200, null=True, blank=True, )
    app_store = models.URLField(max_length=200, null=True, blank=True, )
    google_play = models.URLField(max_length=200, null=True, blank=True, )
    about = RichTextUploadingField(verbose_name='О нас')


class Subscribe(models.Model):
    email = models.EmailField(max_length=200, unique=True, )
    date = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.email


class Confidentiality(models.Model):

    title = models.CharField(verbose_name='Название', max_length=255)
    description = RichTextUploadingField('Описание')

    class Meta:
        verbose_name = 'Конфиденциальность'
        verbose_name_plural = 'Конфиденциальности'

    def __str__(self):
        return self.title

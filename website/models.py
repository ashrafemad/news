import os
import socket

from django.conf import settings
from django.db import models
from ckeditor.fields import RichTextField
from django.template.defaultfilters import slugify
from django.utils import timezone
from gtts import gTTS
from stdimage import StdImageField
from stdimage.utils import UploadToUUID
from django.conf import settings #or from my_project import settings



class New(models.Model):
    title = models.CharField(max_length=80)
    title_rom = models.CharField(max_length=80)
    content = models.TextField()
    content_rom = models.TextField()
    slug = models.SlugField(blank=True)
    image = StdImageField(upload_to=UploadToUUID(path=''), blank=True,
                          variations={
                              'thumbnail': (300, 300, True),
                          })
    date = models.DateTimeField(default=timezone.now)
    published = models.BooleanField(default=True)
    TYPES = ((1, 'High'), (0, 'Low'))
    priority = models.IntegerField(choices=TYPES, null=False, default=1)
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True)
    audio = models.CharField(max_length=80, blank=True)
    audio_rom = models.CharField(max_length=80, blank=True)

    def __str__(self):
        return '{} - {}'.format(self.category, self.title)

    def save(self, *args, **kwargs):
        if not self.pk:
            self.slug = slugify(self.title)
        tts = gTTS(text=self.content, lang='ru')
        tts_rom = gTTS(text=self.content_rom, lang='ro')
        tts.save(settings.MEDIA_URL + self.slug + '.mp3')
        tts_rom.save(settings.MEDIA_ROOT + '/' + self.slug + '_rom.mp3')
        self.audio = settings.MEDIA_URL + self.slug + '.mp3'
        self.audio_rom = settings.MEDIA_URL  + self.slug + '_rom.mp3'
        super(New, self).save(*args, **kwargs)


class Category(models.Model):
    title = models.CharField(max_length=80)
    title_rom = models.CharField(max_length=80)

    def __str__(self):
        return self.title


class Ads(models.Model):
    title = models.CharField(max_length=80)
    url = models.URLField()
    image = StdImageField(upload_to=UploadToUUID(path='ads'), blank=True)
    published = models.BooleanField(default=True)
    date = models.DateTimeField(default=timezone.now)




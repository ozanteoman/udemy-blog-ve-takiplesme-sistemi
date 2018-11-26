from django.db import models
from django.contrib.auth.models import User


class Fallowing(models.Model):
    fallower = models.ForeignKey(User, related_name='fallower', null=True, verbose_name='Takip eden kullanıcı')
    fallowed = models.ForeignKey(User, null=True, related_name='fallowing', verbose_name='Takip edilen kullanıcı')

    class Meta:
        verbose_name_plural = 'Takipleşme Sistemi'

    def __str__(self):
        return "Fallower {} - Fallowed {}".format(self.fallower.username, self.fallowed)

    @classmethod
    def kullanici_takip_et(cls, fallower, fallowed):
        cls.objects.create(fallower=fallower, fallowed=fallowed)

    @classmethod
    def kullanici_takipten_cikar(cls, fallower, fallowed):
        cls.objects.filter(fallower=fallower, fallowed=fallowed).delete()

    @classmethod
    def kullaniciyi_takip_ediyor_mu(cls, fallower, fallowed):
        return cls.objects.filter(fallower=fallower, fallowed=fallowed).exists()

    @classmethod
    def kullanici_takip_edilenler_ve_takipciler(cls, user):
        data = {'takip_edilenler': 0, 'takipciler': 0}
        takip_edilenler = cls.objects.filter(fallower=user).count()
        takipciler = cls.objects.filter(fallowed=user).count()

        data.update({'takip_edilenler': takip_edilenler, 'takipciler': takipciler})
        return data

    @classmethod
    def get_fallowers(cls, user):
        return cls.objects.filter(fallowed=user)
        # kullanıcının takip ettiklerini getir

    @classmethod
    def get_fallowed(cls, user):
        return cls.objects.filter(fallower=user)
        # kullanıcıyı takip edenleri getir.

    @classmethod
    def get_fallowed_username(cls, user):
        fallowed = cls.get_fallowed(user)
        yanit=fallowed.values_list('fallowed__username', flat=True)
        return yanit

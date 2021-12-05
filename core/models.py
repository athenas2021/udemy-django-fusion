from django.db import models
from stdimage.models import StdImageField

class Base(models.Model):
    criados = models.DateTimeField('Criação', auto_now_add=True)
    modificado = models.DateField('Atualização', auto_now=True)
    ativo = models.BooleanField('Ativo', default=True)

    class Meta:
        abstract = True


class Service(Base):
    ICON_CHOICES = (
        ('lni-cog', 'Whell'),
        ('lni-stats-up', 'Graphic'),
        ('lni-users', 'Users'),
        ('lni-layers', 'Design'),
        ('lni-mobile', 'Mobile'),
        ('lni-rocket', 'Rocket'),
    )
    service = models.CharField('Service', max_length=100)
    description = models.TextField('Descripton', max_length=200)
    icon = models.CharField('Icon', max_length=12, choices=ICON_CHOICES)

    class Meta:
        verbose_name = 'Service'
        verbose_name_plural = 'Services'

    def __str__(self):
        return self.service


class Position(Base):
    position = models.CharField('Position', max_length=100)

    class Meta:
        verbose_name = 'Position'
        verbose_name_plural = 'Positions'

    def __str__(self):
        return self.position


class Team(Base):
        name = models.CharField('Name', max_length=100)
        position = models.ForeignKey('core.Position', verbose_name='Position', on_delete=models.CASCADE)
        bio = models.TextField('Bio', max_length=200)
        image = StdImageField('Image', upload_to='team', variations={'thumb': {'width': 480, 'height': 480, 'crop': True}})
        facebook = models.CharField('Facebook', max_length=100, default='#')
        twitter = models.CharField('Twitter', max_length=100, default='#')
        instagram = models.CharField('Instagram', max_length=100, default='#')

        class Meta:
            verbose_name = 'Team'
            verbose_name_plural = 'Teams'

        def __str__(self):
            return self.name
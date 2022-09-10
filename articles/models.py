from django.db import models
from core.models import TimeStampedModel

FILTER1 = 'FILTER1'
FILTER2 = 'FILTER2'
FILTER3 = 'FILTER3'
FILTER4 = 'FILTER4'
CHOICES = [
        (FILTER1, 'Collège'),
        (FILTER2, 'Lycée'),
        (FILTER3, 'Université'),
        (FILTER4, 'Default'),
    ]


class Article(TimeStampedModel):
    slug = models.SlugField(db_index=True, max_length=255, unique=True)
    title = models.CharField(db_index=True, max_length=255)
    image = models.ImageField(upload_to='staticfiles/assets/images/articles/',max_length=512,blank=True, null=True)
    ville = models.CharField(max_length=256,blank=True,null=True)
    link = models.CharField(max_length=256,blank=True,null=True)
    deadline = models.CharField(max_length=256,blank=True,null=True)


    description = models.TextField(blank=True,null=True)
    content = models.TextField()

    author = models.ForeignKey(
        'profile.Profile', on_delete=models.CASCADE, related_name='articles'
    )

    tags = models.ManyToManyField(
        'articles.Tag', related_name='articles'
    )
    
    filter = models.CharField(
        max_length=265,
        choices=CHOICES,
        default=FILTER4, blank=True,null=True
    )

    def __str__(self):
        return self.title


class Tag(TimeStampedModel):
    tag = models.CharField(max_length=255)
    slug = models.SlugField(db_index=True, unique=True)

    def __str__(self):
        return self.tag

# Create your models here.

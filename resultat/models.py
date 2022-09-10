from django.db import models
from profile.models import Profile
from test.models import Test
from core.models import TimeStampedModel
from resultat.filesettings import MyFileStorage
# Create your models here.
LEVEL1 = 'LEVEL1'
LEVEL2 = 'LEVEL2'
LEVEL3 = 'LEVEL3'
LEVEL4 = 'LEVEL4'
CHOICES = [
        (LEVEL1, 'Collège'),
        (LEVEL2, 'Tronc Commun'),
        (LEVEL3, '1ère année bac'),
        (LEVEL4, 'Default'),
    ]


class Matiere(models.Model):
    name = models.CharField(max_length=255)
 
    class Meta:
            verbose_name_plural="Matières"
            ordering = ["id"]
    
    def __str__(self):
        return self.name


class ResulatSA(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True,null=True)
    pourcentage_log = models.FloatField(blank=True,null=True)

    class Meta:
            verbose_name_plural="Secteurs d'activités"
            ordering = ["id"]
    
    def __str__(self):
        return self.name
        

class Resultat(TimeStampedModel):
    
    mfs = MyFileStorage()
    secteur_activites = models.ForeignKey(ResulatSA,on_delete=models.CASCADE,related_name='resultats',blank=True,null=True)
    membre = models.ForeignKey(Profile,on_delete=models.CASCADE,related_name='resultats')
    test = models.ForeignKey(Test,on_delete=models.CASCADE,related_name="resultats")
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True,null=True)
    #persona
    imagePdf =  models.FileField(storage = mfs,upload_to='staticfiles/assets/images/results/',blank=True,null=True)

    class Meta:
            verbose_name_plural="resultats"
            ordering = ["id"]
    
    def __str__(self):
        return self.name
        

class ResulatMetier(models.Model):
    name = models.CharField(max_length=255,blank=True,null=True)
    metier1= models.CharField(max_length=255,blank=True,null=True)
    metier2= models.CharField(max_length=255,blank=True,null=True)
    metier3= models.CharField(max_length=255,blank=True,null=True)
    
    level_algo = models.CharField(
        max_length=265,
        choices=CHOICES,
        default=LEVEL4, blank=True,null=True
    )

    matieres = models.ManyToManyField(
        'Matiere', related_name='resultatmetiers'
    )

    description = models.TextField(blank=True,null=True)


    class Meta:
            verbose_name_plural="Metiers"
            ordering = ["id"]
    
    def __str__(self):
        return self.name
        



class ResulataPersona(models.Model):
    resultat_persona= models.ForeignKey(Resultat,models.CASCADE,related_name='resultatpersonna')
    name = models.CharField(max_length=255)
    pourcentage = models.FloatField(blank=True,null=True)
    description = models.TextField(blank=True,null=True)


    class Meta:
            verbose_name_plural="Personna"
            ordering = ["id"]
    
    def __str__(self):
        return self.name
        
  
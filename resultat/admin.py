from django.contrib import admin
from resultat.models import Resultat,ResulatMetier,ResulataPersona, ResulatSA, Matiere
from import_export import resources
from import_export.admin import ImportExportActionModelAdmin


class ResultatResource(resources.ModelResource):

    class Meta:
        model = Resultat
        skip_unchanged = True
        report_skipped = False
        fields = ('id', 'membre__fullName', 'membre__date', 'membre__city', 'membre__branch', 'membre__school', 'membre__tel', 'pratique', 'methodique',
                  'entreprenant', 'social', 'creatif', 'investigateur', 'metier1', 'metier2', 'metier3', 'metier4', 'metier5', 'metier6'
                  , 'metier7', 'metier8', 'metier9', 'metier10', 'metier11', 'metier12', 'metier13', 'metier13', 'metier14' )

# Register your models here.


class ResultatAdmin(ImportExportActionModelAdmin):
    resource_class = ResultatResource
    list_display = [field.name for field in Resultat._meta.fields]


class ResulatMetierAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ResulatMetier._meta.fields]
    filter_horizontal=("matieres",)



class ResulataPersonaAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ResulataPersona._meta.fields]


class ResulatSAAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ResulatSA._meta.fields]


class MatiereAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Matiere._meta.fields]


admin.site.register(Matiere, MatiereAdmin)
admin.site.register(Resultat, ResultatAdmin)
admin.site.register(ResulatSA, ResulatSAAdmin)
admin.site.register(ResulatMetier, ResulatMetierAdmin)
admin.site.register(ResulataPersona, ResulataPersonaAdmin)

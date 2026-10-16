from django.contrib import admin
from .models import Atleta, Equipe, Modalidade, Tecnico


# o tecnico deve ser cadasreado dentro do cadastro da equipe
class TecnicoInline(admin.TabularInline):
    model = Atleta


@admin.register(Modalidade)
class ModalidadeAdmin(admin.ModelAdmin):
    ...


@admin.register(Equipe)
class EquipeAdmin(admin.ModelAdmin):
    list_display = ['nome', 'curso']
    #inlines = [TecnicoInline]


@admin.register(Tecnico)
class TecnicoAdmin(admin.ModelAdmin):
    ...


@admin.register(Atleta)
class AtletaAdmin(admin.ModelAdmin):
    list_display = ['nome', 'matricula', 'equipe']
    list_filter = ['equipe', 'modalidades']
    search_fields = ['nome']
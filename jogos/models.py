from django.db import models

# Create your models here.
class Modalidade(models.Model):
    nome = models.CharField(max_length=100,unique=True)
    tipo = models.CharField(choices={
        ('coletiva','coletiva'),
        ('individual','individual')
    })
    max_atletas = models.PositiveIntegerField()
    #atletas = models.ManyToManyField("Atleta", blank=True, related_name="modalidades")
    class Meta:
        verbose_name = 'Modalidade'
        verbose_name_plural = 'Modalidades'
        ordering = ["nome"]

    def __str__(self):
        return self.nome

class Equipe(models.Model):
    nome = models.CharField(max_length=100,unique=True)
    curso = models.CharField(max_length=50)
    cor = models.CharField(max_length=50)
    criada_em = models.DateTimeField(auto_now_add=True)
    tecnico = models.OneToOneField("Tecnico",on_delete=models.CASCADE,related_name="tecnicos")
    

    class Meta:
        verbose_name = 'Equipe'
        verbose_name_plural = 'Equipes'
        ordering = ["nome"]

    def __str__(self):
        return self.nome

class Tecnico(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    telefone = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Tecnico'
        verbose_name_plural = 'Tecnicos'

    def __str__(self):
        return self.nome

class Atleta(models.Model):
    nome = models.CharField(max_length=100)
    matricula = models.CharField(max_length=100, unique=True)
    data_nascimento = models.DateField()
    equipe = models.ForeignKey("Equipe",on_delete=models.PROTECT)
    modalidades = models.ManyToManyField("Modalidade",null=True,related_name="atletas")


    class Meta:
        verbose_name = 'Atleta'
        verbose_name_plural = 'Atletas'
        ordering = ["nome"]

    def __str__(self):
        return self.nome
    


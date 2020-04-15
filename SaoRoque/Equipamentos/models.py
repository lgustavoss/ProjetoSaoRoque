from django.db import models


# Create your models here.
# Aqui começam os cadatros
# Classe colaborador
class Colaborador(models.Model):
    nome = models.CharField(max_length=50)
    funcao = models.CharField(max_length=10)

    class Meta:
        ordering = ['nome']
        verbose_name = "Colaborador"
        verbose_name_plural = "Colaboradores"

    def __str__(self):
        return self.nome


# Classe Estabelecimento
class Estabelecimento(models.Model):
    nome = models.CharField(max_length=50)
    cnpj = models.CharField(max_length=20, help_text="Ex.: 00.000.00/0000-00")

    class Meta:
        ordering = ['nome']
        verbose_name = "Estabelecimento"

    def __str__(self):
        return self.nome


# Classe Computador
class Computador(models.Model):
    TIPO_CHOICES = (
        ('desktop', 'Desktop'),
        ('notebook', 'Notebook'),
    )
    tipo = models.CharField(max_length=10, choices=TIPO_CHOICES)
    colaborador = models.ForeignKey(Colaborador, on_delete=models.PROTECT)
    estabelecimento = models.ForeignKey(Estabelecimento, on_delete=models.PROTECT)
    marca = models.CharField(max_length=15)
    modelo = models.CharField(max_length=15)
    processador = models.CharField(max_length=15)
    memoria = models.CharField(max_length=15)
    armazenamento = models.CharField(max_length=20)
    service_tag = models.CharField(max_length=15, unique=True)
    observacoes = models.TextField(null=True, blank=True)

    class Meta:
        ordering = ['tipo', 'colaborador']
        verbose_name = "Computador"
        verbose_name_plural = "Computadores"

    def __str__(self):
        return self.tipo


# Classe Dispositivos
class Dispositivos(models.Model):
    TIPO_COICES = (
        ('mouse', 'Mouse'),
        ('teclado', 'Teclado'),
        ('impressora', 'Impressora'),
        ('scanner', 'Scanner'),
        ('switch', 'Switch'),
        ('roteador', 'Roteador'),
    )
    tipo = models.CharField(max_length=15, choices=TIPO_COICES)
    colaborador = models.ForeignKey(Colaborador, on_delete=models.PROTECT)
    estabelecimento = models.ForeignKey(Estabelecimento, on_delete=models.PROTECT)
    marca = models.CharField(max_length=15)
    modelo = models.CharField(max_length=15)
    service_tag = models.CharField(max_length=15, unique=True)
    observacoes = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = "Dispositivo"

    def __str__(self):
        return self.tipo


# Classe Adquirentes
class Adquirentes(models.Model):
    adquirente = models.CharField(max_length=20, unique=True)

    class Meta:
        verbose_name = "Adquirente"

    def __str__(self):
        return self.adquirente


# Classe Maquininha
class Maquininha(models.Model):
    TIPO_CHOICES = (
        ('sitef', 'Sitef'),
        ('pos', 'POS'),
        ('sitef_fixa', 'Sitef Fixa'),
        ('pos_fixa', 'POS Fixa'),
    )

    STATUS_CHOICES = (
        ('Ativo', 'Ativo'),
        ('Inativo', 'Inativo'),
    )

    tipo = models.CharField(max_length=10, null=False, choices=TIPO_CHOICES)
    adquirente = models.ForeignKey(Adquirentes, on_delete=models.PROTECT)
    estabelecimento = models.ForeignKey(Estabelecimento, on_delete=models.PROTECT)
    n_serie = models.IntegerField(null=False, unique=True)
    n_logico = models.CharField(max_length=10, unique=True)
    mensalidade = models.FloatField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)
    data_ativacao = models.DateField()
    data_inativacao = models.DateField(blank=True, null=True)
    observacoes = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = "Maquininha"

    def __str__(self):
        return self.tipo

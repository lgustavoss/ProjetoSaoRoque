from django.db import models


# Create your models here.
# Aqui começam os cadatros
# Classe colaborador
class Colaborador(models.Model):
    nome = models.CharField(max_length=50, help_text="Informe o nome do colaborador.")
    funcao = models.CharField(max_length=10, help_text="Informe a função do colaborador.")

    class Meta:
        ordering = ['nome']
        verbose_name = "Colaborador"
        verbose_name_plural = "Colaboradores"

    def __str__(self):
        return self.nome


# Classe Estabelecimento
class Estabelecimento(models.Model):
    nome = models.CharField(max_length=50, help_text="Informe o nome do estabelecimento.")
    cnpj = models.CharField(max_length=20, help_text="Informe o cnpj (00.000.00/0000-00)")

    class Meta:
        ordering = ['nome']
        verbose_name = "Estabelecimento"

    def __str__(self):
        return self.nome


# Classe Computador
class Computador(models.Model):
    TIPO_CHOICES = (
        ('desktop', 'Desktop'),
        ('notebook', 'notebook'),
    )
    tipo = models.CharField(max_length=10, choices=TIPO_CHOICES)
    colaborador = models.ForeignKey(Colaborador, on_delete=models.PROTECT)
    estabelecimento = models.ForeignKey(Estabelecimento, on_delete=models.PROTECT)
    marca = models.CharField(max_length=15, help_text="Informe a marca do equipamento.")
    modelo = models.CharField(max_length=15, help_text="Informe o modelo do equipamento.")
    processador = models.CharField(max_length=15, help_text="Informe o processador do equipamento.")
    memoria = models.CharField(max_length=15, help_text="Informe a memódia do equipamento.")
    armazenamento = models.CharField(max_length=20, help_text="Informe a capacidade de armazenamento do equipamento.")
    service_tag = models.CharField(max_length=15, unique=True, help_text="Informe a Service TAG do equipamento.")
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
    marca = models.CharField(max_length=15, help_text="Informe a marca do equipamento.")
    modelo = models.CharField(max_length=15, help_text="Informe o modelo do equipamento.")
    service_tag = models.CharField(max_length=15, unique=True, help_text="Informe a Service TAG do equipamento.")
    observacoes = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = "Dispositivo"

    def __str__(self):
        return self.tipo


# Classe Adquirentes
class Adquirentes(models.Model):
    adquirente = models.CharField(max_length=20, unique=True, help_text="Informe aqui a adquirente.")

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
        ('ativo', 'Ativo'),
        ('inativo', 'Inativo'),
    )

    tipo = models.CharField(max_length=10, null=False, choices=TIPO_CHOICES)
    adquirente = models.ForeignKey(Adquirentes, on_delete=models.PROTECT)
    estabelecimento = models.ForeignKey(Estabelecimento, on_delete=models.PROTECT)
    n_serie = models.IntegerField(null=False, unique=True, help_text="Informe o Nº de serie.")
    n_logico = models.CharField(max_length=10, unique=True, help_text="Informe o nº da etiqueta do verso.")
    mensalidade = models.FloatField(help_text="Informe o valor da mensalidade")
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)
    data_ativacao = models.DateField(help_text="Informe a data de Ativação.")
    data_inativacao = models.DateField(blank=True, null=True, help_text="Informe a data de Inativação.")
    observacoes = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = "Maquininha"

    def __str__(self):
        return self.tipo

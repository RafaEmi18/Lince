from django.db import models


class InformeTrimestral(models.Model):

    class Trimestre(models.TextChoices):
        ENERO_MARZO = 'ene-mar','Enero-Marzo'
        ABRIL_JUNIO = 'abr-jun','Abril-Junio'
        JULIO_SEPTIEMBRE = 'jul-sep','Julio-Septiembre'
        OCTUBRE_DICIEMBRE = 'oct-dic','Octubre-Diciembre'

    id = models.AutoField(primary_key=True)
    work_area=models.CharField(max_length=100) 
    trimester = models.CharField(
        max_length=7,
        choices=Trimestre.choices,
        default=Trimestre.ENERO_MARZO,
    )
    year = models.IntegerField()
    month= models.CharField(max_length=20)
    pide = models.CharField(max_length=150)
    cacei= models.CharField(max_length=200)

    


    created_by = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    vo_bo = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return f"Informe {self.trimester} {self.year} - {self.work_area}"




class Action(models.Model):
    id= models.AutoField(primary_key=True)

    informe_trimestral= models.ForeignKey(
        InformeTrimestral,
        on_delete=models.CASCADE,
        related_name='actions'
    )

    action_num=models.CharField(max_length=10)

    is_specific = models.BooleanField(default=True)
    description = models.TextField()
    planificated = models.IntegerField()
    finalized = models.IntegerField()
    cumpliment_percent = models.DecimalField(max_digits=5, decimal_places=2)
    incumpliment_justification = models.TextField()
    activity_impact = models.TextField()

    detach = models.BooleanField(default=False)
    action_date=models.DateTimeField()
    photograpi_url=models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return f"Action {self.id} - {self.informe_trimestral.description}"



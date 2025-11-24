from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils import timezone


class InformeTrimestral(models.Model):

    class Trimestre(models.TextChoices):
        ENERO_MARZO = 'ene-mar','Enero-Marzo'
        ABRIL_JUNIO = 'abr-jun','Abril-Junio'
        JULIO_SEPTIEMBRE = 'jul-sep','Julio-Septiembre'
        OCTUBRE_DICIEMBRE = 'oct-dic','Octubre-Diciembre'

    id = models.AutoField(primary_key=True)
    work_area = models.CharField(
        max_length=100,
        verbose_name='Área de trabajo',
        help_text='Área o departamento responsable del informe'
    )
    trimester = models.CharField(
        max_length=7,
        choices=Trimestre.choices,
        default=Trimestre.ENERO_MARZO,
        verbose_name='Trimestre'
    )
    year = models.IntegerField(
        verbose_name='Año',
        validators=[
            MinValueValidator(2000),
            MaxValueValidator(2100)
        ]
    )
    month = models.CharField(
        max_length=20,
        verbose_name='Mes',
        help_text='Mes del informe'
    )
    pide = models.CharField(
        max_length=150,
        verbose_name='PIDE',
        help_text='Plan Integral de Desarrollo Educativo'
    )
    cacei = models.CharField(
        max_length=200,
        verbose_name='CACEI',
        help_text='Consejo de Acreditación de la Enseñanza de la Ingeniería'
    )

    created_by = models.CharField(
        max_length=100,
        verbose_name='Creado por'
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Fecha de creación'
    )
    updated_by = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        verbose_name='Actualizado por'
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name='Fecha de actualización'
    )
    vo_bo = models.CharField(
        max_length=50,
        null=True,
        blank=True,
        verbose_name='Visto bueno',
        help_text='Aprobación o visto bueno del informe'
    )

    class Meta:
        verbose_name = 'Informe Trimestral'
        verbose_name_plural = 'Informes Trimestrales'
        ordering = ['-year', '-trimester', 'work_area']
        unique_together = ['work_area', 'trimester', 'year']

    def __str__(self):
        return f"Informe {self.trimester} {self.year} - {self.work_area}"



class Action(models.Model):
    id = models.AutoField(primary_key=True)

    informe_trimestral = models.ForeignKey(
        InformeTrimestral,
        on_delete=models.CASCADE,
        related_name='actions',
        verbose_name='Informe Trimestral'
    )

    action_num = models.CharField(
        max_length=10,
        verbose_name='Número de acción',
        help_text='Número o código identificador de la acción'
    )

    is_specific = models.BooleanField(
        default=True,
        verbose_name='Es específica',
        help_text='Indica si la acción es específica o general'
    )
    description = models.TextField(
        verbose_name='Descripción',
        help_text='Descripción detallada de la acción'
    )
    planificated = models.IntegerField(
        verbose_name='Planificado',
        validators=[MinValueValidator(0)],
        help_text='Cantidad planificada para esta acción'
    )
    finalized = models.IntegerField(
        verbose_name='Finalizado',
        validators=[MinValueValidator(0)],
        help_text='Cantidad finalizada de esta acción'
    )
    cumpliment_percent = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        verbose_name='Porcentaje de cumplimiento',
        validators=[
            MinValueValidator(0),
            MaxValueValidator(100)
        ],
        help_text='Porcentaje de cumplimiento de la acción (0-100)'
    )
    incumpliment_justification = models.TextField(
        verbose_name='Justificación de incumplimiento',
        blank=True,
        null=True,
        help_text='Justificación en caso de incumplimiento'
    )
    activity_impact = models.TextField(
        verbose_name='Impacto de la actividad',
        help_text='Descripción del impacto de esta actividad'
    )

    detach = models.BooleanField(
        default=False,
        verbose_name='Desvinculado',
        help_text='Indica si la acción está desvinculada del informe'
    )
    action_date = models.DateTimeField(
        verbose_name='Fecha de la acción'
    )
    photography_url = models.URLField(
        max_length=500,
        null=True,
        blank=True,
        verbose_name='URL de fotografía',
        help_text='URL de la fotografía relacionada con la acción'
    )

    created_at = models.DateTimeField(
        default=timezone.now,
        verbose_name='Fecha de creación'
    )
    updated_at = models.DateTimeField(
        default=timezone.now,
        verbose_name='Fecha de actualización'
    )

    class Meta:
        verbose_name = 'Acción'
        verbose_name_plural = 'Acciones'
        ordering = ['informe_trimestral', 'action_num']
        indexes = [
            models.Index(fields=['informe_trimestral', 'action_num']),
            models.Index(fields=['action_date']),
        ]

    def __str__(self):
        return f"Acción {self.action_num} - {self.informe_trimestral}"

    def save(self, *args, **kwargs):
        # Calcular porcentaje de cumplimiento automáticamente si hay valores
        if self.planificated > 0:
            self.cumpliment_percent = (self.finalized / self.planificated) * 100
        
        # Actualizar updated_at si el objeto ya existe
        if self.pk:
            self.updated_at = timezone.now()
        # Si es un nuevo objeto y no tiene created_at, establecerlo
        elif not self.created_at:
            self.created_at = timezone.now()
            self.updated_at = timezone.now()
        
        super().save(*args, **kwargs)

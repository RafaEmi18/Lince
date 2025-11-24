from django.contrib import admin
from .models import InformeTrimestral, Action


@admin.register(InformeTrimestral)
class InformeTrimestralAdmin(admin.ModelAdmin):
    list_display = ['id', 'work_area', 'trimester', 'year', 'month', 'created_by', 'created_at', 'vo_bo']
    list_filter = ['trimester', 'year', 'work_area', 'created_at']
    search_fields = ['work_area', 'pide', 'cacei', 'created_by']
    readonly_fields = ['created_at', 'updated_at']
    fieldsets = (
        ('Información General', {
            'fields': ('work_area', 'trimester', 'year', 'month')
        }),
        ('Documentación', {
            'fields': ('pide', 'cacei')
        }),
        ('Auditoría', {
            'fields': ('created_by', 'created_at', 'updated_by', 'updated_at', 'vo_bo')
        }),
    )


@admin.register(Action)
class ActionAdmin(admin.ModelAdmin):
    list_display = ['id', 'action_num', 'informe_trimestral', 'is_specific', 'planificated', 'finalized', 'cumpliment_percent', 'action_date', 'detach']
    list_filter = ['is_specific', 'detach', 'action_date', 'informe_trimestral']
    search_fields = ['action_num', 'description', 'activity_impact']
    readonly_fields = ['created_at', 'updated_at', 'cumpliment_percent']
    fieldsets = (
        ('Información de la Acción', {
            'fields': ('informe_trimestral', 'action_num', 'is_specific', 'description')
        }),
        ('Cumplimiento', {
            'fields': ('planificated', 'finalized', 'cumpliment_percent', 'incumpliment_justification')
        }),
        ('Impacto y Detalles', {
            'fields': ('activity_impact', 'action_date', 'photography_url', 'detach')
        }),
        ('Auditoría', {
            'fields': ('created_at', 'updated_at')
        }),
    )
    raw_id_fields = ['informe_trimestral']

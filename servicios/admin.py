from django.contrib import admin
from .models import Servicio

# Register your models here.

#hay que espicificar que aparezca created y modificated ya que se reyenan automaticamente
class ServicioAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

admin.site.register(Servicio, ServicioAdmin)
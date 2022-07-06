from django.contrib import admin
from Modulos.Academica.models import *

from universidad.MiUniversidad.Modulos.Academica.models import Carrera, Estudiante

# Register your models here.

admin.site.register(Carrera)
admin.site.register(Estudiante)
admin.site.register(Curso)
admin.site.register(Matricula)



from django.db import models

# Create your models here.
class CategoriaProdu(models.Model):
    nombre = models.CharField(max_length= 70)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name='categoriaProd'
        verbose_name_plural='categoriasProd'

    def __str__(self):
        return self.nombre
    

class Producto (models.Model):
    nombre = models.CharField(max_length=70)
    categoria=models.ForeignKey(CategoriaProdu, on_delete=models.CASCADE)
    descripcion = models.CharField(max_length=200)
    imagen = models.ImageField(upload_to='tienda', null=True, blank=True)
    precio = models.FloatField(default=20)
    disponibilidad = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name='producto'
        verbose_name_plural='productos'

    def __str__(self):
        return self.nombre
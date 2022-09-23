from django.shortcuts import render

from .models import CategoriaProdu, Producto

# Create your views here.
def tienda(request):
    productos = Producto.objects.all()
    return render(request, 'tienda/tienda.html',{'productos':productos})

def categoria(request, categoria_id):
    categoria=CategoriaProdu.objects.get(id=categoria_id)
    producto=Producto.objects.filter(categorias=categoria)
    return  render(request, 'tienda/categoria.html', {'categoria': categoria, 'producto':producto})   
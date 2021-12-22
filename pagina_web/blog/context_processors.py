from .categorias import categorias

def categorias_to_base(request):        
    return {'categorias': categorias}
from .models import Menu

def get_menu(request):
    return {'navigation':Menu.objects.get(slug="x")}
from .models import Navbar

def get_navbar(request):
    if(Navbar.objects.exists()):
        return {'nav_tabs': Navbar.objects.first().nav_items.all()}
    return {'nav_tabs':None}
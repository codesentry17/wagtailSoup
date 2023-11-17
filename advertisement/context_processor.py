from .models import Advertisement
import random

def extras(request):

    ads = Advertisement.objects
    
    return {
        "ads": ads.all(),
        "adId": 0 if ads.count() == 0 else random.randint(1,ads.count())
    }
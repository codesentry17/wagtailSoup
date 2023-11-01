from .models import Advertisement
import random

def extras(request):

    ads = Advertisement.objects
    if ads.count() == 0:
        adId = 0
    else:
        adId = random.randint(1,ads.count())

    return {
        "ads": ads.all(),
        "adId": adId
    }
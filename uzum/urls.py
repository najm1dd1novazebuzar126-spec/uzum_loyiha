from django.urls import path
from .views import *

urlpatterns = [
    path("", splash, name="splash"),
    path('home/', home, name='home'),
    path("nav/", navigation, name="navigation"),
    path("footer/", footer, name="footer"),
    path("sotuvchi_bolish/", sotuvchi_bolish, name="sotuvchi"),
    path("sotuvchi_login/", sotuvchi_login, name="sotuvchi_login"),
    path("sotuvchi_register/", sotuvchi_register, name="sotuvchi_register"),
    path("topshirish_punkitini_ochish/", topshirish_punkitini_ochish, name="topshirish_punkitini_ochish"),
    path("savol/", savol_javob, name="savol_javob"),
    path("salom/", salom, name="salom"), 
    path("savdo/", savdo, name="savdo"),
    path("detail/<int:tovar_id>/", detail, name="detail"),

]
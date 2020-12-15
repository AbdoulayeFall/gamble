from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.compte, name="compte"),
    path('<slug:user_id>',views.profile, name="profile"),
    path('accepter/<str:pari_type>/<int:pari_id>',views.accepter, name="accepter"),
    path('refuser/<str:pari_type>/<int:pari_id>',views.refuser, name="refuser"),
    path('<str:pari_type>/<slug:user_id>/<int:pari_id>',views.invite, name="invite"),
    path('parier/<str:pari_type>/<slug:user_id>/<int:pari_id>',views.parier, name="parier"),
    path('resultat/<str:pari_type>/<slug:user_id>/<int:pari_id>',views.resultat, name="resultat"),
]

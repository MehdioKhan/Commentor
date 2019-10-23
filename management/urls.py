from rest_framework.routers import DefaultRouter
from . import views
from django.urls import path,include

app_name = 'management'

router = DefaultRouter()

router.register(r'sites',views.SiteView)
router.register(r'configurations',views.ConfigurationView)
router.register(r'moderation',views.ModerationView)


urlpatterns = [
    path('', include(router.urls)),
]
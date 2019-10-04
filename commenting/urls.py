from django.urls import path
from rest_framework.routers import SimpleRouter
from . import views

app_name = 'commenting'

router = SimpleRouter()
router.register('comments',views.CommentViewSet)

urlpatterns = router.urls
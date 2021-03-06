from django.conf.urls import url
from django.contrib import admin
from rest_framework.documentation import include_docs_urls
from rest_framework_mongoengine import routers
from microservice import views


router = routers.DefaultRouter(trailing_slash=False)
router.register(r"user/auth", views.UserAuthView)
router.register(r"user/logout", views.UserLogoutView)
router.register(r"user/article", views.ArticleView)
router.register(r"article/like", views.ArticleLikeView)
router.register(r"user", views.UserView)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^docs/', include_docs_urls(title='Articles API')),
]

urlpatterns += router.urls

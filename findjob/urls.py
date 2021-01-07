from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from . import views
from .views import ProfileAPIView, JobpostAPIView, ReviewsAPIView, RoleAPIView, singleprofile

urlpatterns = [
    # path('auth/', include('djoser.urls')),
    # path('auth/', include('djoser.urls.authtoken')),
    path('dj-rest-auth/', include('dj_rest_auth.urls')),
    path('dj-rest-auth/registration/', include('dj_rest_auth.registration.urls')),
    path('api/viewprofile/<str:pk>/', views.singleprofile, name='singleprofile'),
    path('api/jobposts/', JobpostAPIView.as_view()),
    path('api/reviews/', ReviewsAPIView.as_view()), 
    path('api/role/', RoleAPIView.as_view())
    ]

# if settings.DEBUG:
#     urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
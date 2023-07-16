from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views


from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('teacher/', views.teacher_list),
    path('teacher/<str:user_name>/', views.teacher_detail),

    path('token/', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .views import RegisterView, PatientListCreateView, PatientDetailView, DoctorListCreateView, DoctorDetailView, MappingListCreateView, MappingByPatientView, MappingDeleteView

urlpatterns = [
    #Authentication APIs
    path('auth/register/', RegisterView.as_view(), name='register'),
    path('auth/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    #Patient Management APIs
    path('patients/', PatientListCreateView.as_view(), name='patient-list-create'),
    path('patients/<int:pk>/', PatientDetailView.as_view(), name='patient-detail'),
    #Doctor Management APIs
    path('doctors/', DoctorListCreateView.as_view(), name='doctor-list-create'),
    path('doctors/<int:pk>/', DoctorDetailView.as_view(), name='doctor-detail'),
    #Patient-Doctor Mapping APIs
    path('mappings/', MappingListCreateView.as_view(), name='mapping-list-create'),
    path('mappings/patient/<int:pk>/', MappingByPatientView.as_view(), name='mapping-by-patient'),
    path('mappings/<int:pk>/', MappingDeleteView.as_view(), name='mapping-delete'),
]

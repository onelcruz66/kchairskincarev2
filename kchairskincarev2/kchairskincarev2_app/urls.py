from django.urls import path
from . import views
from .views import CustomLoginView

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('pricing/', views.pricing, name='pricing'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('team/', views.team, name='team'),
    path('post/', views.post, name='post'),
    path('faq/', views.faq, name='faq'),
    path('services-page/', views.services_page, name='services_page'),
    path('team-details/', views.team_details, name='team_details'),
    path('error-404/', views.error_404, name='error_404'),
    path('coming-soon/', views.coming_soon, name='coming_soon'),
    path('blog/', views.blog, name='blog'),
    path('blog2/', views.blog2, name='blog2'),
    path('blog3/', views.blog3, name='blog3'),
    path('contact/', views.contact, name='contact'),
    path('login/', CustomLoginView.as_view(), name='login'),
]

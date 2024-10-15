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
    path('auth/login/', CustomLoginView.as_view(), name='login'),
    path('auth/logout/', views.logout, name='logout'),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("requested-appointments/", views.requested_appointments, name="requested_appointments"),
    path("approved-appointments/", views.approved_appointments, name="approved_appointments"),
    path("message-requests/", views.message_requests, name="message_requests"),
    path("register-user/", views.register_user, name="register_user"),
    path("email-subscribers/", views.email_subscribers, name="email_subscribers"),
    path("contact-info/", views.contact_info, name="contact_info"),
]

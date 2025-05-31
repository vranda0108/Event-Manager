from django.urls import path, include
from django.views.generic import RedirectView
from . import views

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("index/", RedirectView.as_view(url="/", permanent=True)),

    path("edit-event/<int:pk>/", views.EditEvent, name="edit_event"),
    path("delete-event/<int:pk>/", views.DeleteEvent, name="delete_event"),

    path("delete_review/<int:pk>/", views.DeleteReview, name="delete_review"),
    path("edit_review/<int:pk>/", views.EditReview, name="edit_review"),

    path("dash/", views.DashView.as_view(), name="dash"),
    path("login/", views.LoginView, name="login"),
    path("register/", views.RegisterView, name="register"),
    path("logout/", views.LogoutView, name="logout"),
    path("profile/", views.ProfileView, name="profile"),
    path('profile/edit/', views.edit_profile, name='edit_profile'),

    path("add-event/", views.AddEvent, name="add-event"),
    path("buy-ticket/<int:pk>/", views.BuyTicket, name="buy-ticket"),
    path("details/<int:pk>/", views.PublicDetails, name="details"),
    path("review/<int:pk>/", views.AddReview, name="add-review"),

    path('api/', include('events.urls_api')),
]

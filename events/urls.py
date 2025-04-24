from django.urls import path
from django.views.generic import RedirectView  # For redirecting /index to /
from . import views

urlpatterns = [
    # Index page routes
    path("", views.IndexView.as_view(), name="index"),
    path("index/", RedirectView.as_view(url="/", permanent=True)),  # Redirect /index to /

    # Event management routes
    path("edit-event/<int:pk>/", views.EditEvent, name="edit_event"),
    path("delete-event/<int:pk>/", views.DeleteEvent, name="delete_event"),

    # Review management routes
    path("delete_review/<int:pk>/", views.DeleteReview, name="delete_review"),
    path("edit_review/<int:pk>/", views.EditReview, name="edit_review"),

    # Dashboard and authentication routes
    path("dash/", views.DashView.as_view(), name="dash"),
    path("login/", views.LoginView, name="login"),
    path("register/", views.RegisterView, name="register"),
    path("logout/", views.LogoutView, name="logout"),
    path("profile/", views.ProfileView, name="profile"),

    # Event creation and ticket routes
    path("add-event/", views.AddEvent, name="add-event"),
    path("buy-ticket/<int:pk>/", views.BuyTicket, name="buy-ticket"),

    # Event details and review routes
    path("details/<int:pk>/", views.PublicDetails, name="details"),
    path("review/<int:pk>/", views.AddReview, name="add-review"),
]

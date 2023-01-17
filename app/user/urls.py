from django.urls import path
from user import views

# this is used in the reverse function in the tests
app_name = "user"

urlpatterns = [
    path("create/", views.CreateUserView.as_view(), name="create"),
]

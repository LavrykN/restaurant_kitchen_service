from django.urls import path

from kitchen.views import DishListView, DishCreateView, DishUpdateView, DishDeleteView, index

urlpatterns = [
    path("", index, name="index"),
    path(
        "dish/",
        DishListView.as_view(),
        name="kitchen-list",
    ),
    path(
        "dish/create/",
        DishCreateView.as_view(),
        name="kitchen-create",
    ),
    path(
        "dish/<int:pk>/update/",
        DishUpdateView.as_view(),
        name="kitchen-update",
    ),
    path(
        "dish/<int:pk>/delete/",
        DishDeleteView.as_view(),
        name="kitchen-delete",
    ),
]

app_name = "kitchen"

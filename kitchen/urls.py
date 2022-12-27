from django.urls import path

from kitchen.views import (
    index,
    DishListView,
    DishCreateView,
    DishUpdateView,
    DishDeleteView,
    CookListView,
    CookUpdateView,
    CookCreateView,
    CookDeleteView,
)

urlpatterns = [
    path("", index, name="index"),
    path(
        "dish/",
        DishListView.as_view(),
        name="dish-list",
    ),
    path(
        "dish/create/",
        DishCreateView.as_view(),
        name="dish-create",
    ),
    path(
        "dish/<int:pk>/update/",
        DishUpdateView.as_view(),
        name="dish-update",
    ),
    path(
        "dish/<int:pk>/delete/",
        DishDeleteView.as_view(),
        name="dish-delete",
    ),
    path(
        "cook/",
        CookListView.as_view(),
        name="cook-list",
    ),
    path(
        "cook/create/",
        CookCreateView.as_view(),
        name="cook-create",
    ),
    path(
        "cook/<int:pk>/update/",
        CookUpdateView.as_view(),
        name="cook-update",
    ),
    path(
        "cook/<int:pk>/delete/",
        CookDeleteView.as_view(),
        name="cook-delete",
    ),
]

app_name = "kitchen"

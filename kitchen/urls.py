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
    DishTypeListView,
    DishTypeCreateView,
    DishTypeUpdateView,
    DishTypeDeleteView, CookDetailView,
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
        "cook/<int:pk>/",
        CookDetailView.as_view(),
        name="cook-detail",
    ),
    path(
        "cook/<int:pk>/delete/",
        CookDeleteView.as_view(),
        name="cook-delete",
    ),
    path(
        "dish-type/",
        DishTypeListView.as_view(),
        name="dish-type-list",
    ),
    path(
        "dish-type/create/",
        DishTypeCreateView.as_view(),
        name="dish-type-create",
    ),
    path(
        "dish-type/<int:pk>/update/",
        DishTypeUpdateView.as_view(),
        name="dish-type-update",
    ),
    path(
        "dish-type/<int:pk>/delete/",
        DishTypeDeleteView.as_view(),
        name="dish-type-delete",
    ),
]

app_name = "kitchen"

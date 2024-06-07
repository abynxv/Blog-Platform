from django.urls import path
from . views import *

urlpatterns = [
    path('blog/', BlogView.as_view()),
    path('blog/<int:pk>/', BlogDetailView.as_view()),
    path('blog/<int:pk>/comment/', CommentView.as_view()),
    path('blog/authors/', AuthorView.as_view()),
    path('blog/authors/<int:pk>/', AuthorDetailView.as_view()),
]

from rest_framework import generics, status, filters
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.shortcuts import get_object_or_404
from rest_framework.response import Response

from .models import Recipe, RecipeLike
from .serializers import RecipeLikeSerializer, RecipeSerializer
from .permissions import IsAuthorOrReadOnly

class RecipeListAPIView(generics.ListAPIView):
    """
    Get: a collection of recipes
    """ 
    serializer_class = RecipeSerializer
    permission_classes = (AllowAny,)
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'desc', 'ingredients', 'procedure', 'author__username', 'category__name']
    filterset_fields = ('category__name', 'author__username', 'bookmarked_by__user__username')
    
    def get_queryset(self):
        queryset = Recipe.objects.all()
            
        bookmarked_username = self.request.query_params.get('bookmarked_by__user__username')
        if bookmarked_username:
            queryset = queryset \
                                .filter(bookmarked_by__user__username=bookmarked_username) \
                                .prefetch_related('bookmarked_by__user')
            
        author_username = self.request.query_params.get('author__username')
        if author_username:
            queryset = queryset.filter(author__username=author_username)

        limit = self.request.query_params.get('limit')
        if limit and limit.isdigit():
            limit = int(limit)
            if limit > 0:
                queryset = queryset[:limit]
            
        return queryset 
    
    
class RecipeCreateAPIView(generics.CreateAPIView):
    """
    Create: a recipe
    """
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
        
    
class RecipeAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
    Get, Update, Delete a recipe
    """
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    permission_classes = (IsAuthorOrReadOnly,)
    
    
class RecipeLikeAPIView(generics.CreateAPIView):
    """
    Like, Dislike a recipe
    """
    serializer_class = RecipeLikeSerializer
    permission_classes = (IsAuthenticated,)

    def post(self, request, pk):
        recipe = get_object_or_404(Recipe, id=self.kwargs['pk'])
        new_like, created = RecipeLike.objects.get_or_create(
            user=request.user, recipe=recipe)
        if created:
            new_like.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        recipe = get_object_or_404(Recipe, id=self.kwargs['pk'])
        like = RecipeLike.objects.filter(user=request.user, recipe=recipe)
        if like.exists():
            like.delete()
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
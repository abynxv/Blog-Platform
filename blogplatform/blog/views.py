from .models import *
from .serializers import *
from rest_framework.decorators import APIView
from rest_framework.response import Response
from rest_framework import status


class BlogView(APIView):
    def get(self, request):
        blogs = BlogPost.objects.all()
        serializer = BlogPostSerializer(blogs, many=True)
        return Response(serializer.data)
    def post(self, request):
        serializer = BlogPostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class BlogDetailView(APIView):
    def get(self, request, pk=None):
        if pk is None:
            blogs = BlogPost.objects.all()
            serializer = BlogPostSerializer(blogs, many=True)
            return Response(serializer.data)
        else:
            try:
                blog = BlogPost.objects.get(pk=pk)  
                serializer = BlogPostSerializer(blog) 
                return Response(serializer.data)
            except BlogPost.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
    def put(self, request, pk):
        try:
            blog = BlogPost.objects.get(pk=pk)
        except BlogPost.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = BlogPostSerializer(blog, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk):
        try:
            blog = BlogPost.objects.get(pk=pk)
        except BlogPost.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        blog.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class AuthorView(APIView):
    def get(self, request):
        authors = BlogAuthor.objects.all()
        serializer = BlogAuthorSerializer(authors, many=True)
        return Response(serializer.data)
    def post(self, request):
        serializer = BlogAuthorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class AuthorDetailView(APIView):
    def get(self, request, pk=None):
        if pk is None:
            authors = BlogAuthor.objects.all()
            serializer = BlogAuthorSerializer(authors, many=True)
            return Response(serializer.data)
        else:
            try:
                author = BlogAuthor.objects.get(pk=pk)
                serializer = BlogAuthorSerializer(author)
                return Response(serializer.data)
            except BlogAuthor.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        try:
            author = BlogAuthor.objects.get(pk=pk)
        except BlogAuthor.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        serializer = BlogAuthorSerializer(author, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        try:
            author = BlogAuthor.objects.get(pk=pk)
        except BlogAuthor.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        author.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
            
class CommentView(APIView):
    def post(self, request, pk=None):
        try:
            blog = BlogPost.objects.get(pk=pk)
        except BlogPost.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = BlogCommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(blog=blog)
            return Response(serializer.data, status=status.HTTP_201_CREATED) 
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


        



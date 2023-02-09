from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response

from .serializers import PostSerializer, GroupSerializer, CommentSerializer
from posts.models import Post, Group, Comment


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    # permission_classes = [IsAuthentificated, UserOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    # permission_classes = (AuthorOrReadOnly,)

    # def get_queryset(self):
    #     # our_post = get_object_or_404(Post, pk=self.kwargs.get('post_id'))
    #     # new_queryset = Comment.objects.filter(post=our_post)
    #     # return new_queryset
    #
    #     new_queryset = self.queryset.filter(post_id=self.kwargs['post_id'])
    #     return new_queryset

    # def get_queryset(self):
    #     post_id = self.kwargs.get("post_id")
    #     new_queryset = Comment.objects.filter(post=post_id)
    #     return new_queryset
    #
    # def create(self, request, post_id):
    #     post_id = self.kwargs.get("post_id")
    #     serializer = CommentSerializer(data=request.data)
    #     if serializer.is_valid(raise_exception=True):
    #         serializer.save(author=request.user,
    #                         post=Post.objects.get(id=post_id))
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)

    def create(self, request, post_id):
        post = Post.objects.get(id=post_id)
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(author=request.user, post=post)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # def perform_create(self, request, post_id):
    #     serializer = CommentSerializer(data=request.data)
    #     post = Post.objects.get(id=post_id)
    #     serializer.save(author=self.request.user, post=post)
    #     return Response(serializer.data, status=status.HTTP_201_CREATED)

from abstract.serializers import BaseSerializer
from .models import Product, Comment

class ProductSerializer(BaseSerializer):
    class Meta:
        fields = ('id', 'category', 'title', 'price', 'description', 'comments')
        model = Product
    
    def serialize_obj(self, obj):
        data = super().serialize_obj(obj)
        data['comments'] = CommentSerializer().serialize_queryset(obj.comments)
        return data

class CommentSerializer(BaseSerializer):
    class Meta:
        fields = ('id', 'user', 'body', 'created_at')
        model = Comment

    def serialize_obj(self, obj):
        data = super().serialize_obj(obj)
        data['user'] = obj.user.username
        return data
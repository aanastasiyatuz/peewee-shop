from abstract.serializers import BaseSerializer
from .models import MyUser as User

class UserSerializer(BaseSerializer):
    class Meta:
        fields = ('id','username')
        model = User
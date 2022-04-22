from rest_framework import serializers
from .models import Store,User,Shift


class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'


class ShiftSerializer(serializers.ModelSerializer):

    worker1 = serializers.StringRelatedField()
    worker2 = serializers.StringRelatedField()
    worker3 = serializers.StringRelatedField()
    worker4 = serializers.StringRelatedField()
    store = serializers.StringRelatedField()

    class Meta:
        model = Shift
        fields = '__all__'



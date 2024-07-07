from rest_framework import serializers

class MemberSerializer(serializers.Serializer):
    firstname = serializers.CharField()
    lastname = serializers.CharField()
    phone = serializers.IntegerField()
    email = serializers.EmailField()



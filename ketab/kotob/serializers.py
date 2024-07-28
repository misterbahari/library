from rest_framework import serializers

from ketab.kotob.models import Question, Answer


class MemberSerializer(serializers.Serializer):
    firstname = serializers.CharField()
    lastname = serializers.CharField()
    phone = serializers.IntegerField()
    email = serializers.EmailField()


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'

class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = '__all__'



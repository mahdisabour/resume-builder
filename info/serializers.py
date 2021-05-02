from rest_framework import serializers
from .models import Resume, PersonalInfo, EmploymentHistory

class personalInfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = PersonalInfo
        fields = '__all__'


class EmploymentHistoySerializer(serializers.ModelSerializer):

    class Meta:
        model = EmploymentHistory
        fields = '__all__'


class resumeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Resume
        fields = ['id', 'resumeTitle', 'owner'] 


class resumeDetailSerializer(serializers.ModelSerializer):

    personalInfo = personalInfoSerializer(source= 'PI_modified', read_only=False)
    # employmentHistory = EmploymentHistoySerializer(source= 'EH_modified', read_only=False, many= True)

    class Meta:
        model = Resume
        fields = ['id', 'resumeTitle', 'personalInfo']


    # def update(self, validated_data):
    #     employmentHistoryData = validated_data.pop('employmenHistory')
    #     resume = Resume.objects.get(id= validated_data["id"])
    #     for data in employmentHistoryData:
    #         EmploymentHistory.objects.create(resumeId=resume, **data)
    #     return resume

        



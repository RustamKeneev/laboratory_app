from rest_framework import serializers
from doctors.models import Doctors, DoctorType, MedicalStaffPositions


class DoctorDetailSerializer(serializers.ModelSerializer):
    doctorType = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Doctors
        fields = '__all__'


class DoctorListSerializer(serializers.ModelSerializer):
    doctorType = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Doctors
        fields = (
            'id', 'doctorFullName', 'doctorType', 'doctorWorkLocation',
            'doctorStatus', 'doctorImage',
        )


class DoctorTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = DoctorType
        fields = ('id', 'name', 'image', 'field_1', 'field_2')


class MedicalStaffPositionsSerializer(serializers.ModelSerializer):
    # medical_staff_count = serializers.SerializerMethodField()
    class Meta:
        model = MedicalStaffPositions
        fields = ('id', 'name', 'medical_staff_count', 'image')
    #
    # def get_medical_staff_count(self,obj):
    #     return len(Doctors.objects.filter(medical_staff_positions=obj))

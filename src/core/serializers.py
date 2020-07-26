from rest_framework import serializers
from src.core.models import TestModel
from src.core.models import Contact
from src.core.models import Scholarship
from src.core.models import PhoneNumber
from src.core.models import Event


class TestModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = TestModel
        fields =  ('id', 'first_name', 'last_name')

class PhoneNumberSerializer(serializers.ModelSerializer):

    class Meta:
        model = PhoneNumber
        fields = ('id','contact', 'phone', 'platforms')


class ContactSerializer(serializers.ModelSerializer):
    phone_contact_set = PhoneNumberSerializer(many=True)
    class Meta:
        model = Contact
        fields = ('id','name','website','email','fax', 'description', 'department', 'contact_type', 'phone_contact_set')


class ScholarshipSerializer(serializers.ModelSerializer):

    class Meta:
        model = Scholarship
        fields = ('id','name','description','details')

class EventSerializer(serializers.ModelSerializer):

    class Meta:
        model = Event
        fields = ('id', 'name', 'start_date_time', 'end_date_time', 'location')

        
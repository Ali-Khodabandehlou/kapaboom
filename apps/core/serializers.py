from django.contrib.auth.models import User

from rest_framework import serializers

from .models import CentralGovernment, Time, Manager, Group, Actions


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'pk', 'username',
        ]


class CentralGovernmentSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()

    class Meta:
        model = CentralGovernment
        fields = [
            'pk', 'name', 'user',
        ]

    @staticmethod
    def get_user(obj):
        return UserSerializer(obj).data


class ManagerSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()

    class Meta:
        model = Manager
        fields = [
            'pk', 'name', 'user',
        ]

    @staticmethod
    def get_user(obj):
        return UserSerializer(obj).data


class GroupSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()

    class Meta:
        model = Group
        fields = [
            'pk', 'name', 'user',
        ]

    @staticmethod
    def get_user(obj):
        return UserSerializer(obj.user).data


class GroupDetailSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    location = serializers.SerializerMethodField()

    class Meta:
        model = Group
        fields = [
            'pk', 'name', 'user',
            'action_point', 'location', 'money',
            'wealth', 'power', 'reputation',
            'primary_water', 'primary_food', 'primary_fuel',
            'secondary_iron', 'secondary_copper', 'secondary_gold', 'secondary_diamond'
        ]

    @staticmethod
    def get_user(obj):
        return UserSerializer(obj.user).data

    @staticmethod
    def get_location(obj):
        return obj.location.location_title


class TimeSerializer(serializers.ModelSerializer):
    timer = serializers.SerializerMethodField()

    class Meta:
        model = Time
        fields = [
            'pk', 'year', 'timer', 'start_time'
        ]

    @staticmethod
    def get_timer(obj, *args, **kwargs):
        return obj.timer.seconds


class ActionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actions
        fields = ['pk', 'title', 'title_fa', 'consumption_water', 'consumption_food', 'consumption_fuel',
                  'consumption_gold', 'consumption_ap', ]

import datetime

from django.contrib.auth import authenticate
from django.contrib.auth.models import User

from rest_framework import status, views
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response

from .actions import ACTIONS
from .models import KASB_LIMIT, CentralGovernment, Time, Manager, Group, Actions, MapLocation
from .serializers import CentralGovernmentSerializer, UserSerializer, TimeSerializer, ManagerSerializer, \
    GroupSerializer, ActionSerializer, GroupDetailSerializer


class LoginView(views.APIView):
    @staticmethod
    def post(request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(username=username, password=password)
        if user is not None:
            user_data = UserSerializer(user).data
            if user.is_superuser:
                response = {'user': user_data, 'type': 'admin'}
            elif user.is_staff:
                response = {'user': user_data, 'type': 'gov'}
            else:
                group = user.group.first()
                response = {'user': user_data, 'type': 'client', 'group_pk': group.pk}
            return Response(response, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'username does not exist'}, status=status.HTTP_400_BAD_REQUEST)


class CentralGovernmentSignUpView(views.APIView):
    permission_classes = (IsAdminUser,)

    @staticmethod
    def post(request, *args, **kwargs):
        govname = request.data.get('govname')
        username = request.data.get('username')
        password = request.data.get('password')

        gov = CentralGovernment.objects.filter(name=govname)
        if gov.count():
            return Response({'error': 'government exists'}, status=status.HTTP_400_BAD_REQUEST)
        user = User.objects.filter(username=username)
        if user.count():
            return Response({'error': 'username exists'}, status=status.HTTP_400_BAD_REQUEST)

        user = User.objects.create_user(
            username=username,
            password=password
        )
        user.is_superuser = True
        user.is_staff = True
        user.save()
        gov = CentralGovernment.objects.create(
            name=govname,
            user=user
        )
        return Response(CentralGovernmentSerializer(gov).data, status=status.HTTP_201_CREATED)


class ManagerSignUpView(views.APIView):
    permission_classes = (IsAdminUser,)

    @staticmethod
    def post(request, *args, **kwargs):
        managername = request.data.get('managername')
        username = request.data.get('username')
        password = request.data.get('password')

        manager = Manager.objects.filter(name=managername)
        if manager.count():
            return Response({'error': 'manager exists'}, status=status.HTTP_400_BAD_REQUEST)
        user = User.objects.filter(username=username)
        if user.count():
            return Response({'error': 'username exists'}, status=status.HTTP_400_BAD_REQUEST)

        user = User.objects.create_user(
            username=username,
            password=password
        )
        user.is_staff = True
        user.save()
        manager = Manager.objects.create(
            name=managername,
            user=user
        )
        return Response(ManagerSerializer(manager).data, status=status.HTTP_201_CREATED)


class GroupSignUpView(views.APIView):
    permission_classes = (IsAdminUser,)

    @staticmethod
    def post(request, *args, **kwargs):
        groupname = request.data.get('groupname')
        username = request.data.get('username')
        password = request.data.get('password')

        group = Group.objects.filter(name=groupname)
        if group.count():
            return Response({'error': 'group exists'}, status=status.HTTP_400_BAD_REQUEST)
        user = User.objects.filter(username=username)
        if user.count():
            return Response({'error': 'username exists'}, status=status.HTTP_400_BAD_REQUEST)

        user = User.objects.create_user(
            username=username,
            password=password
        )
        group = Group.objects.create(
            name=groupname,
            user=user
        )
        return Response(GroupSerializer(group).data, status=status.HTTP_201_CREATED)


class GroupListView(views.APIView):
    permission_classes = (IsAuthenticated,)

    @staticmethod
    def get(request, *args, **kwargs):
        groups = Group.objects.all()
        return Response(GroupSerializer(groups, many=True).data, status=status.HTTP_200_OK)


class TimerView(views.APIView):
    @staticmethod
    def get(request, *args, **kwargs):
        active_time = Time.objects.filter(active=True).last()
        time = Time.objects.last()
        if active_time is not None:
            response = {
                'year': time.year,
                'timer': TimeSerializer(active_time).data
            }
            return Response(response, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'there are no active timers'}, status=status.HTTP_400_BAD_REQUEST)


class TimerAddView(views.APIView):
    @staticmethod
    def post(request, *args, **kwargs):
        if request.user.is_staff:
            year = request.data.get('year')
            timer = request.data.get('timer')

            duration = datetime.timedelta(seconds=int(timer))
            Time.objects.create(year=year, timer=duration)
            return Response({'message': 'timer created successfuly'}, status=status.HTTP_200_OK)

        return Response({'error': 'user has no access'}, status=status.HTTP_401_UNAUTHORIZED)


class ActionListView(views.APIView):
    @staticmethod
    def get(request, *args, **kwargs):
        response = {}
        for action in Actions.objects.all():
            response[action.title] = ActionSerializer(action).data
        return Response(response, status=status.HTTP_200_OK)


class ActionView(views.APIView):
    permission_classes = [IsAuthenticated, ]

    @staticmethod
    def post(request, *args, **kwargs):
        group_pk = int(request.data.get('group_pk'))
        action_pk = int(request.data.get('action_pk'))
        group = Group.objects.get(pk=group_pk)
        action = Actions.objects.get(pk=action_pk)

        if group is None:
            return Response({'error': 'Group does not exist'}, status=status.HTTP_404_NOT_FOUND)
        if group.action_point < action.consumption_ap:
            return Response({'error': 'Group action points are low'}, status=status.HTTP_400_BAD_REQUEST)

        response = ACTIONS[action.title](group, request)
        if 'error' in response.keys():
            return Response({'error': response['error']}, status=status.HTTP_400_BAD_REQUEST)

        group.action_point -= action.consumption_ap
        group.save()
        return Response(GroupSerializer(group).data, status=status.HTTP_200_OK)


class GroupDetailView(views.APIView):
    permission_classes = [IsAuthenticated, ]

    @staticmethod
    def post(request, *args, **kwargs):
        group = request.data.get('gpk')
        return Response(GroupDetailSerializer(Group.objects.get(pk=int(group))).data, status=status.HTTP_200_OK)
        # return Response(GroupDetailSerializer(group).data, status=status.HTTP_200_OK)


# class LocationListView(views.APIView):
#     @staticmethod
#     def get(request, *args, **kwargs):
#         locations = MapLocation.objects.all()
#         response = {}
#         for loc in locations:
#             response[loc.location_title] = loc.pk
#         return Response(response, status=status.HTTP_200_OK)

from django.contrib.auth.models import User
from django.db import models

KASB_LIMIT = 12

# TECH_COST = {
#     '1': {'iron': 5, 'copper': 0, 'gold': 0, 'diamond': 0, 'wealth': 2},
#     '2': {'iron': 10, 'copper': 4, 'gold': 0, 'diamond': 0, 'wealth': 4},
#     '3': {'iron': 15, 'copper': 8, 'gold': 3, 'diamond': 0, 'wealth': 6},
#     '4': {'iron': 20, 'copper': 16, 'gold': 6, 'diamond': 2, 'wealth': 8},
# }
#
# WEATHER_EFFECTS = {
#     '1': {'color': 'black', 'food': -20, 'water': -20},
#     '2': {'color': 'yellow', 'food': 0, 'water': -20},
#     '3': {'color': 'red', 'food': -20, 'water': 0},
#     '4': {'color': 'white', 'food': 0, 'water': 0},
#     '5': {'color': 'green', 'food': 20, 'water': 0},
#     '6': {'color': 'blue', 'food': 0, 'water': 20},
#     '7': {'color': 'darkgreen', 'food': 20, 'water': 20},
# }
#
# RESOURCE_PRICE = {
#     'water': 0.1,
#     'food': 0.1,
#     'fuel': 0.1,
#     'iron': 1,
#     'copper': 2,
#     'gold': 5,
#     'diamond': 13,
# }
#
#
# class Tech(models.Model):
#     title = models.CharField(max_length=50)
#     level = models.IntegerField(default=0)
#     image = models.ImageField(upload_to='media', null=True, blank=True)
#
#     active = models.BooleanField(default=False)


class Resource(models.Model):
    name = models.CharField(max_length=50)
    name_fa = models.CharField(max_length=50, blank=True)
    image = models.ImageField(upload_to='media/resources/', null=True, blank=True)

    def __str__(self):
        return self.name


class MapLocation(models.Model):
    location_title = models.CharField(max_length=5)
    resources = models.ManyToManyField(Resource)
    weather = models.IntegerField(default=0)

    neighbor_Locations = models.ManyToManyField("self")

    def __str__(self):
        return self.location_title


# class Map(models.Model):
#     image = models.ImageField(upload_to='media')
#     locations = models.ManyToManyField(MapLocation)


class CentralGovernment(models.Model):
    name = models.CharField(max_length=150)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Manager(models.Model):
    name = models.CharField(max_length=150)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Group(models.Model):
    name = models.CharField(max_length=150)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='group')

    action_point = models.IntegerField(default=0)
#     tech_level = models.ForeignKey(Tech, on_delete=models.SET_NULL, null=True)
    location = models.ForeignKey(MapLocation, on_delete=models.SET_NULL, null=True)

    money = models.IntegerField(default=0)

    wealth = models.IntegerField(default=0)
    power = models.IntegerField(default=0)
    reputation = models.IntegerField(default=0)

    primary_water = models.IntegerField(default=0)
    primary_food = models.IntegerField(default=0)
    primary_fuel = models.IntegerField(default=0)

    secondary_iron = models.IntegerField(default=0)
    secondary_copper = models.IntegerField(default=0)
    secondary_gold = models.IntegerField(default=0)
    secondary_diamond = models.IntegerField(default=0)

    def __str__(self):
        return self.name

    def calculate_wealth(self):
        self.wealth = self.primary_water + self.primary_food + self.primary_fuel + self.secondary_iron + \
                      self.secondary_copper + self.secondary_gold + self.secondary_diamond
        self.save()

    def calculate_power(self):
        self.power = (0.1 * (self.primary_water + self.primary_food + self.primary_fuel)) + (self.secondary_iron) + \
                      (2 * self.secondary_copper) + (5 * self.secondary_gold) + (13 * self.secondary_diamond)
        self.save()


class Time(models.Model):
    year = models.IntegerField(default=0)
    timer = models.DurationField(default=0)

    start_time = models.TimeField(auto_now=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.year} - {self.timer}'


class Actions(models.Model):
    title = models.CharField(max_length=50)
    title_fa = models.CharField(max_length=50, null=True)
    # tech_level = models.ForeignKey(Tech, on_delete=models.SET_NULL, null=True)

    consumption_water = models.IntegerField(default=0)
    consumption_food = models.IntegerField(default=0)
    consumption_fuel = models.IntegerField(default=0)
    consumption_gold = models.IntegerField(default=0)
    consumption_ap = models.IntegerField(default=0)

    def __str__(self):
        return self.title
#
#
# class Disaster(models.Model):
#     title = models.CharField(max_length=50)
#     dynamic = models.BooleanField(default=False)
#
#     effect_location = models.ManyToManyField(MapLocation)
#     effect_group = models.ManyToManyField(Group)
#
#     effect_water = models.IntegerField(default=0)
#     effect_food = models.IntegerField(default=0)
#     active = models.BooleanField(default=False)
#
#
# class History(models.Model):
#     action = models.ForeignKey(Actions, on_delete=models.SET_NULL, null=True)
#     group = models.ForeignKey(Group, on_delete=models.SET_NULL, null=True)

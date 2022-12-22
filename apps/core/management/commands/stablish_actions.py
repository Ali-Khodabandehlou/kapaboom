from django.core.management.base import BaseCommand

from ...models import Actions

ACTIONS = {
    'kasb': {
        'title': 'کسب منابع اولیه',
        'water': 0,
        'food': 0,
        'fuel': 0,
        'gold': 0,
        'ap': 1
    },
    'safar': {
        'title': 'سفر',
        'water': 6,
        'food': 2,
        'fuel': 2,
        'gold': 0,
        'ap': 1
    },
    'estekhraj': {
        'title': 'استخراج',
        'water': 2,
        'food': 4,
        'fuel': 4,
        'gold': 0,
        'ap': 1
    },
    # 'ekteshaf': {
    #     'title': 'اکتشاف',
    #     'water': 2,
    #     'food': 4,
    #     'fuel': 4,
    #     'gold': 0,
    #     'ap': 1
    # },
    # 'mobadele': {
    #     'title': 'مبادله',
    #     'water': 0,
    #     'food': 0,
    #     'fuel': 0,
    #     'gold': 0,
    #     'ap': 1
    # },
    # 'kar': {
    #     'title': 'کسب و کار',
    #     'water': 0,
    #     'food': 0,
    #     'fuel': 0,
    #     'gold': 20,
    #     'ap': 3
    # },
    # 'jang': {
    #     'title': 'جنگ',
    #     'water': 0,
    #     'food': 0,
    #     'fuel': 0,
    #     'gold': 30,
    #     'ap': 3
    # },
    # 'tech': {
    #     'title': 'فناوری',
    #     'water': 0,
    #     'food': 0,
    #     'fuel': 0,
    #     'gold': 0,
    #     'ap': 0
    # },
}


class Command(BaseCommand):
    def handle(self, *args, **options):
        for action in ACTIONS.keys():
            Actions.objects.get_or_create(
                title=action,
                title_fa=ACTIONS[action]['title'],
                consumption_water=ACTIONS[action]['water'],
                consumption_food=ACTIONS[action]['food'],
                consumption_fuel=ACTIONS[action]['fuel'],
                consumption_gold=ACTIONS[action]['gold'],
                consumption_ap=ACTIONS[action]['ap'],
            )

from .models import KASB_LIMIT, Group, Actions, CentralGovernment, MapLocation


def kasb(group: Group, request, undo=False):
    effect = -1 if undo else 1

    water = int(request.data.get('water'))
    food = int(request.data.get('food'))
    fuel = int(request.data.get('fuel'))

    if (water + food + fuel) > KASB_LIMIT:
        return {
            'error': 'resources exceed limit'
        }

    group.primary_water += effect * water
    group.primary_food += effect * food
    group.primary_fuel += effect * fuel

    group.save()

    return {'success': 'OK'}


def safar(group: Group, request, undo=False):
    destination = request.data.get('destination')
    destination = MapLocation.objects.get(location_title__iexact=destination)
    origin = group.location

    if destination == origin:
        return {'error': 'you are on the same map tile'}
    if destination not in origin.neighbor_Locations.all():
        return {'error': 'cannot travel this way'}

    group.location = destination
    group.save()
    return {'success': 'OK'}


# def ekteshaf(group: Group, undo=False):
#     effect = -1 if undo else 1
#     # todo
#     group.save()
#
#
# def estekhraj(group: Group, undo=False):
#     effect = -1 if undo else 1
#     # todo
#     group.save()
#
#
# def mobadele(group: Group, dest_group: Group, resource_name, resource_count, undo=False):
#     effect = -1 if undo else 1
#     # todo
#     group.save()
#     dest_group.save()
#
#
# def mobadele_gover(group: Group, governer: CentralGovernment, resource_name, resource_count, undo=False):
#     effect = -1 if undo else 1
#     # todo
#     group.save()
#     governer.save()
#
#
# def kar(group: Group, action: Actions, undo=False):
#     effect = -1 if undo else 1
#     # todo
#     group.save()
#
#
# def war(group: Group, dest_group: Group, undo=False):
#     effect = -1 if undo else 1
#     # todo
#     group.save()
#     dest_group.save()
#
#
# def tech_advance(group: Group, undo=False):
#     effect = -1 if undo else 1
#     # todo
#     group.save()


ACTIONS = {
    'kasb': kasb,
    'safar': safar,
}

from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.generic import View
from main.models import Member, Location


class HomeView(View):

    def get(self, request, *args, **kwargs):
        context = {}

        # how many people are in the home hole?
        members_at_home = Member.objects.filter(location__name='J212812')
        context['num_members_at_home'] = len(members_at_home)

        # how many scanning ships are in the home hole?
        ships_at_home = {}

        for member in members_at_home:
            # if this kind of ship has already been seen at home
            if member.ship.id in ships_at_home.keys():
                ships_at_home[member.ship.id]['count'] += 1
            # else if this is the first time we've seen this kind of ship
            else:
                ships_at_home[member.ship.id] = {}
                ships_at_home[member.ship.id]['count'] = 1
                ships_at_home[member.ship.id]['name'] = member.ship.name

        context['ships_at_home'] = ships_at_home

        import pprint
        pprint.pprint(context)

        return render_to_response(
                'home.html', context,
                context_instance=RequestContext(request))


class ControlledView(View):

    def get(self, request, *args, **kwargs):
        context = {}

        # regex that matches a wormhole name
        wh_regex = r'J[0-9]{6}'

        # find the wormholes that contain corp members
        wormholes = Location.objects.filter(name__regex=wh_regex).order_by('name')
        context['wormholes'] = wormholes

        # find the corp members inside wormholes
        scouts = Member.objects.filter(location__name__regex=wh_regex).order_by('name')
        context['scouts'] = scouts

        # for scout in scouts:
        #     print "%s - %s" % (scout.location.name, scout.name)

        return render_to_response(
                'controlled.html', context,
                context_instance=RequestContext(request))
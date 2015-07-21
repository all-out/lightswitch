#!/usr/bin/env python
import datetime
import evelink.corp
import os
import sys

sys.path.append("..")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "lightswitch.settings")

from main.models import Location, Member, Ship


# Comment to "refresh" information
# Uncomment to "replace" information
# Location.objects.all().delete()
# Member.objects.all().delete()
# Ship.objects.all().delete()

# ---------------------

# api = evelink.api.API(api_key=(ALL_OUT_KEYID, ALL_OUT_VCODE))
# corp = evelink.corp.Corp(api)
# member_response = corp.members()

# # prints a dictionary
# print member_response.result

# ---------------------

# result = {91707907: {'logon_ts': 1429071190, 'name': 'Murdock Okada', 'logoff_ts': 1429071242, 'title': '', 'can_grant': 0, 'join_ts': 1427140680, 'base': {'id': 0, 'name': ''}, 'ship_type': {'id': None, 'name': 'Unknown Type'}, 'roles': 0, 'id': 91707907, 'location': {'id': 60007921, 'name': 'Madomi V - Moon 6 - Ministry of War Information Center'}}, 95356549: {'logon_ts': 1427393993, 'name': 'Reinhard Lennenkamp', 'logoff_ts': 1427394130, 'title': '', 'can_grant': 0, 'join_ts': 1424793480, 'base': {'id': 0, 'name': ''}, 'ship_type': {'id': 606, 'name': 'Velator'}, 'roles': 0, 'id': 95356549, 'location': {'id': 60014689, 'name': 'Duripant VII - Moon 6 - Federal Navy Academy'}}, 93613959: {'logon_ts': 1437266242, 'name': 'John Freechman', 'logoff_ts': 1437267449, 'title': '', 'can_grant': 180143985094819840, 'join_ts': 1417250040, 'base': {'id': 0, 'name': ''}, 'ship_type': {'id': None, 'name': 'Unknown Type'}, 'roles': 1044835113549955200, 'id': 93613959, 'location': {'id': 60008494, 'name': 'Amarr VIII (Oris) - Emperor Family Academy'}}, 92633608: {'logon_ts': 1434524254, 'name': 'Yon Talie-Kuo', 'logoff_ts': 1434524884, 'title': '', 'can_grant': 0, 'join_ts': 1433822400, 'base': {'id': 0, 'name': ''}, 'ship_type': {'id': None, 'name': 'Unknown Type'}, 'roles': 324259173170675712, 'id': 92633608, 'location': {'id': 60008494, 'name': 'Amarr VIII (Oris) - Emperor Family Academy'}}, 93614089: {'logon_ts': 1433464222, 'name': 'Kathrine Smith', 'logoff_ts': 1433467763, 'title': '', 'can_grant': 144115188075855872, 'join_ts': 1416667920, 'base': {'id': 0, 'name': ''}, 'ship_type': {'id': 11188, 'name': 'Anathema'}, 'roles': 1044835113549955200, 'id': 93614089, 'location': {'id': 31001180, 'name': 'J212812'}}, 94354214: {'logon_ts': 1435688005, 'name': 'Brorik Aerus', 'logoff_ts': 1435688033, 'title': '', 'can_grant': 0, 'join_ts': 1416406920, 'base': {'id': 0, 'name': ''}, 'ship_type': {'id': 655, 'name': 'Epithal'}, 'roles': 0, 'id': 94354214, 'location': {'id': 31002054, 'name': 'J165953'}}, 95283288: {'logon_ts': 1436772264, 'name': 'Atlas Atilius', 'logoff_ts': 1436772708, 'title': '', 'can_grant': 0, 'join_ts': 1432787220, 'base': {'id': 0, 'name': ''}, 'ship_type': {'id': 32880, 'name': 'Venture'}, 'roles': 324259173170675712, 'id': 95283288, 'location': {'id': 30000162, 'name': 'Maila'}}, 92204180: {'logon_ts': 1435422099, 'name': 'Akeiko Shegemi', 'logoff_ts': 1435422243, 'title': '', 'can_grant': 0, 'join_ts': 1433968260, 'base': {'id': 0, 'name': ''}, 'ship_type': {'id': None, 'name': 'Unknown Type'}, 'roles': 0, 'id': 92204180, 'location': {'id': 60008494, 'name': 'Amarr VIII (Oris) - Emperor Family Academy'}}, 2108901550: {'logon_ts': 1432529290, 'name': 'Yin Askavelles', 'logoff_ts': 1432535781, 'title': '', 'can_grant': 0, 'join_ts': 1431290820, 'base': {'id': 0, 'name': ''}, 'ship_type': {'id': None, 'name': 'Unknown Type'}, 'roles': 324259173170675712, 'id': 2108901550, 'location': {'id': 60011725, 'name': 'Adacyne IV - Moon 14 - Federal Administration Bureau Offices'}}, 95104662: {'logon_ts': 1435449550, 'name': 'Dylann Noree', 'logoff_ts': 1435462748, 'title': '', 'can_grant': 180143985094819840, 'join_ts': 1425885420, 'base': {'id': 0, 'name': ''}, 'ship_type': {'id': None, 'name': 'Unknown Type'}, 'roles': 1044835113549955200, 'id': 95104662, 'location': {'id': 60008953, 'name': 'Toshabia VII - Moon 5 - Theology Council Tribunal'}}, 93245083: {'logon_ts': 1437375864, 'name': 'Jardok Akari', 'logoff_ts': 1437376208, 'title': '', 'can_grant': 0, 'join_ts': 1434313740, 'base': {'id': 0, 'name': ''}, 'ship_type': {'id': 34562, 'name': 'Svipul'}, 'roles': 900719925474099200, 'id': 93245083, 'location': {'id': 31001180, 'name': 'J212812'}}, 1733400990: {'logon_ts': 1434487330, 'name': 'Gildaer Strij', 'logoff_ts': 1434487434, 'title': '', 'can_grant': 0, 'join_ts': 1429943640, 'base': {'id': 0, 'name': ''}, 'ship_type': {'id': 638, 'name': 'Raven'}, 'roles': 324259173170675712, 'id': 1733400990, 'location': {'id': 30002738, 'name': 'Inoue'}}, 93004960: {'logon_ts': 1437424800, 'name': 'magic creeper', 'logoff_ts': 1437425640, 'title': '', 'can_grant': 0, 'join_ts': 1437269280, 'base': {'id': 0, 'name': ''}, 'ship_type': {'id': 32880, 'name': 'Venture'}, 'roles': 324259173170675712, 'id': 93004960, 'location': {'id': 31001180, 'name': 'J212812'}}, 92091425: {'logon_ts': 1425436779, 'name': 'Tehol Aerus', 'logoff_ts': 1425437727, 'title': '', 'can_grant': 0, 'join_ts': 1415827020, 'base': {'id': 0, 'name': ''}, 'ship_type': {'id': 670, 'name': 'Capsule'}, 'roles': 0, 'id': 92091425, 'location': {'id': 60008494, 'name': 'Amarr VIII (Oris) - Emperor Family Academy'}}, 95047458: {'logon_ts': 1436376243, 'name': 'Big Pi', 'logoff_ts': 1436376428, 'title': 'Benevolent Dictator For Life', 'can_grant': 0, 'join_ts': 1414970580, 'base': {'id': 0, 'name': ''}, 'ship_type': {'id': 34317, 'name': 'Confessor'}, 'roles': 9223372036854775807, 'id': 95047458, 'location': {'id': 31001180, 'name': 'J212812'}}, 92625827: {'logon_ts': 1437437317, 'name': 'Jeremy Fisher Mileghere', 'logoff_ts': 1437440264, 'title': '', 'can_grant': 0, 'join_ts': 1434761820, 'base': {'id': 0, 'name': ''}, 'ship_type': {'id': 33468, 'name': 'Astero'}, 'roles': 900719925474099200, 'id': 92625827, 'location': {'id': 31001180, 'name': 'J212812'}}, 93450406: {'logon_ts': 1427568918, 'name': 'Cristine Reynolds', 'logoff_ts': 1427574022, 'title': '', 'can_grant': 0, 'join_ts': 1424818140, 'base': {'id': 0, 'name': ''}, 'ship_type': {'id': None, 'name': 'Unknown Type'}, 'roles': 36028797018963968, 'id': 93450406, 'location': {'id': 60003760, 'name': 'Jita IV - Moon 4 - Caldari Navy Assembly Plant'}}, 90074922: {'logon_ts': 1430935481, 'name': 'Magnus Legatus', 'logoff_ts': 1430935676, 'title': '', 'can_grant': 0, 'join_ts': 1427647740, 'base': {'id': 0, 'name': ''}, 'ship_type': {'id': None, 'name': 'Unknown Type'}, 'roles': 900719925474099200, 'id': 90074922, 'location': {'id': 60003760, 'name': 'Jita IV - Moon 4 - Caldari Navy Assembly Plant'}}, 95711147: {'logon_ts': 1437305777, 'name': 'Teorec', 'logoff_ts': 1437311144, 'title': '', 'can_grant': 0, 'join_ts': 1437242880, 'base': {'id': 0, 'name': ''}, 'ship_type': {'id': None, 'name': 'Unknown Type'}, 'roles': 324259173170675712, 'id': 95711147, 'location': {'id': 60003760, 'name': 'Jita IV - Moon 4 - Caldari Navy Assembly Plant'}}, 95035692: {'logon_ts': 1433354004, 'name': 'Quia Adoudel', 'logoff_ts': 1433359975, 'title': '', 'can_grant': 0, 'join_ts': 1432337520, 'base': {'id': 0, 'name': ''}, 'ship_type': {'id': None, 'name': 'Unknown Type'}, 'roles': 0, 'id': 95035692, 'location': {'id': 60011866, 'name': 'Dodixie IX - Moon 20 - Federation Navy Assembly Plant'}}, 90757037: {'logon_ts': 1434633091, 'name': 'Jason Saissore', 'logoff_ts': 1434633943, 'title': '', 'can_grant': 0, 'join_ts': 1433628780, 'base': {'id': 0, 'name': ''}, 'ship_type': {'id': 2006, 'name': 'Omen'}, 'roles': 324259173170675712, 'id': 90757037, 'location': {'id': 31001180, 'name': 'J212812'}}, 94823726: {'logon_ts': 1437407342, 'name': 'Death Cupcake', 'logoff_ts': 1437409313, 'title': '', 'can_grant': 0, 'join_ts': 1437293460, 'base': {'id': 0, 'name': ''}, 'ship_type': {'id': None, 'name': 'Unknown Type'}, 'roles': 0, 'id': 94823726, 'location': {'id': 60004516, 'name': 'Hek IV - Krusual Tribe Bureau'}}, 95679343: {'logon_ts': 1436461023, 'name': 'Klaus Severasse', 'logoff_ts': 1436461324, 'title': '', 'can_grant': 0, 'join_ts': 1435936440, 'base': {'id': 0, 'name': ''}, 'ship_type': {'id': None, 'name': 'Unknown Type'}, 'roles': 324259173170675712, 'id': 95679343, 'location': {'id': 60012412, 'name': 'Agil VI - Moon 2 - CONCORD Logistic Support'}}, 95253041: {'logon_ts': 1430543602, 'name': 'Foskl', 'logoff_ts': 1430543852, 'title': '', 'can_grant': 0, 'join_ts': 1427361060, 'base': {'id': 0, 'name': ''}, 'ship_type': {'id': None, 'name': 'Unknown Type'}, 'roles': 0, 'id': 95253041, 'location': {'id': 60003760, 'name': 'Jita IV - Moon 4 - Caldari Navy Assembly Plant'}}, 95298995: {'logon_ts': 1428433462, 'name': 'PudgePudge', 'logoff_ts': 1428434774, 'title': '', 'can_grant': 0, 'join_ts': 1426826160, 'base': {'id': 0, 'name': ''}, 'ship_type': {'id': None, 'name': 'Unknown Type'}, 'roles': 0, 'id': 95298995, 'location': {'id': 60008494, 'name': 'Amarr VIII (Oris) - Emperor Family Academy'}}, 95184822: {'logon_ts': 1437312003, 'name': 'Euripides Chancel', 'logoff_ts': 1437314319, 'title': '', 'can_grant': 0, 'join_ts': 1435733160, 'base': {'id': 0, 'name': ''}, 'ship_type': {'id': 672, 'name': 'Caldari Shuttle'}, 'roles': 324259173170675712, 'id': 95184822, 'location': {'id': 31001180, 'name': 'J212812'}}, 94735625: {'logon_ts': 1425003134, 'name': 'Kazuho Yoshii', 'logoff_ts': 1425003238, 'title': '', 'can_grant': 0, 'join_ts': 1416425700, 'base': {'id': 0, 'name': ''}, 'ship_type': {'id': None, 'name': 'Unknown Type'}, 'roles': 36028797018963968, 'id': 94735625, 'location': {'id': 60002554, 'name': 'Mabnen V - Moon 5 - Expert Distribution Warehouse'}}, 94993976: {'logon_ts': 1436495288, 'name': 'Georges Ondioline', 'logoff_ts': 1436498609, 'title': '', 'can_grant': 0, 'join_ts': 1436413920, 'base': {'id': 0, 'name': ''}, 'ship_type': {'id': None, 'name': 'Unknown Type'}, 'roles': 324259173170675712, 'id': 94993976, 'location': {'id': 60011872, 'name': 'Aunia I - Moon 11 - Federation Navy Assembly Plant'}}, 93731914: {'logon_ts': 1437282742, 'name': 'Mussah Yacoub', 'logoff_ts': 1437290135, 'title': '', 'can_grant': 0, 'join_ts': 1417801140, 'base': {'id': 0, 'name': ''}, 'ship_type': {'id': 11182, 'name': 'Cheetah'}, 'roles': 9223372036854775807, 'id': 93731914, 'location': {'id': 31001180, 'name': 'J212812'}}, 95077036: {'logon_ts': 1437343737, 'name': 'Shira Voldaren', 'logoff_ts': 1437360830, 'title': '', 'can_grant': 0, 'join_ts': 1435360140, 'base': {'id': 0, 'name': ''}, 'ship_type': {'id': 16238, 'name': 'Cormorant'}, 'roles': 0, 'id': 95077036, 'location': {'id': 31001180, 'name': 'J212812'}}, 95627716: {'logon_ts': 1435155292, 'name': 'Katgat Enat', 'logoff_ts': 1435155753, 'title': '', 'can_grant': 0, 'join_ts': 1433015220, 'base': {'id': 0, 'name': ''}, 'ship_type': {'id': None, 'name': 'Unknown Type'}, 'roles': 0, 'id': 95627716, 'location': {'id': 60008494, 'name': 'Amarr VIII (Oris) - Emperor Family Academy'}}, 91207114: {'logon_ts': 1437349779, 'name': 'Tablecat', 'logoff_ts': 1437353484, 'title': '', 'can_grant': 0, 'join_ts': 1436235540, 'base': {'id': 0, 'name': ''}, 'ship_type': {'id': 598, 'name': 'Breacher'}, 'roles': 324259173170675712, 'id': 91207114, 'location': {'id': 31001180, 'name': 'J212812'}}, 95585612: {'logon_ts': 1432627457, 'name': 'Dimitri Motsu', 'logoff_ts': 1432628097, 'title': '', 'can_grant': 0, 'join_ts': 1432309800, 'base': {'id': 0, 'name': ''}, 'ship_type': {'id': 670, 'name': 'Capsule'}, 'roles': 0, 'id': 95585612, 'location': {'id': 31001180, 'name': 'J212812'}}, 95594063: {'logon_ts': 1432026955, 'name': 'Ciera Shitsgiggles', 'logoff_ts': 1432028877, 'title': '', 'can_grant': 0, 'join_ts': 1431772560, 'base': {'id': 0, 'name': ''}, 'ship_type': {'id': 649, 'name': 'Tayra'}, 'roles': 0, 'id': 95594063, 'location': {'id': 31001180, 'name': 'J212812'}}, 93813200: {'logon_ts': 1426883851, 'name': 'Flaire Lancer', 'logoff_ts': 1426884643, 'title': '', 'can_grant': 180143985094819840, 'join_ts': 1421721900, 'base': {'id': 0, 'name': ''}, 'ship_type': {'id': 23757, 'name': 'Archon'}, 'roles': 189151184349560960, 'id': 93813200, 'location': {'id': 31002054, 'name': 'J165953'}}, 95164984: {'logon_ts': 1425678496, 'name': 'Cruian Severasse', 'logoff_ts': 1425680218, 'title': '', 'can_grant': 0, 'join_ts': 1419876660, 'base': {'id': 0, 'name': ''}, 'ship_type': {'id': 33468, 'name': 'Astero'}, 'roles': 0, 'id': 95164984, 'location': {'id': 31002054, 'name': 'J165953'}}, 95194275: {'logon_ts': 1427730313, 'name': 'Nagg', 'logoff_ts': 1427731223, 'title': '', 'can_grant': 1130405722673123712, 'join_ts': 1423076940, 'base': {'id': 0, 'name': ''}, 'ship_type': {'id': 33468, 'name': 'Astero'}, 'roles': 1130405722673123712, 'id': 95194275, 'location': {'id': 31002054, 'name': 'J165953'}}, 1489872855: {'logon_ts': 1436930666, 'name': 'Elldgrim', 'logoff_ts': 1436930945, 'title': '', 'can_grant': 0, 'join_ts': 1432658100, 'base': {'id': 0, 'name': ''}, 'ship_type': {'id': None, 'name': 'Unknown Type'}, 'roles': 324259173170675712, 'id': 1489872855, 'location': {'id': 60004588, 'name': 'Rens VI - Moon 8 - Brutor Tribe Treasury'}}, 741355736: {'logon_ts': 1437428590, 'name': 'Amplify', 'logoff_ts': 1437429920, 'title': '', 'can_grant': 180143985094819840, 'join_ts': 1421626200, 'base': {'id': 0, 'name': ''}, 'ship_type': {'id': None, 'name': 'Unknown Type'}, 'roles': 468374361246531968, 'id': 741355736, 'location': {'id': 60006220, 'name': 'Pimebeka VII - Moon 16 - Carthum Conglomerate Factory'}}, 92346969: {'logon_ts': 1437158078, 'name': 'Kyle Aerus', 'logoff_ts': 1437158149, 'title': '', 'can_grant': 0, 'join_ts': 1415620080, 'base': {'id': 0, 'name': ''}, 'ship_type': {'id': None, 'name': 'Unknown Type'}, 'roles': 0, 'id': 92346969, 'location': {'id': 60003760, 'name': 'Jita IV - Moon 4 - Caldari Navy Assembly Plant'}}, 94272603: {'logon_ts': 1428142079, 'name': 'Scrooge Antollare', 'logoff_ts': 1428142353, 'title': '', 'can_grant': 0, 'join_ts': 1416404460, 'base': {'id': 0, 'name': ''}, 'ship_type': {'id': 655, 'name': 'Epithal'}, 'roles': 0, 'id': 94272603, 'location': {'id': 31002054, 'name': 'J165953'}}, 90780895: {'logon_ts': 1421948528, 'name': 'Gaston Canton', 'logoff_ts': 1421959848, 'title': '', 'can_grant': 0, 'join_ts': 1420162140, 'base': {'id': 0, 'name': ''}, 'ship_type': {'id': None, 'name': 'Unknown Type'}, 'roles': 0, 'id': 90780895, 'location': {'id': 60008494, 'name': 'Amarr VIII (Oris) - Emperor Family Academy'}}, 94751456: {'logon_ts': 1437367316, 'name': 'incinerator rex', 'logoff_ts': 1437368896, 'title': '', 'can_grant': 0, 'join_ts': 1415384520, 'base': {'id': 0, 'name': ''}, 'ship_type': {'id': 34317, 'name': 'Confessor'}, 'roles': 900719925474099200, 'id': 94751456, 'location': {'id': 31001180, 'name': 'J212812'}}, 93666146: {'logon_ts': 1429552117, 'name': 'Veknic Maken', 'logoff_ts': 1429552193, 'title': '', 'can_grant': 0, 'join_ts': 1427058060, 'base': {'id': 0, 'name': ''}, 'ship_type': {'id': None, 'name': 'Unknown Type'}, 'roles': 0, 'id': 93666146, 'location': {'id': 60013975, 'name': 'Palas II - Royal Khanid Navy Assembly Plant'}}, 94168742: {'logon_ts': 1433864825, 'name': 'Vidar Ymir', 'logoff_ts': 1433866337, 'title': '', 'can_grant': 0, 'join_ts': 1424991660, 'base': {'id': 0, 'name': ''}, 'ship_type': {'id': None, 'name': 'Unknown Type'}, 'roles': 36028797018963968, 'id': 94168742, 'location': {'id': 60006352, 'name': 'Bahromab IX - Moon 13 - Carthum Conglomerate Factory'}}, 95573203: {'logon_ts': 1437374484, 'name': 'Killigan Vaille', 'logoff_ts': 1437379109, 'title': '', 'can_grant': 0, 'join_ts': 1433871660, 'base': {'id': 0, 'name': ''}, 'ship_type': {'id': 650, 'name': 'Nereus'}, 'roles': 900719925474099200, 'id': 95573203, 'location': {'id': 31001180, 'name': 'J212812'}}, 95619345: {'logon_ts': 1435750312, 'name': 'Forgetting The Past', 'logoff_ts': 1435750339, 'title': '', 'can_grant': 0, 'join_ts': 1432783440, 'base': {'id': 0, 'name': ''}, 'ship_type': {'id': 11192, 'name': 'Buzzard'}, 'roles': 324259173170675712, 'id': 95619345, 'location': {'id': 30004777, 'name': 'ZXB-VC'}}, 95619816: {'logon_ts': 1433376206, 'name': 'Natalka Dormer', 'logoff_ts': 1433376310, 'title': '', 'can_grant': 0, 'join_ts': 1432706160, 'base': {'id': 0, 'name': ''}, 'ship_type': {'id': None, 'name': 'Unknown Type'}, 'roles': 324259173170675712, 'id': 95619816, 'location': {'id': 60015027, 'name': 'Uitra VI - Moon 4 - State War Academy'}}, 95695870: {'logon_ts': 1437422007, 'name': 'Fly By Wire', 'logoff_ts': 1437423470, 'title': '', 'can_grant': 0, 'join_ts': 1437108960, 'base': {'id': 0, 'name': ''}, 'ship_type': {'id': None, 'name': 'Unknown Type'}, 'roles': 324259173170675712, 'id': 95695870, 'location': {'id': 60000067, 'name': 'Ronne I - Moon 1 - CBD Corporation Storage'}}, 95383598: {'logon_ts': 1425844888, 'name': 'David Altacor', 'logoff_ts': 1425898800, 'title': '', 'can_grant': 0, 'join_ts': 1424816880, 'base': {'id': 0, 'name': ''}, 'ship_type': {'id': None, 'name': 'Unknown Type'}, 'roles': 0, 'id': 95383598, 'location': {'id': 60012670, 'name': 'Airaken V - Moon 1 - Sisters of EVE Academy'}}, 1912174704: {'logon_ts': 1426883912, 'name': 'Fayng Lancer', 'logoff_ts': 1426884645, 'title': '', 'can_grant': 180143985094819840, 'join_ts': 1421260920, 'base': {'id': 0, 'name': ''}, 'ship_type': {'id': 670, 'name': 'Capsule'}, 'roles': 189151184349560960, 'id': 1912174704, 'location': {'id': 60008494, 'name': 'Amarr VIII (Oris) - Emperor Family Academy'}}, 95485363: {'logon_ts': 1437442830, 'name': 'Wydwen Zirud', 'logoff_ts': 1437439357, 'title': '', 'can_grant': 0, 'join_ts': 1436477280, 'base': {'id': 0, 'name': ''}, 'ship_type': {'id': 11188, 'name': 'Anathema'}, 'roles': 900719925474099200, 'id': 95485363, 'location': {'id': 31001180, 'name': 'J212812'}}, 94062781: {'logon_ts': 1437419342, 'name': 'Egravan Anstian', 'logoff_ts': 1437431606, 'title': '', 'can_grant': 0, 'join_ts': 1417476720, 'base': {'id': 0, 'name': ''}, 'ship_type': {'id': 12038, 'name': 'Purifier'}, 'roles': 0, 'id': 94062781, 'location': {'id': 31001005, 'name': 'J125833'}}, 95546352: {'logon_ts': 1437152746, 'name': 'Yin Askavelle', 'logoff_ts': 1437153403, 'title': '', 'can_grant': 0, 'join_ts': 1435761840, 'base': {'id': 0, 'name': ''}, 'ship_type': {'id': None, 'name': 'Unknown Type'}, 'roles': 0, 'id': 95546352, 'location': {'id': 60008494, 'name': 'Amarr VIII (Oris) - Emperor Family Academy'}}, 95073522: {'logon_ts': 1437401308, 'name': 'Vilhyin Auffrie', 'logoff_ts': 1437432986, 'title': '', 'can_grant': 0, 'join_ts': 1422900060, 'base': {'id': 0, 'name': ''}, 'ship_type': {'id': 33468, 'name': 'Astero'}, 'roles': 9223372036854775807, 'id': 95073522, 'location': {'id': 31001180, 'name': 'J212812'}}, 94191859: {'logon_ts': 1437437413, 'name': 'Meryl Redmond', 'logoff_ts': 1437438739, 'title': '', 'can_grant': 0, 'join_ts': 1421488860, 'base': {'id': 0, 'name': ''}, 'ship_type': {'id': 12733, 'name': 'Prorator'}, 'roles': 36028797018963968, 'id': 94191859, 'location': {'id': 31001180, 'name': 'J212812'}}, 95104244: {'logon_ts': 1417695379, 'name': 'Rachel Aerus', 'logoff_ts': 1417695680, 'title': '', 'can_grant': 0, 'join_ts': 1416939300, 'base': {'id': 0, 'name': ''}, 'ship_type': {'id': None, 'name': 'Unknown Type'}, 'roles': 0, 'id': 95104244, 'location': {'id': 60003760, 'name': 'Jita IV - Moon 4 - Caldari Navy Assembly Plant'}}, 95245429: {'logon_ts': 1437195671, 'name': 'Aqustin Agustus', 'logoff_ts': 1437195688, 'title': '', 'can_grant': 0, 'join_ts': 1436331600, 'base': {'id': 0, 'name': ''}, 'ship_type': {'id': None, 'name': 'Unknown Type'}, 'roles': 324259173170675712, 'id': 95245429, 'location': {'id': 60000847, 'name': 'Oto VIII - Moon 4 - Minedrill Mining Outpost'}}, 95571190: {'logon_ts': 1431053482, 'name': 'Daveman2173 Aideron', 'logoff_ts': 1431053676, 'title': '', 'can_grant': 0, 'join_ts': 1430956440, 'base': {'id': 0, 'name': ''}, 'ship_type': {'id': None, 'name': 'Unknown Type'}, 'roles': 0, 'id': 95571190, 'location': {'id': 60015036, 'name': 'Clellinon VI - Moon 11 - Center for Advanced Studies School'}}, 94351096: {'logon_ts': 1428682209, 'name': 'Katy Aerus', 'logoff_ts': 1428693625, 'title': '', 'can_grant': 0, 'join_ts': 1423770600, 'base': {'id': 0, 'name': ''}, 'ship_type': {'id': None, 'name': 'Unknown Type'}, 'roles': 36028797018963968, 'id': 94351096, 'location': {'id': 60002698, 'name': 'Tasabeshi IV - Moon 10 - CBD Sell Division Retail Center'}}, 95108500: {'logon_ts': 1437438376, 'name': 'Nootkin', 'logoff_ts': 1437442620, 'title': '', 'can_grant': 0, 'join_ts': 1422160260, 'base': {'id': 0, 'name': ''}, 'ship_type': {'id': 605, 'name': 'Heron'}, 'roles': 9223372036854775807, 'id': 95108500, 'location': {'id': 31001180, 'name': 'J212812'}}, 94961962: {'logon_ts': 1420489534, 'name': 'Mole Skine', 'logoff_ts': 1420490746, 'title': '', 'can_grant': 0, 'join_ts': 1418739360, 'base': {'id': 0, 'name': ''}, 'ship_type': {'id': None, 'name': 'Unknown Type'}, 'roles': 0, 'id': 94961962, 'location': {'id': 60014134, 'name': 'Ardar IV - Moon 2 - Thukker Mix Factory'}}, 95255323: {'logon_ts': 1436931669, 'name': 'Reyni Allas-Rui', 'logoff_ts': 1436939122, 'title': '', 'can_grant': 180143985094819840, 'join_ts': 1420753620, 'base': {'id': 0, 'name': ''}, 'ship_type': {'id': None, 'name': 'Unknown Type'}, 'roles': 1044835113549955200, 'id': 95255323, 'location': {'id': 60003760, 'name': 'Jita IV - Moon 4 - Caldari Navy Assembly Plant'}}, 95648121: {'logon_ts': 1435346187, 'name': 'Allie Tzash', 'logoff_ts': 1435346856, 'title': '', 'can_grant': 0, 'join_ts': 1433872980, 'base': {'id': 0, 'name': ''}, 'ship_type': {'id': 589, 'name': 'Executioner'}, 'roles': 900719925474099200, 'id': 95648121, 'location': {'id': 31001180, 'name': 'J212812'}}}


for id in result.keys():

    # First check to see if the member is in a ship.  If they are, check to
    # see if the ship id already exists.  Add an entry if it doesn't;
    # update the existing one if it does.  Save the updated ship object.
    ship_id = result[id]['ship_type']['id']
    if ship_id is not None:
        new_ship, created = Ship.objects.get_or_create(id=ship_id)
        new_ship.name = result[id]['ship_type']['name']
        new_ship.save()

    # Check to see if this location id already exists.  Add an entry if it
    # doesn't; update the existing one if it does.  Save the updated location
    # object.
    new_location, created = Location.objects.get_or_create(id=result[id]['location']['id'])
    new_location.name = result[id]['location']['name']
    new_location.save()

    # Check to see if this user id already exists.  Add an entry if it doesn't,
    # update the existing one if it does.
    new_member, created = Member.objects.get_or_create(id=id)
    new_member.name = result[id]['name']

    # Convert the logoff timestamp to a datetime.datetime object for storage
    logoff_ts = result[id]['logoff_ts']
    logoff_datetime = datetime.datetime.fromtimestamp(logoff_ts)
    new_member.logoff_ts = logoff_datetime

    # Convert the join timestamp to a datetime.datetime object for storage
    join_ts = result[id]['join_ts']
    join_datetime = datetime.datetime.fromtimestamp(join_ts)
    new_member.join_ts = join_datetime

    # if the member is in a ship, make the member-ship relationship
    if ship_id is not None:
        new_member.ship = new_ship

    # make the member-location relationship
    new_member.location = new_location

    # Save the updated member object
    new_member.save()

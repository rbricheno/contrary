"""Example where we pretend we are configuring a RADIUS client."""
import pprint
from contrary import Contrary

config_instance = Contrary(["config_example.yaml", "config_secrets_example.yaml"])
config_dict = config_instance.data
pp = pprint.PrettyPrinter(depth=12)
pp.pprint(config_dict)

# Prints:
#
# OrderedDict([('radius_nas_identifier', 'Catweazle'),
#              ('radius_client_bind_ip', 'a.b.c.d'),
#              ('radius_schedule', 'round-robin'),
#              ('radius_server_timeout', 3),
#              ('radius_append_realm', True),
#              ('radius_default_realm', 'wireless.inst.example.com'),
#              ('radius_servers',
#               OrderedDict([('radius0.inst.example.com',
#                             OrderedDict([('secret', b'real_secret_0'),
#                                          ('auth_port', 1812)])),
#                            ('radius1.inst.example.com',
#                             OrderedDict([('secret', b'real_secret_1'),
#                                          ('auth_port', 1812)]))]))])
#
# Note: the secrets have been replaced in the config with the values from config_secrets_example.yaml
# while the rest of the config is maintaned from config_example.yaml

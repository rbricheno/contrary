"""Example where we pretend we are configuring a RADIUS client."""
import pprint
from contrary import Contrary

config_instance = Contrary(["config_example.yaml", "config_secrets_example.yaml"])
config_dict = config_instance.data
pp = pprint.PrettyPrinter(depth=12)
pp.pprint(config_dict)

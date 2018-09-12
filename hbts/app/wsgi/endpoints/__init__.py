from werkzeug.routing import Map

from .health import HealthEndpoint
from .version import VersionEndpoint
from .timestamp import TimestampEndpoint


urlpatterns = Map([
    HealthEndpoint.as_rule(),
    VersionEndpoint.as_rule(),
    TimestampEndpoint.as_rule(),
])


# !!! SG MANAGED FILE -- DO NOT EDIT -- VERSION:  !!!

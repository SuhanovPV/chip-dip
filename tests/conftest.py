import config
import pytest


def pytest_addoption(parser):
    parser.addoption(
        '--location',
        default='local',
        help='--location: local, remote'
    )
    parser.addoption(
        '--service',
        default='web',
        help='--service: web, app'
    )

@pytest.fixture(scope='class', autouse=True)
def browser_settings(request):
    service = request.config.getoption('--service')
    location = request.config.getoption('--location')
    if service == 'web':
        config.set_browser(location)
    elif service == 'app':
        config.set_mobile(location)
    else:
        raise KeyError
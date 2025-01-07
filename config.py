from appium.options.android import UiAutomator2Options
from appium import webdriver as appium_webdriver
from selenium import webdriver as selenium_webdriver
from pydantic_settings import BaseSettings
from selene import browser
from selenium.webdriver.chrome.options import Options
from chip_dip.utils import path_helper


class WebConfig(BaseSettings):
    browser_name: str = ''
    browser_version: str = ''
    selenoid_login: str = ''
    selenoid_pass: str = ''
    selenoid_url: str = ''
    width: str = ''
    height: str = ''
    base_url: str = ''

class AppConfig(BaseSettings):
    deviceName: str = ''
    app: str = ''
    appWaitActivity: str = ''
    appActivity: str = ''
    remote_url: str = ''
    timeout: float = 8.0
    platformVersion: str = ''
    sessionName: str = ''
    projectName: str = ''
    name: str = ''
    accessKey: str = ''


def load_app_config_from_env(location):
    if location in ['local', 'remote']:
        config = AppConfig(_env_file=path_helper.abs_path_from_project(f'.env_app_{location}'))
    else:
        raise KeyError
    return config


def load_web_config_from_env(location):
    if location in ['local', 'remote']:
        config = WebConfig(_env_file=path_helper.abs_path_from_project(f'.env_web_{location}'))
    else:
        raise KeyError
    return config


def set_app_options(config, location):
    options = UiAutomator2Options().load_capabilities(
        {
            'deviceName': config.deviceName,
            'appWaitActivity': config.appWaitActivity,
            'appActivity': config.appActivity,
        }
    )
    options.set_capability('app',
                           config.app if location == 'remote' else path_helper.abs_path_from_project(config.app))

    if location == 'remote':
        options.set_capability('platformVersion', config.platformVersion)
        options.set_capability('bstack:options', {
            "sessionName": config.sessionName,
            "projectName": config.projectName,
            "userName": config.name,
            "accessKey": config.accessKey
        })
    return options


def set_mobile(location):
    config = load_app_config_from_env(location)
    options = set_app_options(config, location)
    browser.config.timeout = config.timeout
    browser.config.driver = appium_webdriver.Remote(config.remote_url, options=options)


def set_local_browser(config):
    if config.browser_name == 'firefox':
        options = selenium_webdriver.FirefoxOptions()
    elif config.browser_name == 'chrome':
        options = selenium_webdriver.ChromeOptions()
    else:
        raise KeyError('Not supported browser')
    browser.config.driver_options = options


def set_remote_browser(config):
    options = Options()
    selenoid_capabilities = {
        "browserName": config.browser_name,
        "browserVersion": config.browser_version,
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True
        }
    }
    options.capabilities.update(selenoid_capabilities)
    driver = selenium_webdriver.Remote(
        command_executor=f"https://{config.selenoid_login}:{config.selenoid_pass}@{config.selenoid_url}/wd/hub",
        options=options)
    browser.config.driver = driver


def set_browser(location):
    config = load_web_config_from_env(location)
    if location == 'local':
        set_local_browser(config)
    else:
        set_remote_browser(config)
    browser.config.window_width = config.width
    browser.config.window_height = config.height
    browser.config.base_url = config.base_url

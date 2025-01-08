import allure
import requests
import config


def add_html(browser):
    allure.attach(
        body=browser.driver.page_source,
        name='page',
        attachment_type=allure.attachment_type.HTML,
        extension='.html'
    )


def add_xml(browser):
    allure.attach(
        body=browser.driver.page_source,
        name='screen_xml_dump',
        attachment_type=allure.attachment_type.XML
    )


def page_source(browser, service):
    if service == 'web':
        add_html(browser)
    elif service == 'app':
        add_xml(browser)


def screenshot(browser):
    allure.attach(
        body=browser.driver.get_screenshot_as_png(),
        name='screenshot',
        attachment_type=allure.attachment_type.PNG,
        extension='.png'
    )


def bs_video_url(session_id):
    conf = config.load_app_config_from_env('remote')
    bstack_session = requests.get(
        f'https://api.browserstack.com/app-automate/sessions/{session_id}.json',
        auth=(conf.name, conf.accessKey)
    ).json()
    return bstack_session['automation_session']['video_url']


def selenoid_video_url(session_id):
    conf = config.load_web_config_from_env('remote')
    return f'https://{conf.selenoid_url}/video/{session_id}.mp4'


def video(service, session_id):
    if service == 'app':
        video_url = bs_video_url(session_id)
    else:
        video_url = selenoid_video_url(session_id)
    allure.attach(
        '<html><body><video width="100%" height="100%" controls autoplay>'
        f'<source src={video_url} type="video/mp4">'
        '</video></body></html>',
        name='video_rec',
        attachment_type=allure.attachment_type.HTML
    )


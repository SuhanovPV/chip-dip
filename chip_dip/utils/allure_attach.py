import allure

def page_source(browser):
    allure.attach(
        body=browser.driver.page_source,
        name='page',
        attachment_type=allure.attachment_type.HTML,
        extension='.html'
    )

def screenshot(browser):
    allure.attach(
        body=browser.driver.get_screenshot_as_png(),
        name='screenshot',
        attachment_type=allure.attachment_type.PNG,
        extension='.png'
    )

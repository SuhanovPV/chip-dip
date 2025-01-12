# Проект Web/Mobile тестирования сайта и приложения магазина ChipDip
> <a target="_blank" href="https://www.chipdip.ru/">ChipDip</a>
<img width="1200" src="source/chipdip_web.png">


## Используемый стек технологий и инструментов

|                        Python                         |                        Pytest                         |                          Selen                          |                        Selenoid                         |                        Git                         |                        Jenkins                         |                        Allure                         |                        Allure TestOps                         |                        Appium                         |                        BrowserStack                         |                        Telegram                         |
|:-----------------------------------------------------:|:-----------------------------------------------------:|:-------------------------------------------------------:|:-------------------------------------------------------:|:--------------------------------------------------:|:------------------------------------------------------:|:-----------------------------------------------------:|:-------------------------------------------------------------:|:-----------------------------------------------------:|:-----------------------------------------------------------:|:-------------------------------------------------------:|
| <img width="55" height="55" src="source/python.svg"/> | <img width="55" height="55" src="source/pytest.svg"/> | <img width="55" height="55" src="source/selenium.svg"/> | <img width="55" height="55" src="source/selenoid.svg"/> | <img width="55" height="55" src="source/git.svg"/> | <img width="55" height="55" src="source/jenkins.svg"/> | <img width="55" height="55" src="source/allure.svg"/> | <img width="40" height="40" src="source/allure-testops.png"/> | <img width="40" height="40" src="source/appium.png"/> | <img width="40" height="40" src="source/browserstack.png"/> | <img width="40" height="40" src="source/telegram.svg"/> |

## Tесты
### UI
<ul style="list-style-type: '\2705 &#160'">
    <li>Login to site with correct credentials</li>
    <li>Login to site with wrong credentials</li>
    <li>Search existing product in cart</li>
    <li>Search non-existent product in cart</li>
    <li>Add product to cart</li>
    <li>Remove all product from cart</li>
    <li>Ordering product</li>
</ul>

### App
<ul style="list-style-type: '\2705 &#160'">
    <li>Add product to cart</li>
    <li>Remove all product from cart</li>
    <li>Change number of section on main page</li>
</ul>
https://jenkins.autotests.cloud/job/c16-chip-dip/

## <img width="3%" title="Jenkins" src="source/jenkins.svg"> Запуск проекта в Jenkins
#### Для запуска автотестов в Jenkins
1. __Открыть проект <a href="https://jenkins.autotests.cloud/job/c16-chip-dip/">в Jenkins</a>__
2. __Выбрать пункт `Build with Parameters`__
3. __Выбрать тип запускаемых тестов в списке `SERVICE`(`web` или `api`)__
4. __Если выбран `web`, можно задать параметры браузера:__
   * __Браузер: `Chrome` или `Firefox`__
   * __А так же выбрать версию браузера__
5. __Нажать кнопку `Build`__
6. __Результат запуска сборки можно посмотреть в отчете Allure__

> <a target="_blank" href="https://www.chipdip.ru/">Jenkis</a>
<img width="1200" src="source/Jenkins_build.png">

## <img width="3%" title="Allure report"  src="source/allure.svg"> Отчет в Allure report
>__Просмотр результатов выполнения тестов в Allure report__
<img width="1200" src="source/allure_report_overview.png">

>__Отчет позволяет получить общую информацию о прохождении тестов__
<img width="1200" src="source/allure_report_suites_all.png">

>__Отчет позволяет получить информацию о прохождении каждого теста__
<img width="1200" src="source/allure_report_suites_one_test.png">

__Каждый тесто содержит детальную информацию по всем шагам тестов, включая скриншоты, дам страницы и видео прохождения теста.__
>__Пример видео для теста вебсайта: (Оформление заказа)__
<img width="1200" src="source/web_video.gif">

>__Пример видео для теста приложения: (Добавление товара в корзину)__
> 
<img width="350" src="source/app_video.gif">
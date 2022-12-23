# Changelog

## [Unreleased]

## [0.0.44] - 2022-12-23

### Добавлено

- Typed connect views [@fringer2423](https://github.com/fringer2423)
- Typed QRCode views
- Typed rate info views
- Typed rate views
- Typed review settings views
- Typed review views

### Изменено

- 

## [0.0.43] - 2022-12-22

### Добавлено

- Added django-silk [@fringer2423](https://github.com/fringer2423)
- Configured silk
- Typed answer views
- Typed branch views
- Typed company views
- Refactor random generate service

### Изменено

- Upgrade certifi to version 2022.12.07 or later to fix [@fringer2423](https://github.com/fringer2423)
- Rename type (type_answer) in answer service

## [0.0.42] - 2022-12-13

### Изменено

- Edited model rate_info [@fringer2423](https://github.com/fringer2423)

## [0.0.41] - 2022-12-02

### Изменено

- added counter in login page [@AlexTrubkina](https://github.com/AlexTrubkina)
- fixed email verification
- changed assets
- fixed login code verification
- исправлены стейты

## [0.0.40] - 2022-12-01

### Изменено

- assets changed [@AlexTrubkina](https://github.com/AlexTrubkina)

## [0.0.40] - 2022-11-30

### Изменено

- Refactor frontend [@fringer2423](https://github.com/fringer2423)
- Удалены лишние ссылки из навигационной панель при авторизации и регистрации [@AlexTrubkina](https://github.com/AlexTrubkina)
- Fix verification email after registration
- Fix userInfo after authorization
- Fix login button
- Fix logout

## [0.0.39] - 2022-11-29

### Изменено

- fixed Authorization [@AlexTrubkina](https://github.com/AlexTrubkina)
- fixed redirect
- fixed profile button on main page
- routes fixed
- Refactor frontend [@fringer2423](https://github.com/fringer2423)

## [0.0.38] - 2022-11-28

### Добавлено

- userLoginVerify reducer [@AlexTrubkina](https://github.com/AlexTrubkina)

### Изменено

- input change color mail validation [@AlexTrubkina](https://github.com/AlexTrubkina)
- bug fixed
- авторизация с помощью кода
- Refactor frontend [@fringer2423](https://github.com/fringer2423)

## [0.0.37] - 2022-11-25

### Добавлено

- PrivateRoute [@AlexTrubkina](https://github.com/AlexTrubkina)

### Изменено

- dashboard navbar [@AlexTrubkina](https://github.com/AlexTrubkina)
- message after registration
- исправлено поведение при верификации пользователя

## [0.0.36] - 2022-11-24

### Добавлено

- VerificationScreen.js, verificationScreen.css [@AlexTrubkina](https://github.com/AlexTrubkina)

### Изменено

- email verification [@AlexTrubkina](https://github.com/AlexTrubkina)

## [0.0.35] - 2022-11-23

### Добавлено

-

### Изменено

-

## [0.0.34] - 2022-11-22

### Добавлено

- QuerySet type on all api services [@fringer2423](https://github.com/fringer2423)
- Typed answer views
- registerValidator to validate password and email [@AlexTrubkina](https://github.com/AlexTrubkina)

### Изменено

- Refactor all services [@fringer2423](https://github.com/fringer2423)
- Login page and registration page [@AlexTrubkina](https://github.com/AlexTrubkina)

## [0.0.33] - 2022-11-21

### Добавлено

- Coefficient calculating for RateInfo model [@fringer2423](https://github.com/fringer2423)
- Docker ignore config
- Typed company service
- Typed answer service
- Typed branch service
- Typed connect service
- Typed QRCode service
- Typed rate info service
- Typed rate service
- Typed review service
- Typed review settings service
- Typed telebot service
- Typed user service

### Изменено

- Refactor frontend [@fringer2423](https://github.com/fringer2423)
- Frontend import paths
- RateInfo model

## [0.0.32] - 2022-11-18

### Добавлено

- Docstrings for new func in user service [@fringer2423](https://github.com/fringer2423)
- Purity Ui Dashboard [@AlexTrubkina](https://github.com/AlexTrubkina)

### Изменено

- User service [@fringer2423](https://github.com/fringer2423)
- log-in button [@AlexTrubkina](https://github.com/AlexTrubkina)
- blueBall.css

## [0.0.31] - 2022-11-17

### Добавлено

- Login confirmation (sending a confirmation code to the user's email) [@fringer2423](https://github.com/fringer2423)
- New user service (generate_new_verify_code_for_user_service)
- New view controller (verify_code_user_view)
- New view controller (send_verify_code_user_view)
- New user service (verify_user_by_code_service)
- added functions countWeekDefaultPrice, countYearDefaultPrice [@AlexTrubkina](https://github.com/AlexTrubkina)
- added blueBall.css

### Изменено

- MyTokenObtainPairView (Added new func for post request) [@fringer2423](https://github.com/fringer2423)
- Centered titles of accordion [@AlexTrubkina](https://github.com/AlexTrubkina)
- changed year in Footer
- fixed whyBlocks
- fixed prices
- fixed login and registration buttons
- changed countPrices


## [0.0.30] - 2022-11-16

### Добавлено

- Subject and body register email message [@fringer2423](https://github.com/fringer2423)

### Изменено

- Bump pillow from 9.2.0 to 9.3.0 [@fringer2423](https://github.com/fringer2423)
- Bump loader-utils from 3.2.0 to 3.2.1 in /frontend
- Refactor frontend

## [0.0.29] - 2022-11-15

### Добавлено

- Email push config [@fringer2423](https://github.com/fringer2423)
- Email push task
- Email push Queue
- Random generator service
- Def save for User model
- New endpoint (verify user)
- New service for user
- Slug and verify code generations
- Docstring for new defs
- Added folder helper [@AlexTrubkina](https://github.com/AlexTrubkina)
- Added function countPrices (for counting range prices in Prices.js)

### Изменено

- Docker-compose config [@fringer2423](https://github.com/fringer2423)
- User model (Added slug field)
- Changed Prices.js (added range for prices) [@AlexTrubkina](https://github.com/AlexTrubkina)
- Changed buttons.css (fixed disabled buttons)
- Changed prices.css (added styles for prices range)
- Changed pictures for better quality

## [0.0.28] - 2022-11-14

### Изменено

- Telegram logging level [@fringer2423](https://github.com/fringer2423)
- Refactor frontend
- User model (new field is_verified)
- User serializer
- Rename frontend/src/validator > validators (так же зависимости)

## [0.0.27] - 2022-11-11

### Добавлено

- React-bootstrap Carousel [@AlexTrubkina](https://github.com/AlexTrubkina)
- email validation
- Docstrings [@fringer2423](https://github.com/fringer2423)

### Изменено

- footer.css, prices.css [@AlexTrubkina](https://github.com/AlexTrubkina)
- Prices.js (added onClick events)
- Minor bugfix [@fringer2423](https://github.com/fringer2423)

### Удалено

- Carousel.js, carousel.css [@AlexTrubkina](https://github.com/AlexTrubkina)

## [0.0.26] - 2022-11-10

### Добавлено

- Hash links in Footer [@AlexTrubkina](https://github.com/AlexTrubkina)
- Added footer.css
- Review list paginator [@fringer2423](https://github.com/fringer2423)
- Branch list paginator

### Изменено

- Header and Footer [@AlexTrubkina](https://github.com/AlexTrubkina)
- Changed CSS: whyBlocks.css, purpleBlock.css, refProg.CSS
- Brands.js: changed pictures
- Swagger conf (added params page for paginator) [@fringer2423](https://github.com/fringer2423)
- Refactor backend

## [0.0.25] - 2022-11-09

### Добавлено

- Celery logger [@fringer2423](https://github.com/fringer2423)
- Queue periodic for celery tasks / workers
- Queue telegram_push for celery tasks / workers
- Celery fast task service
- Periodic tasks logging
- Telegram bot integration
- New command (start_telegram_bot)
- New container telegram bot (Docker)

### Изменено

- Frontend refactor [@fringer2423](https://github.com/fringer2423)
- Logger config
- Celery config
- Docker config

## [0.0.24] - 2022-11-08

### Добавлено

- Yandex tasks [@fringer2423](https://github.com/fringer2423)
- Zoon tasks
- 2GIS tasks
- New app Telebot
- New model Telebot settings
- Log to telegram
- Telegram admin handler
- Telegram send message task
- Компонент Carousel [@AlexTrubkina](https://github.com/AlexTrubkina)

### Изменено

- Edited all loggers msg [@fringer2423](https://github.com/fringer2423)
- Task views
- Изменены маркеры [@AlexTrubkina](https://github.com/AlexTrubkina)
- Компоненты Brands, PurpleCircle, HomeScreen, Header
- CSS purpleBlock, purpleCircle, main, header

## [0.0.23] - 2022-11-07

### Добавлено

- Logger [@fringer2423](https://github.com/fringer2423)
- Логирование Answer endpoints
- Logger custom formatter
- Логирование Branch endpoints
- Логирование Company endpoints
- Логирование Connect endpoints
- Логирование QRCodes endpoints
- Логирование rate info endpoints
- Логирование rate endpoints
- Логирование review settings endpoints
- Логирование review endpoints
- Логирование task endpoints
- Логирование telebot endpoints
- Логирование user endpoints

## [0.0.22] - 2022-11-03

### Добавлено

- New endpoint (branch create) [@fringer2423](https://github.com/fringer2423)
- Added docstrings for new service
- New endpoint (branch update)
- Task serializer
- Task endpoints
- Create branchs commands for tests
- Добавлена анимация [@AlexTrubkina](https://github.com/AlexTrubkina)

### Изменено

- Edited Branch model fields requirements [@fringer2423](https://github.com/fringer2423)
- Edited all views (replace 200 -> 201 status)
- BranchSerializer fix
- Google tasks
- Изменены CSS [@AlexTrubkina](https://github.com/AlexTrubkina)

## [0.0.21] - 2022-11-03

### Добавлено

- Celery beat [@fringer2423](https://github.com/fringer2423)
- Periodic tasks
- New branch service
- New user service
- Schedule beat tasks
- Добавлен whyBlocks.css [@AlexTrubkina](https://github.com/AlexTrubkina)
- Fonts

### Изменено

- Docker-compose config (celery) [@fringer2423](https://github.com/fringer2423)
- Google tasks
- Added new field to Branch model (is_detected)
- First download of branch information task
- Uploading branch reviews task
- Изменены названия файлов CSS [@AlexTrubkina](https://github.com/AlexTrubkina)
- Изменены стили и Компоненты

## [0.0.20] - 2022-11-02

### Изменено

- Google tasks [@fringer2423](https://github.com/fringer2423)
- Added new point in connect service

## [0.0.19] - 2022-11-01

### Добавлено

- Добавлены hash links [@AlexTrubkina](https://github.com/AlexTrubkina)
- Добавлен css для Header
- Added app Tasks [@fringer2423](https://github.com/fringer2423)
- Added new services (yandex_tasks, google_tasks, 2gis_tasks, zoon_tasks)
- Added new api-service

### Изменено

- Edited model review [@fringer2423](https://github.com/fringer2423)
- Изменены css и компоненты ListOfRec, Prices, Header, Footer [@AlexTrubkina](https://github.com/AlexTrubkina)

## [0.0.18] - 2022-10-31

### Добавлено

- User constants [@fringer2423](https://github.com/fringer2423)
- Store provider
- Proxy config
- User actions
- User reducers

### Изменено

- Refactor frontend [@fringer2423](https://github.com/fringer2423)
- Node version in docker config
- Edited details endpoints 4** status

## [0.0.17] - 2022-10-28

### Добавлено

- Анимация [@AlexTrubkina](https://github.com/AlexTrubkina)

### Изменено

- RabbitMQ Linux fix [@fringer2423](https://github.com/fringer2423)
- Celery config
- Flower config
- Updated celery / flower
- Fix Flower OAuth authentication bypass
- Fix OS Command Injection in celery
- Footer, Header, Форма заполнения контактных данных и css [@AlexTrubkina](https://github.com/AlexTrubkina)

## [0.0.16] - 2022-10-27

### Добавлено

- Отдельный сервис с Celery [@fringer2423](https://github.com/fringer2423)
- Отдельный сервис с Flower
- Возможность балансировки задач между всеми workers
- Компоненты LogIn и Registration [@AlexTrubkina](https://github.com/AlexTrubkina)

### Изменено

- HomeScreen.js и css [@AlexTrubkina](https://github.com/AlexTrubkina)

## [0.0.15] - 2022-10-26

### Добавлено

- Проект упакован в Docker [@fringer2423](https://github.com/fringer2423)
- Отдельный сервис с PostgreSQL
- Отдельный сервис с Backend
- Отдельный сервис с Frontend
- Отдельный сервис с RabbitMQ
- Отдельный сервис с Redis
- Отдельный сервис с Redis commander

### Изменено

- Локальные dev конфигурации [@fringer2423](https://github.com/fringer2423)
- fix minimatch ReDoS vulnerability

## [0.0.14] - 2022-10-25

### Добавлено

- Компонент Accordion.js и css accordion.css [@AlexTrubkina](https://github.com/AlexTrubkina)
- Добавлены картинки

### Изменено

- Обновление проекта и подключение python 3.11 [@fringer2423](https://github.com/fringer2423)
- Refactor code
- HomeScreen.js [@AlexTrubkina](https://github.com/AlexTrubkina)
- Refprogram.js и css

## [0.0.13] - 2022-10-21

### Добавлено

- Docs for new service [@fringer2423](https://github.com/fringer2423)

### Изменено

- Context fix urls [@fringer2423](https://github.com/fringer2423)
- Refactor code

## [0.0.12] - 2022-10-20

### Добавлено

- Компонент ListOfRec и css [@AlexTrubkina](https://github.com/AlexTrubkina)
- CSS для кнопок
- Модели Rate и RateInfo [@fringer2423](https://github.com/fringer2423)
- Обработка 401 статуса в авторизации
- Rate info serializer
- Rate info endpoints
- Rate info service
- Rate serializer
- Rate endpoints
- Rate service

### Изменено

- Connect fix [@fringer2423](https://github.com/fringer2423)
- User model
- Добавлено поле rate в UserSerializer
- Компонент Prices.js (добавлена карусель) [@AlexTrubkina](https://github.com/AlexTrubkina)
- Компоненты Prices и HomeScreen
- CSS buttons, main, purple circle

## [0.0.11] - 2022-10-19

### Добавлено

- Обработка 406 статуса [@fringer2423](https://github.com/fringer2423)

### Изменено

- Connect relationship fix [@fringer2423](https://github.com/fringer2423)
- Review serializer (add answer field)
- Компоненты и css [@AlexTrubkina](https://github.com/AlexTrubkina)

## [0.0.10] - 2022-10-18

### Добавлено

- Endpoint для отдачи всех qrcode [@fringer2423](https://github.com/fringer2423)
- Pytest
- Тест ping
- Entrypoint script для Docker
- Именование всех urls
- Обработка 405 статуса
- Обработка 422 статуса
- Компоненты и css [@AlexTrubkina](https://github.com/AlexTrubkina)

### Изменено

- Fix media URLs [@fringer2423](https://github.com/fringer2423)
- Serializer fix
- Refactor code
- QRCode generator вынесен в отдельную функцию
- Refactor docs

## [0.0.9] - 2022-10-17

### Добавлено [@fringer2423](https://github.com/fringer2423)

- Serializer для QRCode
- Endpoints для QRCode
- Генератор QRCode
- Бизнес логика связанная с QRCode

## [0.0.8] - 2022-10-14

### Добавлено

- Документация по всем слоям бизнес логики [@fringer2423](https://github.com/fringer2423)
- Добавлен endpoint для возврата всех отзывов компании
- Расширен слой бизнес логики для review
- Добавлен FormUser [@AlexTrubkina](https://github.com/alextrubkina)
- Добавлен Prices

### Изменено

- Fix Response detail performance [@fringer2423](https://github.com/fringer2423)
- Fix Review serializer field (answered_at)
- Refactor code
- Изменен HomeScreen [@AlexTrubkina](https://github.com/alextrubkina)

## [0.0.7] - 2022-10-13

### Добавлено

- Endpoints для Review [@fringer2423](https://github.com/fringer2423)
- Serializer для Review
- Serializer для Review settings
- Endpoints для Review settings
- Serializer для Answer
- Endpoints для Answer
- main.css [@AlexTrubkina](https://github.com/alextrubkina)

### Изменено

- Endpoints create и update у connect [@fringer2423](https://github.com/fringer2423)
- Endpoints create и update у branch
- Endpoints create и update у company
- Endpoints create и update у review
- Endpoints create и update у telebot
- Endpoints у user
- Refactor all endpoints
- Refactor Create URLS (endpoints)
- Serializers fix
- Exception info fix
- Serializer answer fix
- Header.js, HomeScreen.js [@AlexTrubkina](https://github.com/alextrubkina)

### Удалено

- Старый фронт[@AlexTrubkina](https://github.com/alextrubkina)

## [0.0.6] - 2022-10-12

### Добавлено

- Добавлены endpoints для telebot [@fringer2423](https://github.com/fringer2423)
- Добавлен Serializer для Telebot
- Добавлен endpoint для чтения информации об одном филиале
- Добавлен Serializer для Connect
- Добавлены endpoints для Connect

### Изменено

- Обновлена документация по новым endpoints [@fringer2423](https://github.com/fringer2423)
- Обновлена документация по слою бизнес логики
- Refactor endpoints
- Доработана документация по API
- Refactor code

### Удалено

## [0.0.5] - 2022-10-11

### Добавлено [@fringer2423](https://github.com/fringer2423).

- Описания для аргументов всех endpoints
- Endpoint для удаления company
- Добавлена модель WorkDay
- Добавлен Serializer WorkDay
- Добавлен Serializer Schedule
- Добавлен Serializer Branch

### Изменено [@fringer2423](https://github.com/fringer2423).

- Переопределение метода post в контроллере авторизации
- Бизнес логика перенесена в отдельный слой
- Refactor всех моделей
- Модель графика работы

## [0.0.4] - 2022-10-10

### Добавлено [@fringer2423](https://github.com/fringer2423).

- Endpoints для модели Company
- Serializer для модели Company
- Endpoint для изменения информации пользователя

### Изменено [@fringer2423](https://github.com/fringer2423).

- В некоторые модели добавлены поля created_at
- TimeZone
- app_name в urls по логическим частям
- Подробно описаны все endpoints в документации
- User endpoints теперь по адресу api/user/

## [0.0.3] - 2022-10-07

### Добавлено [@fringer2423](https://github.com/fringer2423).

- Модель User
- Модель Company
- Модель Schedule
- Модель Branch
- Модель Telebot
- Модель QRCode
- Модель Connect
- Модель Review
- Модель ReviewSettings
- Модель Answer
- Автогенерация документации по проекту (находится в личном кабинете администратора)
- Swagger
- Добавлены doc записи ко всем элементам проекта

## [0.0.2] - 2022-10-06

### Изменено [@fringer2423](https://github.com/fringer2423).

- Urls распределены по логическим частям
- Views распределены по логическим частям
- Refactor code

## [0.0.1] - 2022-10-05

### Добавлено [@fringer2423](https://github.com/fringer2423).

- React
- Django
- Структура проекта
- JWT авторизация / регистрация
- ТЗ
- Инструкция по работе с проектом
- Зависимости по проекту
- Добавлены сигналы при работе с моделью User
- Добавлен end point для получения данных о пользователе

### Изменено

- Базовая модель User
- Базовая авторизация
- Readme

#### Типы изменений (Добавлено, исправлено, изменено)

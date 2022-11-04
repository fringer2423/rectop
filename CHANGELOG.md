# Changelog

## [Unreleased]

## [0.0.22] - 2022-11-03

### Добавлено

- New endpoint (branch create) [@fringer2423](https://github.com/fringer2423)
- Added docstrings for new service
- New endpoint (branch update)
- Task serializer
- Task endpoints
- Create branchs commands for tests

### Изменено

- Edited Branch model fields requirements [@fringer2423](https://github.com/fringer2423)
- Edited all views (replace 200 -> 201 status)
- BranchSerializer fix
- Google tasks

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

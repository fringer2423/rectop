# Changelog

## [Unreleased]

## [0.0.15] - 2022-10-26

### Добавлено

- Проект упакован в Docker [@fringer2423](https://github.com/fringer2423)
- Отдельный сервис с PostgreSQL
- Отдельный сервис с Backend 
- Отдельный сервис с Frontend
- Отдельный сервис с RabbitMQ
- Отдельный сервис с Redis
- Отдельный сервис с Redis commander

## [0.0.14] - 2022-10-25

### Изменено

- Обновление проекта и подключение python 3.11 [@fringer2423](https://github.com/fringer2423)
- Refactor code

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
- CSS buttons, main, purplecircle 


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

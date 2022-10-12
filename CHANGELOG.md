# Changelog

## [Unreleased]

## [0.0.6] - 2022-10-12

### Добавлено

- Добавлены endpoints для telebot [@fringer2423](https://github.com/fringer2423)
- Добавлен Serializer для Telebot

### Изменено

- Обновлена документация по новым endpoints [@fringer2423](https://github.com/fringer2423)
- Обновлена документация по слою бизнес логики
- Refactor endpoints

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
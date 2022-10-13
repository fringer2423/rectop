import React from 'react';
import { Button, Alert } from 'react-bootstrap';


const Tariff = () =>
  <div>
      <h3 className="text-center m-lg-4">
          <b>Выбирайте то, что удобно Вам для управления репутацией</b>
      </h3>
      <Button>На неделю</Button><Button>На месяц</Button><Button>На год</Button>
      <div className="d-flex justify-content-center">
      <Alert className="m-5" variant="light">
        <Alert.Heading>Генератор отзывов</Alert.Heading>
        <p>
        Сбор отзывов
        <hr/>
        Оповещение в телеграме
        <hr/>
        Отчетность в Телеграме
        <hr/>
        Система кэшбека
        <hr/>
        Статистика
        <hr/>
        Обратная связь
        <hr/>
        Поддержка 24/7
        <hr/>
        Формирование qr-кода
        </p>
        <Button>Приобрести тариф</Button>
      </Alert>
      <Alert className="m-5" variant="light">
        <Alert.Heading>Какое-то название</Alert.Heading>
        <p>
        Аналитика по филиалу
        <hr/>
        Постоянная актуализация
        <hr/>
        Система кэшбека
        <hr/>
        Скидки от партнеров
        <hr/>
        Поддержка 24/7
        <hr/>
        Ответы на отзывы в одном месте
        <hr/>
        Обратная связь
        <hr/>
        Подробная статистика
        </p>
        <Button>Приобрести тариф</Button>
      </Alert>
      <Alert className="m-5" variant="light">
        <Alert.Heading>Репутация под ключ</Alert.Heading>
        <p>
        Сбор отзывов
        <hr/>
        Оповещение в телеграме
        <hr/>
        Отчетность в Телеграме
        <hr/>
        Система кэшбека
        <hr/>
        Статистика
        <hr/>
        Обратная связь
        <hr/>
        Поддержка 24/7
        <hr/>
        Формирование qr-кода
        </p>
        <Button>Приобрести тариф</Button>
      </Alert>
      </div>
  </div>


export default Tariff

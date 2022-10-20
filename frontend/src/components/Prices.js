import React from "react";
import "../css/prices.css"

import Carousel from "react-bootstrap/Carousel"

const Prices = (props) => {
  return(
  <>
    <div id="listofprices">
    <div className="tableforprice">
      <h3><b>“Генератор отзывов”</b></h3>
      <h5>1 филиал</h5>
      <h4><b>1200 РУБ./МЕС.</b></h4>
      <div className="blockintable">
        <b>
        Производите сбор отзывов </b> от ваших клиентов при помощи QR-кодов на точках продаж
      </div>
      <div className="textinprice">
        Сбор отзывов
        <hr/>
        Оповещения в Телеграме
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
        <hr/>
      </div>
      <button className="blackbutton">Приобрести тариф</button>
    </div>
    <div className="tableforprice">
      <h3><b>Какое-то название</b></h3>
      <h5>1 филиал</h5>
      <h4><b>1200 РУБ./МЕС.</b></h4>
      <div className="blockintable">
        <b>Работа с отзывами</b> на крупнейших интернет-площадках и сервисах
      </div>
      <div className="textinprice">
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
        <hr/>
      </div>
      <button className="blackbutton">Приобрести тариф</button>
    </div>
    <div className="tableforprice">
      <h3><b>Репутация под ключ</b></h3>
      <h5>1 филиал</h5>
      <h4><b>ОТ 4000 РУБ./МЕС.</b></h4>
      <div className="blockintable">
        <b>Работа с отзывами</b> на крупнейших интернет-площадках и сервисах
      </div>
        <div className="textinprice">
        Генератор и агрегатор отзывов
        <hr/>
        Ответы на отзывы нашими специалистами
        <hr/>
        Проверка выставленных отзывов
        <hr/>
        “Спровоцируем” выставление отзывов
        <hr/>
        Подробная отчетность
        <hr/>
        Аналитика в реальном времени
      </div>
      <button className="blackbutton">Приобрести тариф</button>
    </div>
    </div>


    <div id="sliderforprices">
      <Carousel>
          <Carousel.Item>
            <div className="tableforprice">
              <h3><b>“Генератор отзывов”</b></h3>
              <h5>1 филиал</h5>
              <h4><b>1200 РУБ./МЕС.</b></h4>
              <div className="blockintable">
                <b>
                Производите сбор отзывов </b> от ваших клиентов при помощи QR-кодов на точках продаж
              </div>
              <div className="textinprice">
                Сбор отзывов
                <hr/>
                Оповещения в Телеграме
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
                <hr/>
              </div>
              <button className="blackbutton">Приобрести тариф</button>
            </div>
          </Carousel.Item>
          <Carousel.Item>
            <div className="tableforprice">
              <h3><b>Какое-то название</b></h3>
              <h5>1 филиал</h5>
              <h4><b>1200 РУБ./МЕС.</b></h4>
              <div className="blockintable">
                <b>Работа с отзывами</b> на крупнейших интернет-площадках и сервисах
              </div>
              <div className="textinprice">
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
                <hr/>
              </div>
              <button className="blackbutton">Приобрести тариф</button>
            </div>
          </Carousel.Item>
          <Carousel.Item>
            <div className="tableforprice">
              <h3><b>Репутация под ключ</b></h3>
              <h5>1 филиал</h5>
              <h4><b>ОТ 4000 РУБ./МЕС.</b></h4>
              <div className="blockintable">
                <b>Работа с отзывами</b> на крупнейших интернет-площадках и сервисах
              </div>
                <div className="textinprice">
                Генератор и агрегатор отзывов
                <hr/>
                Ответы на отзывы нашими специалистами
                <hr/>
                Проверка выставленных отзывов
                <hr/>
                “Спровоцируем” выставление отзывов
                <hr/>
                Подробная отчетность
                <hr/>
                Аналитика в реальном времени
              </div>
              <button className="blackbutton">Приобрести тариф</button>
            </div>
          </Carousel.Item>
      </Carousel>
    </div>
  </>
 )
}

export default Prices

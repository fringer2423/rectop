import React from "react";
import "../css/prices.css"

const Prices = () => {
  return(
  <div className="tableforprice">
    <h3><b>“Генератор отзывов”</b></h3>
    <h5>1 филиал</h5>
    <h4><b>1200 РУБ./МЕС.</b></h4>
    <div className="blockintable"><b>
    Производите сбор отзывов </b> от ваших клиентов при помощи QR-кодов на точках продаж</div>
    <p>
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
    </p>
    <button className="blackbutton">Приобрести тариф</button>
  </div>
 )
}

export default Prices

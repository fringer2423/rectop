import React from "react";
import "../css/prices.css"

import {Carousel} from 'react-bootstrap'

const Prices = (props) => {
    return (
        <>

            <div id="list-of-prices">
                <div className="table-for-price">
                    <h3><b>“Генератор отзывов”</b></h3>
                    <h5>1 филиал</h5>
                    <h4><b>1200 РУБ./МЕС.</b></h4>
                    <div className="block-in-table">
                        <b>
                            Производите сбор отзывов </b> от ваших клиентов при помощи QR-кодов на точках продаж
                    </div>
                    <div className="text-in-price">
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
                    <button className="black-button"><b>Приобрести тариф</b></button>
                </div>
                <div className="table-for-price">
                    <h3><b>Какое-то название</b></h3>
                    <h5>1 филиал</h5>
                    <h4><b>1200 РУБ./МЕС.</b></h4>
                    <div className="block-in-table">
                        <b>Работа с отзывами</b> на крупнейших интернет-площадках и сервисах
                    </div>
                    <div className="text-in-price">
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
                    <button className="black-button"><b>Приобрести тариф</b></button>
                </div>
                <div className="table-for-price">
                    <h3><b>Репутация под ключ</b></h3>
                    <h5>1 филиал</h5>
                    <h4><b>ОТ 4000 РУБ./МЕС.</b></h4>
                    <div className="block-in-table">
                        <b>Работа с отзывами</b> на крупнейших интернет-площадках и сервисах
                    </div>
                    <div className="text-in-price">
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
                        <hr/>
                    </div>
                    <button className="black-button"><b>Приобрести тариф</b></button>
                </div>
            </div>


            <div id="slider-for-prices">
                <Carousel>
                    <Carousel.Item className="m-5">
                        <div className="table-for-price">
                            <h3><b>“Генератор отзывов”</b></h3>
                            <h5>1 филиал</h5>
                            <h4><b>1200 РУБ./МЕС.</b></h4>
                            <div className="block-in-table">
                                <b>
                                    Производите сбор отзывов </b> от ваших клиентов при помощи QR-кодов на точках продаж
                            </div>
                            <div className="text-in-price">
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
                            <button className="black-button"><b>Приобрести тариф</b></button>
                        </div>
                    </Carousel.Item>
                    <Carousel.Item className="m-5">
                        <div className="table-for-price">
                            <h3><b>Какое-то название</b></h3>
                            <h5>1 филиал</h5>
                            <h4><b>1200 РУБ./МЕС.</b></h4>
                            <div className="block-in-table">
                                <b>Работа с отзывами</b> на крупнейших интернет-площадках и сервисах
                            </div>
                            <div className="text-in-price">
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
                            <button className="black-button"><b>Приобрести тариф</b></button>
                        </div>
                    </Carousel.Item>
                    <Carousel.Item className="m-5">
                        <div className="table-for-price">
                            <h3><b>Репутация под ключ</b></h3>
                            <h5>1 филиал</h5>
                            <h4><b>ОТ 4000 РУБ./МЕС.</b></h4>
                            <div className="block-in-table">
                                <b>Работа с отзывами</b> на крупнейших интернет-площадках и сервисах
                            </div>
                            <div className="text-in-price">
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
                            <button className="black-button"><b>Приобрести тариф</b></button>
                        </div>
                    </Carousel.Item>
                </Carousel>
            </div>
        </>
    )
}

export default Prices

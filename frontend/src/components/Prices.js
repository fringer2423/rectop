import React, {useState} from "react";
import "../css/prices.css"
import {countPrices} from "../helpers/countPrices.js"

import {Carousel, Form} from 'react-bootstrap';
import {FontAwesomeIcon} from '@fortawesome/react-fontawesome';

import {faArrowRightLong} from '@fortawesome/free-solid-svg-icons';
import {faArrowLeftLong} from '@fortawesome/free-solid-svg-icons';

const Prices = () => {

    const [activeIndex, setActiveIndex] = useState(0);
    const [numFilialFirst, setNumFilialFirst] = useState(1);
    const [numFilialSecond, setNumFilialSecond] = useState(1);
    const [numFilialThird, setNumFilialThird] = useState(1);

    const [priceDurationFirst, setPriceDurationFirst] = useState('300 РУБ./НЕД.');
    const [priceDurationSecond, setPriceDurationSecond] = useState('300 РУБ./НЕД.');
    const [priceDurationThird, setPriceDurationThird] = useState('1000 РУБ./НЕД.');

    const [priceOldFirst, setPriceOldFirst] = useState('');
    const [priceOldSecond, setPriceOldSecond] = useState('');
    const [priceOldThird, setPriceOldThird] = useState('');

    const handleClickFirstPrice = () => {
        setActiveIndex(0);
        setPriceDurationFirst("300 РУБ./НЕД.");
        setPriceDurationSecond("300 РУБ./НЕД.");
        setPriceDurationThird("1000 РУБ./НЕД.");
        setPriceOldFirst("300 РУБ./НЕД.");
        setPriceOldSecond("300 РУБ./НЕД.");
        setPriceOldThird("1000 РУБ./НЕД.");
    }

    const handleClickSecondPrice = () => {
        setActiveIndex(1);
        setPriceDurationFirst("1200 РУБ./МЕС.");
        setPriceDurationSecond("1200 РУБ./МЕС.");
        setPriceDurationThird("4000 РУБ./МЕС.");
        setPriceOldFirst("1200 РУБ./МЕС.");
        setPriceOldSecond("1200 РУБ./МЕС.");
        setPriceOldThird("4000 РУБ./МЕС.");
    }

    const handleClickThirdPrice = () => {
        setActiveIndex(2);
        setPriceDurationFirst("14480 РУБ./НЕД.");
        setPriceDurationSecond("14480 РУБ./МЕС.");
        setPriceDurationThird("48000 РУБ./ГОД.");
        setPriceOldFirst("14480 РУБ./НЕД.");
        setPriceOldSecond("14480 РУБ./МЕС.");
        setPriceOldThird("48000 РУБ./ГОД.");
    }

    const setPriceRangeFirst = (e) => {
        setNumFilialFirst(e.target.value);
        if(activeIndex === 0){
            setPriceDurationFirst(countPrices(numFilialFirst, 300).resultPrice + ' РУБ./НЕД.');
            setPriceOldFirst(countPrices(numFilialFirst, 300).oldPrice + ' РУБ./НЕД.');
        }
        if(activeIndex === 1){
            setPriceDurationFirst(countPrices(numFilialFirst, 1200).resultPrice + ' РУБ./МЕС.');
            setPriceOldFirst(countPrices(numFilialFirst, 1200).oldPrice + ' РУБ./МЕС.');
        }
        if(activeIndex === 2){
            setPriceDurationFirst(countPrices(numFilialFirst, 14480).resultPrice + ' РУБ./ГОД.');
            setPriceOldFirst(countPrices(numFilialFirst, 14480).oldPrice + ' РУБ./ГОД.');
        }
    }

    const setPriceRangeSecond = (e) => {
        setNumFilialSecond(e.target.value);
        if(activeIndex === 0){
            setPriceDurationSecond(countPrices(numFilialSecond, 300).resultPrice + ' РУБ./НЕД.');
            setPriceOldSecond(countPrices(numFilialSecond, 300).oldPrice + ' РУБ./НЕД.');
        }
        if(activeIndex === 1){
            setPriceDurationSecond(countPrices(numFilialSecond, 1200).resultPrice + ' РУБ./МЕС.');
            setPriceOldSecond(countPrices(numFilialSecond, 1200).oldPrice + ' РУБ./МЕС.');
        }
        if(activeIndex === 2){
            setPriceDurationSecond(countPrices(numFilialSecond, 14480).resultPrice + ' РУБ./ГОД.');
            setPriceOldSecond(countPrices(numFilialSecond, 14480).oldPrice + ' РУБ./ГОД.');
        }
    }

    const setPriceRangeThird = (e) => {
        setNumFilialThird(e.target.value);
        if(activeIndex === 0){
            setPriceDurationThird(countPrices(numFilialThird, 1000).resultPrice + ' РУБ./НЕД.');
            setPriceOldThird(countPrices(numFilialThird, 1000).oldPrice + ' РУБ./НЕД.');
        }
        if(activeIndex === 1){
            setPriceDurationThird(countPrices(numFilialThird, 4000).resultPrice + ' РУБ./МЕС.');
            setPriceOldThird(countPrices(numFilialThird, 4000).oldPrice + ' РУБ./МЕС.');
        }
        if(activeIndex === 2){
            setPriceDurationThird(countPrices(numFilialThird, 14480).resultPrice + ' РУБ./ГОД.');
            setPriceOldThird(countPrices(numFilialThird, 14480).oldPrice + ' РУБ./ГОД.');
        }
    }



    return (
        <>
            <div className="wrapper-for-buttons">
                <div className="for-buttons">
                    <button className={activeIndex === 0 ? 'button-for-rate active-button' : 'button-for-rate'}
                            onClick={handleClickFirstPrice}>На неделю
                    </button>
                    <button className={activeIndex === 1 ? 'button-for-rate active-button' : 'button-for-rate'}
                            onClick={handleClickSecondPrice}>На месяц
                    </button>
                    <button className={activeIndex === 2 ? 'button-for-rate active-button' : 'button-for-rate'}
                            onClick={handleClickThirdPrice}>На 1 год
                    </button>
                </div>
            </div>

            <div id="list-of-prices">
                <div className= 'table-for-price-first'>
                    <h3><b>“Генератор отзывов”</b></h3>
                    <h5>{numFilialFirst} филиал</h5>
                    <Form.Range className="range-for-prices"
                        value={numFilialFirst}
                        max={150}
                        min={1}
                        onChange={setPriceRangeFirst}/>
                    <h4><b>{priceDurationFirst}</b></h4>
                    <div className="block-ranges-prices">
                        {priceDurationFirst != priceOldFirst && <h6 className="strike-text">{priceOldFirst}</h6>}
                    </div>
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
                <div className= 'table-for-price-second'>
                    <h3><b>Какое-то название</b></h3>
                    <h5>{numFilialSecond} филиал</h5>
                    <Form.Range className="range-for-prices"
                        value={numFilialSecond}
                        max={150}
                        min={1}
                        onChange={setPriceRangeSecond}/>
                    <h4><b>{priceDurationSecond}</b></h4>
                    <div className="block-ranges-prices">
                        {priceDurationSecond != priceOldSecond && <h6 className="strike-text">{priceOldSecond}</h6>}
                    </div>
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
                <div className='table-for-price-third'>
                    <h3><b>Репутация под ключ</b></h3>
                    <h5>{numFilialThird} филиал</h5>
                    <Form.Range className="range-for-prices"
                        value={numFilialThird}
                        max={150}
                        min={1}
                        onChange={setPriceRangeThird}/>
                    <h4><b>{priceDurationThird}</b></h4>
                    <div className="block-ranges-prices">
                        {priceDurationThird != priceOldThird && <h6 className="strike-text">{priceOldThird}</h6>}
                    </div>
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
                <Carousel className="carousel-for-prices" interval={null}>
                    <Carousel.Item>
                        <div className='table-for-price-first'>
                            <h3><b>“Генератор отзывов”</b></h3>
                            <h5>{numFilialFirst} филиал</h5>
                            <Form.Range className="range-for-prices"
                                value={numFilialFirst}
                                max={150}
                                min={1}
                                onChange={setPriceRangeFirst}/>
                            <h4><b>{priceDurationFirst}</b></h4>
                            <div className="block-ranges-prices">
                                {priceDurationFirst != priceOldFirst && <h6 className="strike-text">{priceOldFirst}</h6>}
                            </div>
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
                    <Carousel.Item>

                        <div className= 'table-for-price-second'>
                            <h3><b>Какое-то название</b></h3>
                            <h5>{numFilialSecond} филиал</h5>
                            <Form.Range className="range-for-prices"
                                value={numFilialSecond}
                                max={150}
                                min={1}
                                onChange={setPriceRangeSecond}/>
                            <h4><b>{priceDurationSecond}</b></h4>
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
                    <Carousel.Item>

                        <div className= 'table-for-price-third'>
                            <h3><b>Репутация под ключ</b></h3>
                            <h5>{numFilialThird} филиал</h5>
                            <Form.Range className="range-for-prices"
                                value={numFilialThird}
                                max={150}
                                min={1}
                                onChange={setPriceRangeThird}/>
                            <h4><b>{priceDurationThird}</b></h4>
                            <div className="block-ranges-prices">
                                {priceDurationThird != priceOldThird && <h6 className="strike-text">{priceOldThird}</h6>}
                            </div>
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

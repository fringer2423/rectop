import React, {useState, useRef} from "react";
import "../css/prices.css"
import {
    countPrices,
    countWeekDefaultPrice,
    countYearDefaultPrice
} from "../helpers/countPrices.js"

import {
    Carousel,
    Form,
    Button
} from 'react-bootstrap';

import {FontAwesomeIcon} from '@fortawesome/react-fontawesome';

import {faArrowRightLong} from '@fortawesome/free-solid-svg-icons';
import {faArrowLeftLong} from '@fortawesome/free-solid-svg-icons';

const Prices = () => {

    const priceMonth = {
        first: 1200,
        second: 1200,
        third: 4000
    }

    const priceWeek = {
        first: countWeekDefaultPrice(priceMonth.first),
        second: countWeekDefaultPrice(priceMonth.second),
        third: countWeekDefaultPrice(priceMonth.third)
    }

    const priceYear = {
        first: countYearDefaultPrice(priceMonth.first),
        second: countYearDefaultPrice(priceMonth.second),
        third: countYearDefaultPrice(priceMonth.third)
    }

    const [activeIndex, setActiveIndex] = useState(0);
    const [numBranchsFirst, setNumBranchsFirst] = useState(1);
    const [numBranchsSecond, setNumBranchsSecond] = useState(1);
    const [numBranchsThird, setNumBranchsThird] = useState(1);

    const [priceDurationFirst, setPriceDurationFirst] = useState(priceWeek.first + 'РУБ./НЕД.');
    const [priceDurationSecond, setPriceDurationSecond] = useState(priceWeek.second + 'РУБ./НЕД.');
    const [priceDurationThird, setPriceDurationThird] = useState(priceWeek.third + 'РУБ./НЕД.');

    const [priceOldFirst, setPriceOldFirst] = useState('');
    const [priceOldSecond, setPriceOldSecond] = useState('');
    const [priceOldThird, setPriceOldThird] = useState('');

    const [saleFirst, setSaleFirst] = useState('');
    const [saleSecond, setSaleSecond] = useState('');
    const [saleThird, setSaleThird] = useState('');

    const refFirst = useRef();
    const refSecond = useRef();
    const refThird = useRef();

    const toSetThirdPrice = () => {
        if (activeIndex === 0) {
            setPriceDurationThird(countPrices(numBranchsThird, priceWeek.third).resultPrice + ' РУБ./НЕД.');
            setPriceOldThird(countPrices(numBranchsThird, priceWeek.third).oldPrice + ' РУБ./НЕД.');
            setSaleThird('Скидка: ' + countPrices(numBranchsThird, priceWeek.third).sale + '%');
        }
        if (activeIndex === 1) {
            setPriceDurationThird(countPrices(numBranchsThird, priceMonth.third).resultPrice + ' РУБ./МЕС.');
            setPriceOldThird(countPrices(numBranchsThird, priceMonth.third).oldPrice + ' РУБ./МЕС.');
            setSaleThird('Скидка: ' + countPrices(numBranchsThird, priceMonth.third).sale + '%');
        }
        if (activeIndex === 2) {
            setPriceDurationThird(countPrices(numBranchsThird, priceYear.third).resultPrice + ' РУБ./ГОД.');
            setPriceOldThird(countPrices(numBranchsThird, priceYear.third).oldPrice + ' РУБ./ГОД.');
            setSaleThird('Скидка: ' + countPrices(numBranchsThird, priceYear.third).sale + '%');
        }
    }

    const toSetSecondPrice = () => {
        if (activeIndex === 0) {
            setPriceDurationSecond(countPrices(numBranchsSecond, priceWeek.second).resultPrice + ' РУБ./НЕД.');
            setPriceOldSecond(countPrices(numBranchsSecond, priceWeek.second).oldPrice + ' РУБ./НЕД.');
            setSaleSecond('Скидка: ' + countPrices(numBranchsSecond, priceWeek.second).sale + '%');
        }
        if (activeIndex === 1) {
            setPriceDurationSecond(countPrices(numBranchsSecond, priceMonth.second).resultPrice + ' РУБ./МЕС.');
            setPriceOldSecond(countPrices(numBranchsSecond, priceMonth.second).oldPrice + ' РУБ./МЕС.');
            setSaleSecond('Скидка: ' + countPrices(numBranchsSecond, priceMonth.second).sale + '%');
        }
        if (activeIndex === 2) {
            setPriceDurationSecond(countPrices(numBranchsSecond, priceYear.second).resultPrice + ' РУБ./ГОД.');
            setPriceOldSecond(countPrices(numBranchsSecond, priceYear.second).oldPrice + ' РУБ./ГОД.');
            setSaleSecond('Скидка: ' + countPrices(numBranchsSecond, priceMonth.second).sale + '%')
        }
    }

    const toSetFirstPrice = () => {
        if (activeIndex === 0) {
            setPriceDurationFirst(countPrices(numBranchsFirst, priceWeek.first).resultPrice + ' РУБ./НЕД.');
            setPriceOldFirst(countPrices(numBranchsFirst, priceWeek.first).oldPrice + ' РУБ./НЕД.');
            setSaleFirst('Скидка: ' + countPrices(numBranchsFirst, priceWeek.first).sale + '%');
        }
        if (activeIndex === 1) {
            setPriceDurationFirst(countPrices(numBranchsFirst, priceMonth.first).resultPrice + ' РУБ./МЕС.');
            setPriceOldFirst(countPrices(numBranchsFirst, priceMonth.first).oldPrice + ' РУБ./МЕС.');
            setSaleFirst('Скидка: ' + countPrices(numBranchsFirst, priceMonth.first).sale + '%');
        }
        if (activeIndex === 2) {
            setPriceDurationFirst(countPrices(numBranchsFirst, priceYear.first).resultPrice + ' РУБ./ГОД.');
            setPriceOldFirst(countPrices(numBranchsFirst, priceYear.first).oldPrice + ' РУБ./ГОД.');
            setSaleFirst('Скидка: ' + countPrices(numBranchsFirst, priceYear.first).sale + '%');
        }
    }

    const handleFirstRightClick = () => {
        if (parseInt(refFirst.current.value) <= 149){
            setNumBranchsFirst(parseInt(refFirst.current.value) + 1);
            toSetFirstPrice();
        }
    }

    const handleFirstLeftClick = () => {
        if(parseInt(refFirst.current.value) >= 2){
            setNumBranchsFirst(parseInt(refFirst.current.value) - 1);
            console.log(parseInt(refFirst.current.value) - 1)
            toSetFirstPrice();
        }
    }

    const handleSecondRightClick = () => {
        if(parseInt(refSecond.current.value) <= 149){
            setNumBranchsSecond(parseInt(refSecond.current.value) + 1);
            console.log(parseInt(refSecond.current.value) + 1);
            toSetSecondPrice();
        }
    }

    const handleSecondLeftClick = () => {
        if(parseInt(refSecond.current.value) >= 2){
            setNumBranchsSecond(parseInt(refSecond.current.value) - 1);
            console.log(parseInt(refFirst.current.value) - 1)
            toSetSecondPrice();
        }
    }

    const handleThirdRightClick = () => {
        if (parseInt(refThird.current.value) <= 149){
            setNumBranchsThird(parseInt(refThird.current.value) + 1);
            toSetThirdPrice();
        }
    }

    const handleThirdLeftClick = () => {
        if(parseInt(refThird.current.value) >= 2){
            setNumBranchsThird(parseInt(refThird.current.value) - 1);
            console.log(parseInt(refThird.current.value) - 1)
            toSetThirdPrice();
        }
    }

    const handleClickFirstPrice = () => {
        setActiveIndex(0);
        setPriceDurationFirst(countPrices(numBranchsFirst, priceWeek.first).resultPrice + ' РУБ./НЕД.');
        setPriceDurationSecond(countPrices(numBranchsSecond, priceWeek.second).resultPrice + ' РУБ./НЕД.');
        setPriceDurationThird(countPrices(numBranchsThird, priceWeek.third).resultPrice + ' РУБ./НЕД.');
        setPriceOldFirst(countPrices(numBranchsFirst, priceWeek.first).oldPrice + ' РУБ./НЕД.');
        setPriceOldSecond(countPrices(numBranchsSecond, priceWeek.second).oldPrice + ' РУБ./НЕД.');
        setPriceOldThird(countPrices(numBranchsThird, priceWeek.third).oldPrice + ' РУБ./НЕД.');

    }

    const handleClickSecondPrice = () => {
        setActiveIndex(1);
        setPriceDurationFirst(countPrices(numBranchsFirst, priceMonth.first).resultPrice + ' РУБ./МЕС.');
        setPriceDurationSecond(countPrices(numBranchsSecond, priceMonth.second).resultPrice + ' РУБ./МЕС.');
        setPriceDurationThird(countPrices(numBranchsThird, priceMonth.third).resultPrice + ' РУБ./МЕС.');
        setPriceOldFirst(countPrices(numBranchsFirst, priceMonth.first).oldPrice + ' РУБ./МЕС.');
        setPriceOldSecond(countPrices(numBranchsSecond, priceMonth.second).oldPrice + ' РУБ./МЕС.');
        setPriceOldThird(countPrices(numBranchsThird, priceMonth.third).oldPrice + ' РУБ./МЕС.');
    }

    const handleClickThirdPrice = () => {
        setActiveIndex(2);
        setPriceDurationFirst(countPrices(numBranchsFirst, priceYear.first).resultPrice + ' РУБ./ГОД.');
        setPriceDurationSecond(countPrices(numBranchsSecond, priceYear.second).resultPrice + ' РУБ./ГОД.');
        setPriceDurationThird(countPrices(numBranchsThird, priceYear.third).resultPrice + ' РУБ./ГОД.');
        setPriceOldFirst(countPrices(numBranchsFirst, priceYear.first).oldPrice + ' РУБ./ГОД.');
        setPriceOldSecond(countPrices(numBranchsSecond, priceYear.second).oldPrice + ' РУБ./ГОД.');
        setPriceOldThird(countPrices(numBranchsThird, priceYear.third).oldPrice + ' РУБ./ГОД.');
    }

    const setPriceRangeFirst = (e) => {
        setNumBranchsFirst(e.target.value);
        toSetFirstPrice();
    }

    const setPriceRangeSecond = (e) => {
        setNumBranchsSecond(e.target.value);
        toSetSecondPrice();
    }

    const setPriceRangeThird = (e) => {
        setNumBranchsThird(e.target.value);
        toSetThirdPrice();
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
                <div className='table-for-price-first'>
                    <h3><b>“Генератор отзывов”</b></h3>
                    <h5>{numBranchsFirst} филиал</h5>
                    <div className="wraper-spiner">
                        <button className="control-button-spinner" onClick={handleFirstLeftClick}>-</button>
                        <Form.Range className="range-for-prices"
                                    ref={refFirst}
                                    value={numBranchsFirst}
                                    max={150}
                                    min={1}
                                    onChange={setPriceRangeFirst}/>
                        <button className="control-button-spinner" onClick={handleFirstRightClick}>+</button>
                    </div>
                    <h4><b>{priceDurationFirst}</b></h4>
                    <div className="block-ranges-prices">
                        {priceDurationFirst !== priceOldFirst &&
                            <span className="strike-text">{priceOldFirst}</span>}
                        {priceDurationFirst !== priceOldFirst &&
                            <span className="discount">{saleFirst}</span>}
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
                <div className='table-for-price-second'>
                    <h3><b>Какое-то название</b></h3>
                    <h5>{numBranchsSecond} филиал</h5>
                    <div className="wraper-spiner">
                        <button className="control-button-spinner" onClick={handleSecondLeftClick}>-</button>
                        <Form.Range className="range-for-prices"
                                    value={numBranchsSecond}
                                    ref={refSecond}
                                    max={150}
                                    min={1}
                                    onChange={setPriceRangeSecond}/>
                        <button className="control-button-spinner" onClick={handleSecondRightClick}>+</button>
                    </div>
                    <h4><b>{priceDurationSecond}</b></h4>
                    <div className="block-ranges-prices">
                        {priceDurationSecond !== priceOldSecond &&
                            <span className="strike-text">{priceOldSecond}</span>
                        }
                        {priceDurationSecond !== priceOldSecond &&
                            <span className="discount">{saleSecond}</span>}
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
                    <h5>{numBranchsThird} филиал</h5>
                    <div className="wraper-spiner">
                        <button className="control-button-spinner" onClick={handleThirdLeftClick}>-</button>
                        <Form.Range className="range-for-prices"
                                    value={numBranchsThird}
                                    ref={refThird}
                                    max={150}
                                    min={1}
                                    onChange={setPriceRangeThird}/>
                        <button className="control-button-spinner" onClick={handleThirdRightClick}>+</button>
                    </div>
                    <h4><b>{priceDurationThird}</b></h4>
                    <div className="block-ranges-prices">
                        {priceDurationThird !== priceOldThird &&
                            <span className="strike-text">{priceOldThird}</span>}
                        {priceDurationThird !== priceOldThird &&
                            <span className="discount">{saleThird}</span>}
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
                            <h5>{numBranchsFirst} филиал</h5>
                            <div className="wraper-spiner">
                                <button className="control-button-spinner" onClick={handleFirstLeftClick}>-</button>
                                <Form.Range className="range-for-prices"
                                            value={numBranchsFirst}
                                            ref={refFirst}
                                            max={150}
                                            min={1}
                                            onChange={setPriceRangeFirst}/>
                                <button className="control-button-spinner" onClick={handleFirstRightClick}>+</button>
                            </div>
                            <h4><b>{priceDurationFirst}</b></h4>
                            <div className="block-ranges-prices">
                                {priceDurationFirst !== priceOldFirst &&
                                    <span className="strike-text">{priceOldFirst}</span>}
                                {priceDurationFirst !== priceOldFirst &&
                                    <span className="discount">{saleFirst}</span>}
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

                        <div className='table-for-price-second'>
                            <h3><b>Какое-то название</b></h3>
                            <h5>{numBranchsSecond} филиал</h5>
                            <div className="wraper-spiner">
                                <button className="control-button-spinner" onClick={handleSecondLeftClick}>-</button>
                                <Form.Range className="range-for-prices"
                                            value={numBranchsSecond}
                                            ref={refSecond}
                                            max={150}
                                            min={1}
                                            onChange={setPriceRangeSecond}/>
                                <button className="control-button-spinner" onClick={handleSecondRightClick}>+</button>
                            </div>
                            <h4><b>{priceDurationSecond}</b></h4>
                            <div className="block-ranges-prices">
                                {priceDurationSecond !== priceOldSecond &&
                                    <span className="strike-text">{priceOldSecond}</span>}
                                {priceDurationSecond !== priceOldSecond &&
                                    <span className="discount">{saleSecond}</span>}
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

                    </Carousel.Item>
                    <Carousel.Item>

                        <div className='table-for-price-third'>
                            <h3><b>Репутация под ключ</b></h3>
                            <h5>{numBranchsThird} филиал</h5>
                            <div className="wraper-spiner">
                                <button className="control-button-spinner" onClick={handleThirdLeftClick}>-</button>
                                <Form.Range className="range-for-prices"
                                            value={numBranchsThird}
                                            ref={refThird}
                                            max={150}
                                            min={1}
                                            onChange={setPriceRangeThird}/>
                                <button className="control-button-spinner" onClick={handleThirdRightClick}>+</button>
                            </div>
                            <h4><b>{priceDurationThird}</b></h4>
                            <div className="block-ranges-prices">
                                {priceDurationThird !== priceOldThird &&
                                    <span className="strike-text">{priceOldThird}</span>}
                                {priceDurationThird !== priceOldThird &&
                                    <span className="discount">{saleThird}</span>}
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

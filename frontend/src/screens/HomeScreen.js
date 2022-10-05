import React, {useEffect} from 'react'
import {useDispatch, useSelector} from 'react-redux'
import {Row, Col, Container, Button, Carousel, Card} from 'react-bootstrap'
import * as url from "url";


function HomeScreen() {


    return (
        <body className="mycustom-scroll parent-container" data-mcs-theme="minimal-dark">
            <Container className="col-lg-7 pt-5 mt-4 p-4">
                <Card id="mainCard1" className="card border-0 mx-auto w-100 pt-5 m-lg-0">
                    <Row className="row pt-3 pt-lg-5">
                        <Col className="col-lg-6 col-md-6 col-12">
                            <div className="card-body">
                                <p className="card-text">
                                    Негативные отзывы теперь в прошлом
                                </p>
                                <h3 className="card-title">
                                    <span className="text-primary font-weight-bolder">
                                        RecTop </span> - инновационный сервис взаимодействия с клиентами.
                                </h3>
                                <p className="card-text">
                                    <small className="text-muted">
                                        Отзывы собираются по QR-коду, когда клиент посещает заведение или сайт.
                                    </small>
                                </p>
                                <div className="row flex-nowrap p-2 p-lg-0">
                                    <Button type="button"
                                            className="btn btn-primary bg-gradient text-nowrap rounded-pill col-lg-5 col-6 m-lg-2">
                                        7 дней бесплатно
                                    </Button>
                                    <button type="button"
                                            className="btn btn-outline-primary bg-gradient text-nowrap rounded-pill col-lg-5 col-6 m-lg-2 mx-2 mx-lg-0">
                                        Запросить демо
                                    </button>
                                </div>
                            </div>
                        </Col>
                        <div className="col-lg-6 col-md-6 col-12">
                            <img alt='' id="mainCard1Img" src="/images/main/mainCard1Img.png" className="w-100"/>
                        </div>
                    </Row>
                </Card>

                <img alt='' id="afterCard1Img" className="d-lg-block d-none"
                     src="/images/main/afterMainCard1Img.png"/>

                <section id="mainCard2" className="card border-0 mx-auto w-100 mt-4 m-lg-0">
                    <div className="row">
                        <div className="col-lg-6 col-md-6">
                            <div className="card-body">
                                <h3 className="card-title">
                                    О компании <span className="text-primary font-weight-bolder">RecTop</span>
                                </h3>
                                <p className="card-text">
                                    Качественно повышаем вашу репутацию
                                </p>
                                <p className="card-text">
                                    <small className="text-muted">
                                        <span className="text-bolder">
                                            RecTop
                                        </span>
                                        - это бизнес-решение для тех, кто хочет получать дополнительный трафик за счёт
                                        сбора и мониторинга отзывов.
                                    </small>
                                </p>
                                <div className="row m-1">
                                    <div className="col-2 text-primary">
                                        <hr/>
                                    </div>
                                    <div className="col-8">
                                        <p className="card-text">
                                            <small className="text-muted">
                                                Обратная связь с недовольными клиентами позволит разрешить конфликтную
                                                ситуацию вовремя и без последствий. Получайте уведомления о новых
                                                отзывах в Telegram, отвечайте из личного кабинета.
                                            </small>
                                        </p>
                                    </div>
                                </div>
                            </div>
                        </div>
                        <div className="col-lg-6 col-md-6 mt-3">
                            <img alt='' src="/images/main/mainCard2Img.png" className="img-fluid"/>
                        </div>
                    </div>
                </section>

                <section id="mainCard3" className="card border-0 mx-auto w-100">
                    <div className="card-body">
                        <h3 className="card-title text-center m-2">
                            Почему <span className="text-primary font-weight-bolder">RecTop</span>
                        </h3>
                        <div className="row align-items-end mt-3">
                            <img alt='' src="/images/main/mainCard31Img.png"
                                 className="col-lg-3 col-md-3 col-10 mx-lg-0 mx-auto my-lg-0 my-4 h-50"/>
                            <img alt='' src="/images/main/mainCard32Img.png"
                                 className="col-lg-3 col-md-3 col-10 mx-lg-0 mx-auto h-75"/>
                            <img alt='' src="/images/main/mainCard33Img.png"
                                 className="col-lg-3 col-md-3 col-10 mx-lg-0 mx-auto my-lg-0 my-4"/>
                            <img alt='' src="/images/main/mainCard34Img.png"
                                 className="col-lg-3 col-md-3 col-10 mx-lg-0 mx-auto h-75"/>
                        </div>
                    </div>
                </section>

                <section id="mainCard4" className="card border-0 mx-auto w-100 mt-0">
                    <div className="row w-100">
                        <div className="card-body w-100">
                            <h3 className="card-title text-center m-4">
                                Получайте <span className="text-primary font-weight-bolder">положительные </span>
                                отзывы
                            </h3>
                            <p className="card-text text-center">
                                <small className="text-muted">
                                    Наша команда ежедневно просматривает и анализирует крупнейшие популярные сервисы по
                                    сбору отзывов
                                </small>
                            </p>
                            <p className="card-text text-center m-2">
                                Больше положительных отзывов = Больше доверия = Больше продаж
                            </p>
                            <div className="row d-flex flex-lg-wrap flex-nowrap mt-5 justify-content-center">
                                <Carousel slide id="carouselPlatforms" className="carousel carousel-dark slide"
                                     data-bs-ride="carousel" data-bs-interval="false">
                                    <div className="carousel-indicators my-2 align-self-end">
                                        <button type="button" data-bs-target="#carouselPlatforms"
                                                data-bs-slide-to="0" className="active" aria-current="true"
                                                aria-label="Slide 1"></button>
                                        <button type="button" data-bs-target="#carouselPlatforms"
                                                data-bs-slide-to="1" aria-label="Slide 2"></button>
                                        <button type="button" data-bs-target="#carouselPlatforms"
                                                data-bs-slide-to="2" aria-label="Slide 3"></button>
                                        <button type="button" data-bs-target="#carouselPlatforms"
                                                data-bs-slide-to="3" aria-label="Slide 4"></button>
                                    </div>
                                    <div className="carousel-inner mb-4">
                                        <Carousel.Item className="carousel-item active">
                                            <Row>
                                                <div
                                                    className="card border-0 col-lg-3 col-6 col-md-6 align-items-center">
                                                    <img alt='' className="w-75"
                                                         src="/images/main/mainCard41Img.png"/>
                                                    <div className="card-body">
                                                        <h4 className="card-title text-center m-2">
                                                            Яндекс Карты
                                                        </h4>
                                                        <p className="card-text text-center">
                                                            <small className="text-muted">
                                                                55 млн чел./месяц
                                                            </small>
                                                        </p>
                                                    </div>
                                                </div>
                                                <div
                                                    className="card border-0 col-lg-3 col-6 col-md-6 align-items-center">
                                                    <img alt='' className="w-75"
                                                         src="/images/main/mainCard42Img.png"/>
                                                    <div className="card-body">
                                                        <h4 className="card-title text-center m-2">
                                                            Google Карты
                                                        </h4>
                                                        <p className="card-text text-center">
                                                            <small className="text-muted">
                                                                30 млн чел./месяц
                                                            </small>
                                                        </p>
                                                    </div>
                                                </div>
                                            </Row>
                                        </Carousel.Item>
                                        <div className="carousel-item">
                                            <div className="row">
                                                <div
                                                    className="card border-0 col-lg-3 col-6 col-md-6 align-items-center">
                                                    <img alt='' className="w-75" src="/images/main/mainCard43Img.png"/>
                                                    <div className="card-body">
                                                        <h4 className="card-title text-center m-2">
                                                            2ГИС
                                                        </h4>
                                                        <p className="card-text text-center">
                                                            <small className="text-muted">
                                                                30 млн чел./месяц
                                                            </small>
                                                        </p>
                                                    </div>
                                                </div>
                                                <div
                                                    className="card border-0 col-lg-3 col-6 col-md-6 align-items-center">
                                                    <img alt='' className="w-75" src="/images/main/mainCard44Img.png"/>
                                                    <div className="card-body">
                                                        <h4 className="card-title text-center m-2">
                                                            Wildberries
                                                        </h4>
                                                        <p className="card-text text-center">
                                                            <small className="text-muted">
                                                                92 млн чел./месяц
                                                            </small>
                                                        </p>
                                                    </div>
                                                </div>
                                            </div>
                                        </div>
                                        <div className="carousel-item">
                                            <div className="row">
                                                <div
                                                    className="card border-0 col-lg-3 col-6 col-md-6 align-items-center">
                                                    <img alt='' className="w-75" src="/images/main/mainCard45Img.png"/>
                                                    <div className="card-body">
                                                        <h4 className="card-title text-center m-2">
                                                            Zoon
                                                        </h4>
                                                        <p className="card-text text-center">
                                                            <small className="text-muted">
                                                                24 млн чел./месяц
                                                            </small>
                                                        </p>
                                                    </div>
                                                </div>
                                                <div
                                                    className="card border-0 col-lg-3 col-6 col-md-6 align-items-center">
                                                    <img alt='' className="w-75" src="/images/main/mainCard46Img.png"/>
                                                    <div className="card-body">
                                                        <h4 className="card-title text-center m-2">
                                                            OZON
                                                        </h4>
                                                        <p className="card-text text-center">
                                                            <small className="text-muted">
                                                                80 млн чел./месяц
                                                            </small>
                                                        </p>
                                                    </div>
                                                </div>
                                            </div>
                                        </div>
                                        <div className="carousel-item">
                                            <div className="row">
                                                <div
                                                    className="card border-0 col-lg-3 col-6 col-md-6 align-items-center">
                                                    <img alt='' className="w-75" src="/images/main/mainCard47Img.png"/>
                                                    <div className="card-body">
                                                        <h4 className="card-title text-center m-2">
                                                            Yell
                                                        </h4>
                                                        <p className="card-text text-center">
                                                            <small className="text-muted">
                                                                3 млн чел./месяц
                                                            </small>
                                                        </p>
                                                    </div>
                                                </div>
                                                <div
                                                    className="card border-0 col-lg-3 col-6 col-md-6 align-items-center">
                                                    <img alt='' className="w-75"
                                                         src="/images/main/mainCard48Img.png"/>
                                                    <div className="card-body">
                                                        <h4 className="card-title text-center m-2">
                                                            Flamp
                                                        </h4>
                                                        <p className="card-text text-center">
                                                            <small className="text-muted">
                                                                50 млн чел./месяц
                                                            </small>
                                                        </p>
                                                    </div>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </Carousel>
                            </div>
                        </div>
                    </div>
                </section>

                <img alt='' id="afterCard4Img" className="img-fluid mx-auto" src="/images/main/afterMainCard4Img.png"/>

                <section id="mainCard5" className="mx-auto w-100">
                    <div className="card row border-0 col-lg-6 col-md-6 mt-0">
                        <div className="card-body">
                            <h3 className="card-title">
                                Как мы <span className="text-primary font-weight-bolder">работаем?</span>
                            </h3>
                            <p className="card-text">
                                Сервис "Генератор отзывов"
                            </p>
                            <p className="card-text">
                                <small className="text-muted">
                                    Уникальный генератор отзывов о компании. Эффективно и просто: клиент сканирует
                                    QR-код, оставляет отзыв, вы получаете уведомления в Telegram.
                                </small>
                            </p>
                        </div>
                    </div>

                    <div className="row ml-5 m-0">
                        <img alt='' className="col-lg-6 col-md-6 mb-lg-0 mb-5 mt-3" src="/images/main/mainCard51Img.png"/>
                        <div className="card row border-0 col-lg-6 col-md-6 mt-3 mt-lg-5">
                            <div className="card-body">
                                <h3 className="card-title">
                                    Акцент на <span className="text-primary font-weight-bolder">положительных </span>
                                    отзывах
                                </h3>
                                <p className="card-text">
                                    Клиенту все понравилось?
                                </p>
                                <p className="card-text">
                                    <small className="text-muted">
                                        Довольные клиенты смогут оставлять отзывы в личной карточке компании – их увидят
                                        тысячи людей!
                                    </small>
                                </p>
                                <button type="button"
                                        className="btn btn-primary bg-gradient text-nowrap rounded-pill col-9 col-lg-7 mx-lg-0 my-3 mx-auto">
                                    Попробовать бесплатно
                                </button>
                            </div>
                        </div>
                    </div>

                    <div className="card row border-0 col-lg-12 m-0">
                        <div className="row">
                            <div className="card-body col-lg-6 col-md-6">
                                <h3 className="card-title mt-lg-3">
                                    <span className="text-primary font-weight-bolder">
                                        Негативные отзывы –
                                    </span>
                                    <br/>
                                    в службу поддержки
                                </h3>
                                <p className="card-text">
                                    Клиент не доволен?
                                </p>
                                <div className="row m-1 justify-content-center justify-content-lg-start">
                                    <div className="col-2 text-primary d-lg-block d-none">
                                        <hr/>
                                    </div>
                                    <div className="col-8 col-12">
                                        <p className="card-text text-start">
                                            <small className="text-muted text-lg-start text-center">
                                                Устраняйте конфликтные ситуации в чате службы поддержки в Telegram.
                                            </small>
                                        </p>
                                    </div>
                                </div>
                                <div className="row m-1 justify-content-center justify-content-lg-start">
                                    <div className="col-2 text-primary d-lg-block d-none">
                                        <hr/>
                                    </div>
                                    <div className="col-lg-8 col-12">
                                        <p className="card-text text-start">
                                            <small className="text-muted">
                                                Вовремя разрешённый конфликт – отсутствие негативных отзывов в сети.
                                            </small>
                                        </p>
                                    </div>
                                </div>
                                <button type="button"
                                        className="btn btn-primary bg-gradient text-nowrap rounded-pill col-9 col-lg-7 mx-lg-0 my-3 mx-auto">
                                    Попробовать бесплатно
                                </button>
                            </div>
                            <img alt='' className="col-lg-6 col-md-6 mt-3" src="/images/main/mainCard52Img.png"/>
                        </div>
                    </div>
                </section>

                <section id="mainCard6" className="card border-0 mt-5">
                    <div className="row col-lg-9 align-self-center">
                        <div className="card-body">
                            <h3 className="card-title text-center m-4">
                                <span className="text-primary font-weight-bolder">
                                    Как ликвидировать </span> негативные отзывы?
                            </h3>
                            <p className="card-text text-center m-2">
                                Один негативный отзыв - это 100 положительных, и если вы хотите его убрать, то лучше
                                ответить на него в момент возникновения
                            </p>
                        </div>
                    </div>
                    <div className="row m-1">
                        <div className="card col-lg-3 col-md-3 m-md-0 m-lg-0 col-12 border-0 align-self-start">
                            <div className="row">
                                <div className="card-body col-lg-12 col-1">
                                    <span className="h1 card-title text-primary">
                                        01
                                    </span>
                                    <p className="card-text h6 mt-4">
                                        Обратитесь по имени
                                    </p>
                                    <p className="card-text">
                                        <small className="text-muted">
                                            Обратитесь по имени и поблагодарите за оставленный отзыв.
                                        </small>
                                    </p>
                                </div>
                                <img alt='' className="cardImg61 m-lg-5 col-lg-6 col-md-12 m-md-3 col-6 h-25"
                                     src="/images/main/mainCard61Img.png"/>
                            </div>
                        </div>
                        <div className="card col-lg-3 col-md-3 m-md-0 m-lg-0  col-12 border-0 align-self-end">
                            <div className="row">
                                <img alt='' className="cardImg62 m-lg-5 col-lg-6 col-md-12 m-md-3  col-6 h-25"
                                     src="/images/main/mainCard62Img.png"/>
                                <div className="card-body col-lg-12 col-md-3 col-1">
                                    <span className="h1 card-title text-primary">
                                        02
                                    </span>
                                    <p className="card-text mt-4">
                                        <span className="card-text h6">
                                            Извинитесь,
                                        </span>
                                        <small className="text-muted">
                                            даже если вашей вины нет. Всегда будьте доброжелательны!
                                        </small>
                                    </p>
                                </div>
                            </div>
                        </div>
                        <div className="card col-lg-3 col-md-3 m-md-0 m-lg-0  col-12 border-0 align-self-start">
                            <div className="row">
                                <div className="card-body col-lg-12 col-1">
                                    <span className="h1 card-title text-primary">
                                        03
                                    </span>
                                    <p className="card-text mt-4">
                                        <span className="card-text h6">
                                            Сообщите
                                        </span>
                                        <small className="text-muted">
                                            о вашей готовности помочь в сложившейся ситуации.
                                        </small>
                                    </p>
                                </div>
                                <img alt='' className="cardImg61 m-lg-5 col-lg-6 col-md-12 m-md-3 col-6 h-25"
                                     src="/images/main/mainCard61Img.png"/>
                            </div>
                        </div>
                        <div className="card col-lg-3 col-md-3 m-md-0 m-lg-0 col-12 border-0 align-self-end">
                            <div className="row">
                                <img alt='' className="cardImg62 m-lg-5 col-lg-6 col-6 invisible"
                                     src="/images/main/mainCard62Img.png"/>
                                <div className="card-body col-lg-12 col-md-12 col-1">
                                    <span className="h1 card-title text-primary">
                                        04
                                    </span>
                                    <p className="card-text mt-4">
                                        <span className="card-text h6">
                                        Попросите клиента выслать
                                    </span>
                                        <small className="text-muted">
                                            контактные данные на ваш адрес.
                                        </small>
                                    </p>
                                </div>
                            </div>
                        </div>
                    </div>
                </section>

                <img alt='' id="afterCard6Img" src="/images/main/afterMainCard6Img.png"/>

                <section id="mainCard7" className="border-0 row justify-content-center mt-lg-0 mt-5">
                    <h3 className="text-center m-lg-4">
                        Выбирайте то, что удобно Вам для управления репутацией
                    </h3>
                    <div className="btn-group bg-light w-75 mt-3 mb-lg-3 rounded-pill mx-auto col-12"
                         role="group" aria-label="Базовая группа переключателей радио">
                        <input type="radio" className="btn-check" autoComplete="off"/>
                        <label
                            className="fst-btn-tarif btn btn-outline-primary bg-gradient text-dark border-0 rounded-pill"
                            htmlFor="btnradio1" data-tariff-class=".tarif-block:eq(0)" data-slide="0">
                            На неделю
                        </label>

                        <input type="radio" className="btn-check" autoComplete="off"/>
                        <label
                            className="btn btn-outline-primary bg-gradient text-dark border-0 rounded-pill"
                            htmlFor="btnradio2" data-tariff-class=".tarif-block:eq(1)"
                            data-slide="1">
                            На месяц
                        </label>

                        <input type="radio" className="btn-check" autoComplete="off"/>
                        <label
                            className="btn btn-outline-primary bg-gradient text-dark border-0 rounded-pill"
                            htmlFor="btnradio3" data-tariff-class=".tarif-block:eq(2)"
                            data-slide="2">
                            На год
                        </label>
                    </div>
                    <div className="carousel carousel-dark row g-0 p-0 m-0" data-bs-ride="carousel"
                         id="carouselTariff" data-bs-interval="false" data-bs-touch="false">
                        <div className="carousel-inner row m-lg-3 flex-nowrap">
                            <div className="carousel-item row active">
                                <div className="row m-1 m-lg-0 pb-3 flex-nowrap">
                                    <div
                                        className="tarif-block bg-gradient d-block col-lg-4 col-12 m-4 m-lg-2 p-0 row justify-content-center text-center border shadow">
                                        <p className="h5 text-dark mt-4">
                                            "Генератор Отзывов"
                                        </p>
                                        <p className="text-dark">
                                            1 филиал
                                        </p>
                                        <p className="h5 price">
                                            1200 РУБ./МЕС.
                                        </p>
                                        <div
                                            className="unner-tarif-block bg-primary bg-gradient text-white p-3 mx-auto my-3 col-10 shadow">
                                            <span><span className="fw-bold">
                                                Производите сбор отзывов
                                            </span>
                                                от ваших клиентов при помощи QR-кодов на точках продаж
                                            </span>
                                        </div>
                                        <div className="details-tariff col-lg-10 mx-auto">
                                            <span className="text-dark">
                                                Сбор отзывов
                                            </span>
                                            <hr className="mt-2"/>
                                        </div>
                                        <div className="details-tariff col-lg-10 mx-auto">
                                            <span className="text-dark">
                                                Оповещения в телеграме
                                            </span>
                                            <hr className="mt-2"/>
                                        </div>
                                        <div className="details-tariff col-lg-10 mx-auto">
                                            <span className="text-dark">
                                                Отчетность в телеграме
                                            </span>
                                            <hr className="mt-2"/>
                                        </div>
                                        <div className="details-tariff col-lg-10 mx-auto">
                                            <span className="text-dark">
                                                Система кешбэка
                                            </span>
                                            <hr className="mt-2"/>
                                        </div>
                                        <div className="details-tariff col-lg-10 mx-auto">
                                            <span className="text-dark">
                                                Статистика
                                            </span>
                                            <hr className="mt-2"/>
                                        </div>
                                        <div className="details-tariff col-lg-10 mx-auto">
                                            <span className="text-dark">
                                                Обратная связь
                                            </span>
                                            <hr className="mt-2"/>
                                        </div>
                                        <div className="details-tariff col-lg-10 mx-auto">
                                            <span className="text-dark">
                                                Поддержка 24/7
                                            </span>
                                            <hr className="mt-2"/>
                                        </div>
                                        <div className="details-tariff col-lg-10 mx-auto">
                                            <span className="text-dark">
                                                Формирование qr-кода
                                            </span>
                                            <hr className="mt-2"/>
                                        </div>
                                        <button type="button"
                                                className="getTariff btn btn-outline-primary bg-gradient text-nowrap rounded-pill align-self-end mb-3 mt-2 col-8 col-md-6">
                                            Приобрести тариф
                                        </button>
                                    </div>
                                </div>
                            </div>
                            <div className="carousel-item row">
                                <div className="row m-1 m-lg-0 flex-nowrap">
                                    <div
                                        className="tarif-block bg-gradient d-block col-lg-4 col-12 m-4 m-lg-2 p-0 row justify-content-end text-center border shadow">
                                        <p className="h5 text-dark mt-4">
                                            Какое-то название
                                        </p>
                                        <div className="col-8 mx-auto my-2 px-0">
                                            <label htmlFor="customRange2" className="for-range form-label text-dark">
                                                1 филиал
                                            </label>
                                            <div className="row flex-nowrap col-10 p-0">
                                                <button type="button"
                                                        className="range-btn range-minus-btn btn btn-sm rounded-circle btn-primary bg-gradient col-1 m-2"
                                                        data-range-id="customRange2">
                                                    <i className="bi bi-dash"/>
                                                </button>
                                                <input type="range" data-price-id="tariff-price-2"
                                                       className="form-range col-8" min="1" max="150"
                                                       id="customRange2" value="1"/>
                                                <button type="button"
                                                        className="range-btn range-plus-btn btn btn-sm rounded-circle btn-primary bg-gradient col-1 m-2"
                                                        data-range-id="customRange2">
                                                    <i className="bi bi-plus"/>
                                                </button>
                                            </div>
                                        </div>
                                        <p className="h5 price">
                                            от
                                            <span className="price-val" id="tariff-price-2">
                                                1200
                                            </span>
                                            РУБ./МЕС.
                                        </p>
                                        <span className="after-price-info d-none"
                                              data-price-id="tariff-price-2"/>
                                        <div
                                            className="unner-tarif-block bg-primary bg-gradient text-white p-3 mx-auto my-3 col-10 shadow">
                                            <span><span className="fw-bold">
                                                Работа с отзывами
                                            </span>
                                                на крупнейших интернет-площадках и сервисах
                                            </span>
                                        </div>
                                        <div className="details-tariff col-lg-10 mx-auto">
                                            <span className="text-dark">
                                                Аналитика по филиалу
                                            </span>
                                            <hr className="mt-2"/>
                                        </div>
                                        <div className="details-tariff col-lg-10 mx-auto">
                                            <span className="text-dark">
                                                Постоянная актуализация
                                            </span>
                                            <hr className="mt-2"/>
                                        </div>
                                        <div className="details-tariff col-lg-10 mx-auto">
                                            <span className="text-dark">
                                                Система кэшбека
                                            </span>
                                            <hr className="mt-2"/>
                                        </div>
                                        <div className="details-tariff col-lg-10 mx-auto">
                                            <span className="text-dark">
                                                Скидки от партнеров
                                            </span>
                                            <hr className="mt-2"/>
                                        </div>
                                        <div className="details-tariff col-lg-10 mx-auto">
                                            <span className="text-dark">
                                                Поддержка 24/7
                                            </span>
                                            <hr className="mt-2"/>
                                        </div>
                                        <div className="details-tariff col-lg-10 mx-auto">
                                                        <span
                                                            className="text-dark">
                                                            Ответы на отзывы в одном месте
                                                        </span>
                                            <hr className="mt-2"/>
                                        </div>
                                        <div className="details-tariff col-lg-10 mx-auto">
                                            <span className="text-dark">
                                                Обратная связь
                                            </span>
                                            <hr className="mt-2"/>
                                        </div>
                                        <div className="details-tariff col-lg-10 mx-auto">
                                            <span className="text-dark">
                                                Подробная аналитика
                                            </span>
                                            <hr className="mt-2"/>
                                        </div>
                                        <button type="button"
                                                className="getTariff btn btn-outline-primary bg-gradient text-nowrap rounded-pill align-self-end mb-3 mt-2 col-8 col-md-6">
                                            Приобрести тариф
                                        </button>
                                    </div>
                                </div>
                            </div>
                            <div className="carousel-item row">
                                <div className="row m-1 m-lg-0 flex-nowrap">
                                    <div
                                        className="tarif-block bg-gradient d-block col-lg-4 col-12 m-4 m-lg-2 p-0 row justify-content-end text-center border shadow">
                                        <p className="h5 text-dark mt-4">
                                            Репутация под ключ
                                        </p>
                                        <div className="row col-8 mx-auto my-2 px-0">
                                            <label htmlFor="customRange1"
                                                   className="for-range form-label text-dark">
                                                1 филиал
                                            </label>
                                            <div className="row flex-nowrap col-10 p-0">
                                                <button type="button"
                                                        className="range-btn range-minus-btn btn btn-sm rounded-circle btn-primary bg-gradient col-1 m-2"
                                                        data-range-id="customRange1">
                                                    <i className="bi bi-dash"/>
                                                </button>
                                                <input type="range" data-price-id="tariff-price-3"
                                                       className="form-range col-9" min="1" max="150"
                                                       id="customRange1" value="1"/>
                                                <button type="button"
                                                        className="range-btn range-plus-btn btn btn-sm rounded-circle btn-primary bg-gradient col-1 m-2"
                                                        data-range-id="customRange1">
                                                    <i className="bi bi-plus"/>
                                                </button>
                                            </div>
                                        </div>
                                        <p className="h5 price">
                                            от
                                            <span className="price-val" id="tariff-price-3">
                                                4000
                                            </span>
                                            РУБ./МЕС.
                                        </p>
                                        <span className="after-price-info d-none"
                                              data-price-id="tariff-price-3"/>
                                        <div
                                            className="unner-tarif-block bg-primary bg-gradient text-white p-3 mx-auto my-3 col-10 shadow">
                                            <span>
                                                <span className="fw-bold">
                                                    Работа с отзывами
                                                </span>
                                                на крупнейших интернет-площадках и сервисах
                                            </span>
                                        </div>
                                        <div className="details-tariff col-lg-10 mx-auto">
                                            <span className="text-dark">
                                                Генератор и агрегатор отзывов
                                            </span>
                                            <hr className="mt-2"/>
                                        </div>
                                        <div className="details-tariff col-lg-10 mx-auto">
                                            <span className="text-dark">
                                                Ответы на отзывы нашими специалистами
                                            </span>
                                            <hr className="mt-2"/>
                                        </div>
                                        <div className="details-tariff col-lg-10 mx-auto">
                                            <span className="text-dark">
                                                Проверка выставленных отзывов
                                            </span>
                                            <hr className="mt-2"/>
                                        </div>
                                        <div className="details-tariff col-lg-10 mx-auto">
                                                        <span className="text-dark">
                                                            "Спровоцируем" выставление отзывов
                                                        </span>
                                            <hr className="mt-2"/>
                                        </div>
                                        <div className="details-tariff col-lg-10 mx-auto">
                                            <span className="text-dark">
                                                Подробная отчетность
                                            </span>
                                            <hr className="mt-2"/>
                                        </div>
                                        <div className="details-tariff col-lg-10 mx-auto">
                                            <span className="text-dark">
                                                Аналитика в реальном времени
                                            </span>
                                            <hr className="mt-2"/>
                                        </div>
                                        <button type="button"
                                                className="getTariff btn btn-outline-primary bg-gradient text-nowrap rounded-pill align-self-end mb-3 mt-2 col-8 col-md-6">
                                            Приобрести тариф
                                        </button>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </section>

                <section id="mainCard8" className="row border-0 mt-5">
                    <div className="card border-0 col-lg-7 col-md-6">
                        <div className="card-body">
                            <h3 className="card-title">
                                Запишитесь на
                                <br/>
                                <span className="text-primary font-weight-bolder">
                                    бесплатный звонок
                                </span>
                            </h3>
                            <p className="card-text h6 mt-4 mb-3">
                                Наш менеджер перезвонит вам через 10 минут, в течение которых вы сможете:
                            </p>
                            <ul className="row p-1">
                                <li className="card-text row mb-4">
                                    <i className="circle-list bi bi-circle-fill text-primary col-1 align-self-center"/>
                                    <span className="col">
                                        Узнать все отзывы о своей компании и как их отработать.
                                    </span>
                                </li>
                                <li className="card-text row mb-4">
                                    <i className="circle-list bi bi-circle-fill text-primary col-1 align-self-center"/>
                                    <span className="col">
                                        Получить список интернет-ресурсов, на которых нужно зарегистрировать компанию.
                                    </span>
                                </li>
                                <li className="card-text row mb-4">
                                    <i className="circle-list bi bi-circle-fill text-primary col-1 align-self-center"/>
                                    <span className="col">
                                        Проанализировать общий рейтинг компании и каждой точки продаж в отдельности.
                                    </span>
                                </li>
                                <li className="card-text row mb-4">
                                    <i className="circle-list bi bi-circle-fill text-primary col-1 align-self-center"/>
                                    <span className="col">
                                        Узнать откуда берутся негативные отзывы и как удалить негативный отзыв без бюджета.
                                    </span>
                                </li>
                            </ul>
                            <p className="card-text h6 mt-4">
                                RecTop - Ваша репутация!
                            </p>
                        </div>
                    </div>
                    <div className="m-lg-0 m-1 col-lg-5 col-10 col-md-5 mx-auto">
                        <div className="bg-light border-0 rounded-3 p-4 mx-auto">
                            <h5 className="text-center">
                                Заполните форму заявки
                            </h5>
                            <p className="text-center">
                                Мы перезвоним в течение 10 минут
                            </p>
                            <form className="mt-3 row">
                                <div className="my-2">
                                    <input type="text"
                                           className="form-control rounded-pill border-primary text-center"
                                           placeholder="Ваше имя" id="exampleInputEmail1"
                                           aria-describedby="emailHelp"/>
                                </div>
                                <div className="my-2">
                                    <input type="tel"
                                           className="form-control rounded-pill border-primary text-center"
                                           placeholder="Ваше телефон" id="exampleInputEmail2"
                                           aria-describedby="emailHelp"/>
                                </div>
                                <div className="my-2">
                                    <input type="email"
                                           className="form-control rounded-pill border-primary text-center"
                                           placeholder="Ваш email" id="exampleInputEmail3"
                                           aria-describedby="emailHelp"/>
                                </div>
                                <div className="my-2">
                                    <input type="text"
                                           className="form-control rounded-pill border-primary text-center"
                                           placeholder="Название вашей компании" id="exampleInputEmail4"
                                           aria-describedby="emailHelp"/>
                                </div>
                                <button type="submit"
                                        className="btn btn-primary bg-gradient rounded-pill mt-5 col-8 mx-auto">
                                    Отправьте заявку
                                </button>
                            </form>
                        </div>
                    </div>
                </section>

                <img alt='' id="afterCard8Img" className="img-fluid mt-5 mx-auto"
                     src="/images/main/afterMainCard8Img.png"/>

                <section id="mainCard9" className="card border-0">
                    <div className="card-body row w-100">
                        <h3 className="card-title text-center mt-4 mb-5 fs-3">
                            Часто задаваемые вопросы
                        </h3>
                        <div className="row w-100">
                            <p className="text-left w-100">
                                <button
                                    className="btn button-question border-0 fs-5 w-100 d-flex justify-content-between p-0"
                                    type="button" data-bs-toggle="collapse"
                                    data-bs-target="#collapseExample" aria-expanded="false"
                                    aria-controls="collapseExample">
                                    <span
                                        className="question col-11 p-2 text-start">
                                        Какие виды отзывов вы агрегируете?
                                    </span>
                                    <span className="col-1 pt-2">
                                        <div className="pt-1">
                                        <i className="bi bi-plus text-primary"/>
                                    </div>
                                    </span>
                                </button>
                            </p>
                            <div className="collapse w-100 pb-0 mb-2" id="collapseExample">
                                <div className="card card-body border-0">
                                    Некоторый заполнитель для компонента сворачивания. Эта панель по
                                    умолчанию скрыта, но открывается, когда пользователь активирует
                                    соответствующий триггер.
                                </div>
                            </div>
                        </div>
                        <div className="row w-100">
                            <p className="text-left w-100">
                                <button
                                    className="btn button-question border-0 fs-5 w-100 d-flex justify-content-between p-0"
                                    type="button" data-bs-toggle="collapse"
                                    data-bs-target="#collapseExample2" aria-expanded="false"
                                    aria-controls="collapseExample2">
                                    <span className="question col-11 p-2 text-start">
                                        Чем мне будет полезен сервис RecTop?
                                    </span>
                                    <span className="col-1 pt-2">
                                        <div className="pt-1">
                                            <i className="bi bi-plus text-primary"/>
                                        </div>
                                    </span>
                                </button>
                            </p>
                            <div className="collapse pb-0 mb-2" id="collapseExample2">
                                <div className="card card-body border-0">
                                    Некоторый заполнитель для компонента сворачивания. Эта панель по
                                    умолчанию скрыта, но открывается, когда пользователь активирует
                                    соответствующий триггер.
                                </div>
                            </div>
                        </div>
                        <div className="row w-100">
                            <p className="text-left w-100">
                                <button
                                    className="btn button-question border-0 fs-5 w-100 d-flex justify-content-between p-0"
                                    type="button" data-bs-toggle="collapse"
                                    data-bs-target="#collapseExample3" aria-expanded="false"
                                    aria-controls="collapseExample3">
                                    <span className="question col-11 p-2 text-start">
                                        На чем основана ваша ценовая политика?
                                    </span>
                                    <span className="col-1 pt-2">
                                        <div className="pt-1">
                                            <i className="bi bi-plus text-primary"/>
                                        </div>
                                    </span>
                                </button>
                            </p>
                            <div className="collapse pb-0 mb-2" id="collapseExample3">
                                <div className="card card-body border-0">
                                    Некоторый заполнитель для компонента сворачивания. Эта панель по
                                    умолчанию скрыта, но открывается, когда пользователь активирует
                                    соответствующий триггер.
                                </div>
                            </div>
                        </div>
                        <div className="row w-100">
                            <p className="text-left w-100">
                                <button
                                    className="btn button-question border-0 fs-5 w-100 d-flex justify-content-between p-0"
                                    type="button" data-bs-toggle="collapse"
                                    data-bs-target="#collapseExample4" aria-expanded="false"
                                    aria-controls="collapseExample4">
                                    <span className="question col-11 p-2 text-start">
                                        Как часто я буду получать новые отзывы от RecTop?
                                    </span>
                                    <span className="col-1 pt-2">
                                        <div className="pt-1">
                                            <i className="bi bi-plus text-primary"/>
                                        </div>
                                    </span>
                                </button>
                            </p>
                            <div className="collapse pb-0 mb-2" id="collapseExample4">
                                <div className="card card-body border-0">
                                    Некоторый заполнитель для компонента сворачивания. Эта панель по
                                    умолчанию скрыта, но открывается, когда пользователь активирует
                                    соответствующий триггер.
                                </div>
                            </div>
                        </div>
                        <div className="row w-100">
                            <p className="text-left w-100">
                                <button
                                    className="btn button-question border-0 fs-5 w-100 d-flex justify-content-between p-0"
                                    type="button" data-bs-toggle="collapse"
                                    data-bs-target="#collapseExample5" aria-expanded="false"
                                    aria-controls="collapseExample5">
                                    <span className="question col-11 p-2 text-start">
                                        Любой мой сотрудник сможет получать уведомления о новых отзывах?
                                    </span>
                                    <span className="col-1 pt-2">
                                        <div className="pt-1">
                                            <i className="bi bi-plus text-primary"/>
                                        </div>
                                    </span>
                                </button>
                            </p>
                            <div className="collapse pb-0 mb-2" id="collapseExample5">
                                <div className="card card-body border-0">
                                    Некоторый заполнитель для компонента сворачивания. Эта панель по
                                    умолчанию скрыта, но открывается, когда пользователь активирует
                                    соответствующий триггер.
                                </div>
                            </div>
                        </div>
                    </div>
                </section>
            </Container>
        </body>
    )
}

export default HomeScreen
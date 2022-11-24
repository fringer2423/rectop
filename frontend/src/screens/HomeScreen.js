import React from 'react';

import {Container} from "react-bootstrap"

import "../css/main.css";
import "../css/buttons.css";
import "../css/whyBlocks.css";
import "../css/purpleBlock.css";
import "../css/blueBall.css"

import Prices from "../components/Prices";
import FormUser from "../components/FormUser";
import Refprogram from "../components/Refprogram";
import Accordion from "../components/Accordion";
import Header from '../components/Header'
import Footer from '../components/Footer'

import PurpleCircle from "../components/PurpleCircle";
import Brands from "../components/Brands";
import ListOfRec from "../components/ListOfRec";


import dataForAccordion from "../helpers/dataForAccordion";


const HomeScreen = () => {

    return (
        <div id="body">

            <Header/>
            <Container>
                <div id="first-block">
                    <div className="first-block-text">
                        <h2> Негативные отзывы теперь в прошлом!</h2>
                        <h1><b> <span className="gradient-text">RecTop</span> - инновационный сервис</b> <span
                            className="cursive-text special">взаимодействия с клиентами.</span></h1>
                        <br/><br/>
                        <div className="right-text-buttons-first-block">
                            <div className="small-text-first-block">
                                Отзывы собираются по QR-коду, когда клиент посещает заведение или сайт.
                            </div>
                            <button className="blue-button">7 дней бесплатно</button>
                            <button className="white-button">Запросить демо</button>
                        </div>
                    </div>
                    <img
                        src="/images/main/mainCard1Img.png"
                        className="first-image"
                        alt="first"
                    />
                    <img
                        src="/images/main/mainCard1ImgMobile.png"
                        className="first-img-for-mobile"
                        alt="first for mobile"
                    />

                </div>
                <div id="about">
                    <img
                        src='/images/main/blue_ball.png'
                        className="blue-ball"
                    />
                    <div className="about-comp-text">
                        <h1><b>О компании <span className="gradient-text">RecTop</span></b></h1>

                        <h2>Качественно повышаем вашу репутацию</h2>
                        <div className="small-text">
                            <b>RecTop</b> - это бизнес- решение для тех, кто хочет получать дополнительный трафик за
                            счёт
                            сбора и мониторинга отзывов.<br/><br/>
                            <ul>
                                <li>Обратная связь с недовольными клиентами позволит разрешить конфликтную ситуацию
                                    вовремя
                                    и без последствий. Получайте уведомления о новых отзывах в Telegram, отвечайте из
                                    личного кабинета
                                </li>
                            </ul>
                        </div>
                    </div>
                    <div>
                        <PurpleCircle/>
                    </div>
                </div>
                <div id="why-rectop">
                    <h1><b>Почему RecTop</b></h1>
                    <div className="why-blocks">
                        <div className="why-block">
                            <img
                                src="/images/pic1.svg"
                                alt="mobile"
                            />
                            <h2><b>Увеличим</b></h2>
                            <p><br/> положительные отзывы реальных клиентов на 50%</p>
                        </div>
                        <div className="why-block">
                            <img
                                src="/images/pic2.svg"
                                alt="mobile"
                            />
                            <h2><b>Освободим</b></h2>
                            <p><br/> 90% вашего времени на сбор клиентских отзывов</p>
                        </div>
                        <div className="why-block">
                            <img
                                src="/images/pic3.svg"
                                alt="mobile"
                            />
                            <h2><b>Мотивируем</b></h2>
                            <p><br/> клиентов на повторные продажи: кэшбэк за отзывы</p>
                        </div>
                        <div className="why-block">
                            <img
                                src="/images/pic4.svg"
                                alt="mobile"
                            />
                            <h2><b>Регулируем</b></h2>
                            <p><br/> конфликт вовремя, негативные отзывы получаете только Вы</p>
                        </div>
                    </div>
                </div>
                <div className="get-reports">
                    <h1>
                        <b>Получайте <span className="gradient-text">положительные</span> отзывы</b>
                    </h1>
                    <div className="get-reports-text">
                        Наша команда ежедневно просматривает и анализирует крупнейшие популярные сервисы по сбору
                        отзывов
                    </div>
                    <div className="get-reports-equality">
                        Больше положительных отзывов = Больше доверия = Больше продаж
                    </div>

                    <Brands/>

                    <img
                        src="/images/mobileforpurpleblock.png"
                        className="img-in-purple-block"
                        alt="mobile"
                    />
                    <div className="wrapper-for-purple-block">
                        <div className="purple-block">
                            <img
                                className="white-ellipse"
                                src="/images/4S.png"
                                alt="4S"
                            />
                            <div className="text-in-pb">
                                <h2><b>Сбор отзывов по QR-коду при посещении вашего заведения онлайн/оффлайн</b></h2>
                                <p>
                                    Уникальная система мотивации оставления отзывов от клиентов. Клиент получает кэшбек
                                    за
                                    отзыв
                                    на любом сервисе - его можно обменять на скидку/услугу у партнеров.
                                </p>
                            </div>
                            <img
                                src="/images/mobileforpurpleblockt.png"
                                className="img-in-purple-block-mobile"
                                alt="mobile half"
                            />
                        </div>
                    </div>
                </div>
                <div id="work">
                    <h1><b>Как мы <span className="gradient-text">работаем?</span></b></h1>
                    <h3>Сервис “Генератор отзывов”</h3>
                    <div className="small-text">
                        Уникальный генератор отзывов о компании. Эффективно и просто: клиент сканирует QR-код, оставляет
                        отзыв, вы получаете уведомления в Telegram.
                    </div>
                    <div className="block-with-pic-one">
                        <img
                            src="/images/main/mainCard51Img.png"
                            className="pic-in-block-one"
                            alt="mobile"
                        />
                        <div className="block-with-pic-one-text">
                            <h2><b>Акцент на <span className="gradient-text">положительных отзывах</span></b></h2>
                            <h3>Клиенту все понравилось?</h3>
                            <div className="small-text">
                                <br/>Довольные клиенты смогут оставлять отзывы в личной карточке компании – их увидят
                                тысячи
                                людей!
                            </div>
                            <button className="blue-button">Попробовать бесплатно</button>
                        </div>
                    </div>
                    <div className="block-with-pic-two">
                        <img
                            src="/images/main/mainCard52Img.png"
                            className="block-two-pic-mobile"
                            alt="mobile"
                        />
                        <div className="block-with-pic-two-text">
                            <h2><b>Негативные отзывы - <span className="gradient-text">в службу поддержки</span></b>
                            </h2>
                            <h3>Клиент недоволен?</h3>
                            <div>
                                <ul>
                                    <li>Устраняйте конфликтные ситуации в чате службы поддержки в Telegram.</li>
                                    <li>Вовремя разрешённый конфликт – отсутствие негативных отзывов в сети.</li>
                                </ul>
                            </div>
                            <button className="blue-button">Попробовать бесплатно</button>
                        </div>
                        <img
                            src="/images/main/mainCard52Img.png"
                            className="block-two-pic"
                            alt="mobile"
                        />
                    </div>
                </div>
                <div className="recommendations">
                    <h1><b><span className="gradient-text">Как ликвидировать</span> негативные отзывы?</b></h1>
                    <h2>Один негативный отзыв - это 100 положительных, и если вы хотите его убрать, то лучше ответить на
                        него в момент возникновения</h2>
                    <ListOfRec/>
                </div>
                <div id='tariffs'>
                    <img
                        src="/images/main/purple_spire.png"
                        alt="Blue Spire"
                        className="blue-spire"
                    />
                    <span className="header-tariffs">
                    <h1><b>Выбирайте то, что удобно Вам для управления репутацией</b></h1>
                </span>
                    <Prices/>
                </div>

                <div id="contacts">
                    <div className="text-contacts">
                        <h1><b>Запишитесь на <span className="gradient-text">бесплатный звонок</span></b></h1>
                        <p>Наш менеджер перезвонит вам через 10 минут, в течение которых вы сможете:</p>
                        <ul>
                            <li><span>Узнать все отзывы о своей компании и как их отработать.</span></li>
                            <li>
                                <span>Получить список интернет-ресурсов, на которых нужно зарегистрировать компанию.</span>
                            </li>
                            <li>
                                <span>Проанализировать общий рейтинг компании и каждой точки продаж в отдельности.</span>
                            </li>
                            <li>
                                <span>Узнать откуда берутся негативные отзывы и как удалить негативный отзыв без бюджета.</span>
                            </li>
                        </ul>
                        <span className="text-contacts-computer"><p><b>RecTop - Ваша репутация!</b></p></span>
                    </div>
                    <div className="text-contacts-mobile"><b>Подарим доступ к сервису “Электронная книга отзывов и
                        предложений” навсегда!</b></div>
                    <FormUser/>
                </div>
                <Refprogram/>
                <div id="questions">
                    <h1><b>Часто задаваемые вопросы</b></h1>
                    <div className="block-with-accordion">
                        {
                            dataForAccordion.map(({title, text}) => (
                                    <Accordion title={title} text={text} key={title}/>
                                )
                            )
                        }
                    </div>
                </div>
            </Container>
            <Footer/>
        </div>
    )

}


export default HomeScreen

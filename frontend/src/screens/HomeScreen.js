import React, {useEffect} from 'react';

import "../css/main.css";
import "../css/buttons.css";

import Prices from "../components/Prices";
import FormUser from "../components/FormUser";
import Refprogram from "../components/Refprogram";
import Questions from "../components/Questions";
import PurpleCircle from "../components/PurpleCircle";
import Brands from "../components/Brands";
import ListOfRec from "../components/ListOfRec"

const HomeScreen = () => {
    return (
        <div id="body">
            <div className="fblock">
                <div className="fblocktext">
                    <h2> Негативные отзывы теперь в прошлом!</h2>
                    <h1><b> <span>RecTOP</span> - инновационный сервис</b> <i>взаимодействия с клиентами.</i></h1>
                    <br/><br/>
                    <div className="fsmtext">
                        Отзывы собираются по QR-коду, когда клиент посещает заведение или сайт.
                    </div>
                    <button className="fullb">7 дней бесплатно</button>
                    <button className="whiteb">Запросить демо</button>
                </div>
                <img
                    src="/images/main/mainCard1Img.png"
                    className="fimage"
                />
                <img
                    src="/images/main/mainCard1ImgMobile.png"
                    className="fimagemobile"
                />
            </div>
            {/*
   <img
      src='/images/main/afterMainCard1Img.png'
      width="425px"
      className="blueball"
    />
    */}
            <div id="about">
                <div className="aboutcomptext">
                    <h1><b>О компании <span>Rectop</span></b></h1>

                    <h2>Качественно повышаем вашу репутацию</h2>
                    <div className="fsmtext">
                        <b>RecTop</b> - это бизнес- решение для тех, кто хочет получать дополнительный трафик за счёт
                        сбора и мониторинга отзывов.<br/><br/>
                        <ul>
                            <li>Обратная связь с недовольными клиентами позволит разрешить конфликтную ситуацию вовремя
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
            <div id="whyrectop">
                <h1><b>Почему RecTop</b></h1>
                <div className="whyblocks">
                    <div className="whyblock">
                        <img src="/images/pic1.png"/>
                        <h2><b>Увеличим</b></h2>
                        <p><br/> положительные отзывы реальных клиентов на 50%</p>
                    </div>
                    <div className="whyblock">
                        <img src="/images/pic2.png"/>
                        <h2><b>Освободим</b></h2>
                        <p><br/> 90% вашего времени на сбор клиентских отзывов</p>
                    </div>
                    <div className="whyblock">
                        <img src="/images/pic3.png"/>
                        <h2><b>Мотивируем</b></h2>
                        <p><br/> клиентов на повторные продажи: кэшбэк за отзывы</p>
                    </div>
                    <div className="whyblock">
                        <img src="/images/pic4.png"/>
                        <h2><b>Регулируем</b></h2>
                        <p><br/> конфликт вовремя, негативные отзывы получаете только Вы</p>
                    </div>
                </div>
            </div>
            <div className="getreports">
                <h1>
                    <b>Получайте <span>положительные</span> отзывы</b>
                </h1>
                <p>
                    Наша команда ежедневно просматривает и анализирует крупнейшие популярные сервисы по сбору отзывов
                </p>
                <h2>Больше положительных отзывов = Больше доверия = Больше продаж</h2>

                <Brands/>

                <div className="purpleblock">
                    <div className="textinpb">
                        <h2><b>Сбор отзывов по QR-коду при посещении вашего заведения онлайн/оффлайн</b></h2>
                        <p>
                            Уникальная система мотивации оставления отзывов от клиентов. Клиент получает кэшбек за отзыв
                            на любом сервисе - его можно обменять на скидку/услугу у партнеров.
                        </p>
                    </div>
                    {/*
        <img
            src="/images/mobileforpurpleblock.png"
            className="purpbtimg"
            />
            */}
                    <img
                        src="/images/mobileforpurpleblockt.png"
                        className="purpbsimg"/>
                </div>

            </div>

            <div id="work">
                <h1><b>Как мы <span>работаем?</span></b></h1>
                <h2>Сервис “Генератор отзывов”</h2>
                <div className="fsmtext">
                    Уникальный генератор отзывов о компании. Эффективно и просто: клиент сканирует QR-код, оставляет
                    отзыв, вы получаете уведомления в Telegram.
                </div>
                <div className="blockwithpicone">
                    <img
                        src="/images/main/mainCard51Img.png"
                    />
                    <div className="blockwithpiconetext">
                        <h1><b>Акцент на <span>положительных отзывах</span></b></h1>
                        <h2>Клиенту все понравилось?</h2>
                        <div>
                            <br/>Довольные клиенты смогут оставлять отзывы в личной карточке компании – их увидят тысячи
                            людей!
                        </div>
                        <button className="fullb">Попробовать бесплатно</button>
                    </div>
                </div>
                <div className="blockwithpictwo">
                    <div className="blockwithpictwotext">
                        <h1><b>Негативные отзывы - <span>в службу поддержки</span></b></h1>
                        <h2>Клиент недоволен?</h2>
                        <div>
                            <ul>
                                <li>Устраняйте конфликтные ситуации в чате службы поддержки в Telegram.</li>
                                <li>Вовремя разрешённый конфликт – отсутствие негативных отзывов в сети.</li>
                            </ul>
                        </div>
                        <button className="fullb">Попробовать бесплатно</button>
                    </div>
                    <img
                        src="/images/main/mainCard52Img.png"
                    />
                </div>
            </div>
            <div className="recomendations">
                <h1><b><span>Как ликвидировать</span> негативные отзывы?</b></h1>
                <h2>Один негативный отзыв - это 100 положительных, и если вы хотите его убрать, то лучше ответить на
                    него в момент возникновения</h2>
                <ListOfRec/>
            </div>
            <div id='tariffs'>
                <h1><b>Выбирайте то, что удобно Вам для управления репутацией</b></h1>
                <div className="forButtons">
                    <button className="bforp">На неделю</button>
                    <button className="bforp">На месяц</button>
                    <button className="bforp">На 1 год</button>
                </div>
                <Prices/>
            </div>

            <div id="contacts">
                <div className="textcontacts">
                    <h1><b>Запишитесь на <span>бесплатный звонок</span></b></h1>
                    <p>Наш менеджер перезвонит вам через 10 минут, в течение которых вы сможете:</p>
                    <ul>
                        <li>Узнать все отзывы о своей компании и как их отработать.</li>
                        <li>Получить список интернет-ресурсов, на которых нужно зарегистрировать компанию.</li>
                        <li> Проанализировать общий рейтинг компании и каждой точки продаж в отдельности.</li>
                        <li>Узнать откуда берутся негативные отзывы и как удалить негативный отзыв без бюджета.</li>
                    </ul>
                    <p>Rectop - Ваша репутация!</p>
                </div>
                <FormUser/>
            </div>
            <Refprogram/>
            <div id="questions">
                <h1><b>Часто задаваемые вопросы</b></h1>
                <Questions/>
            </div>
        </div>
    )

}


export default HomeScreen

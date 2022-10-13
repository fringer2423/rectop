import React, {useEffect} from 'react'

import "../css/main.css"

const HomeScreen = () => {
  return(
   <div className="body">
   <div className="fblock">
     <p> Негативные отзывы теперь в прошлом!</p>
     <h1><b> <span>RecTOP</span> - инновационый сервис</b> <i>взаимодейтсвия с клиентами.</i></h1>
     <br/><br/>
     <div className="fsmtext">
     Отзывы собираются по QR-коду, когда клиент посещает заведение или сайт.
     </div>
     <button className="fullb">7 дней бесплатно</button>
     <button className="whiteb">Запросить демо</button>
   </div>
   <img
      src='/images/main/afterMainCard1Img.png'
      width="425px"
      className="blueball"
    />
    <div className="aboutcomptext">
      <h1>О компании <span>Rectop</span></h1>

        <h2>Качественно повышаем вашу репутацию</h2>
        <div className="fsmtext">
        <b>RecTop</b> - это бизнес- решение для тех, кто хочет получать дополнительный трафик за счёт сбора и мониторинга отзывов.<br/><br/>
        Обратная связь с недовольными клиентами позволит разрешить конфликтную ситуацию вовремя и без последствий. Получайте уведомления о новых отзывах в Telegram, отвечайте из личного кабинета.
        </div>
    </div>
    <div className="whyrectop">
      <h1>Почему RecTop</h1>
      <div className="whyblocks">
        <div className="whyblock">
          <h2>Увеличим</h2>
          <p> <br/> положительные отзывы реальных клиентов на 50%</p>
        </div>
        <div className="whyblock">
          <h2>Освободим</h2>
          <p> <br/> 90% вашего времени на сбор клиентских отзывов</p>
        </div>
        <div className="whyblock">
          <h2>Мотивируем</h2>
          <p> <br/> клиентов на повторные продажи: кэшбэк за отзывы</p>
        </div>
        <div className="whyblock">
          <h2>Регулируем</h2>
          <p> <br/> конфликт вовремя, негативные отзывы получаете только Вы</p>
        </div>
      </div>
    </div>
    <div className="getreports">
      <h1>
        <b>Получайте <span>положительные</span> отзывы</b>
      </h1>
        <div className="fsmtext">
        Наша команда ежедневно просматривает и анализирует крупнейшие популярные сервисы по сбору отзывов
        </div>
      <h2>Больше положительных отзывов = Больше доверия = Больше продаж</h2>
      <div className="purpleblock">
        <h2>Сбор отзывов по QR-коду  при посещении вашего заведения онлайн/оффлайн</h2>
        <div className="fsmtext">
        Уникальная система мотивации оставления отзывов от клиентов. Клиент получает кэшбек за отзыв на любом сервисе - его можно обменять на скидку/услугу у партнеров.
        </div>
      </div>
    </div>

    <div className="work">
      <h1><b>Как мы <span>работаем?</span></b></h1>
      <h2>Сервис “Генератор отзывов”</h2>
      <div className="fsmtext">
      Уникальный генератор отзывов о компании. Эффективно и просто: клиент сканирует QR-код, оставляет отзыв, вы получаете уведомления в Telegram.
      </div>
      <div className="blockwithpic">
        <img
          src="/images/main/mainCard51Img.png"
          width="400px"
          height="400px"
        />
        <h1>Акцент на <span>положительных отзывах</span></h1>
        <h2>Клиенту все понравилось?</h2>
        <div className="fblock">Довольные клиенты смогут оставлять отзывы в личной карточке компании – их увидят тысячи людей!</div>
        <button className="fullb">Попробовать бесплатно</button>
      </div>

    </div>

   </div>
 )

}



export default HomeScreen

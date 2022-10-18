import React from "react";

import Accordion from 'react-bootstrap/Accordion';

import "../css/questions.css"

const Questions = () => {
  return(
    <div className="accord">
    <Accordion>
      <Accordion.Item eventKey="0">
        <Accordion.Header>Какие виды отзывов вы агрегируете?</Accordion.Header>
        <Accordion.Body>
        Обратная связь с недовольными клиентами позволит разрешить конфликтную ситуацию вовремя и без последствий. Получайте уведомления о новых отзывах в Telegram, отвечайте из личного кабинета.
        </Accordion.Body>
      </Accordion.Item>
      <Accordion.Item eventKey="1">
        <Accordion.Header>Чем мне будет полезен сервис Rec.Top?</Accordion.Header>
        <Accordion.Body>
        Обратная связь с недовольными клиентами позволит разрешить конфликтную ситуацию вовремя и без последствий. Получайте уведомления о новых отзывах в Telegram, отвечайте из личного кабинета.
        </Accordion.Body>
      </Accordion.Item>
      <Accordion.Item eventKey="2">
        <Accordion.Header>На чем основана ваша ценовая политика?</Accordion.Header>
        <Accordion.Body>
        Обратная связь с недовольными клиентами позволит разрешить конфликтную ситуацию вовремя и без последствий. Получайте уведомления о новых отзывах в Telegram, отвечайте из личного кабинета.
        </Accordion.Body>
      </Accordion.Item>
      <Accordion.Item eventKey="3">
        <Accordion.Header>НКак часто я буду получать новые отзывы от Rec.Top?</Accordion.Header>
        <Accordion.Body>
        Обратная связь с недовольными клиентами позволит разрешить конфликтную ситуацию вовремя и без последствий. Получайте уведомления о новых отзывах в Telegram, отвечайте из личного кабинета.
        </Accordion.Body>
      </Accordion.Item>
      <Accordion.Item eventKey="4">
        <Accordion.Header>Любой мой сотрудник сможет получать уведомления о новых отзывах?</Accordion.Header>
        <Accordion.Body>
        Обратная связь с недовольными клиентами позволит разрешить конфликтную ситуацию вовремя и без последствий. Получайте уведомления о новых отзывах в Telegram, отвечайте из личного кабинета.
        </Accordion.Body>
      </Accordion.Item>
    </Accordion>
    </div>
  )
}

export default Questions;

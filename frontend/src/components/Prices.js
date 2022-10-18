import React from "react";
import "../css/prices.css"

const Prices = (props) => {
  return(
  <div className="tableforprice">
    <h3><b>{props.header}</b></h3>
    <h5>1 филиал</h5>
    <h4><b>{props.price}</b></h4>
    <div className="blockintable">
      <b>
      Производите сбор отзывов </b> от ваших клиентов при помощи QR-кодов на точках продаж
    </div>
    <p>
      {props.f}
      <hr/>
      {props.s}
      <hr/>
      {props.th}
      <hr/>
      {props.ft}
      <hr/>
      {props.ff}
      <hr/>
      {props.sx}
      <hr/>
      {props.sv}
      <hr/>
      {props.eg}
      <hr/>
    </p>
    <button className="blackbutton">Приобрести тариф</button>
  </div>
 )
}

export default Prices

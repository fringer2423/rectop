import React from "react";
import "../css/formuser.css"

const FormUser = () => {
  return(
    <div className="forform">
      <h3>
        <b>Заполните форму заявки</b>
      </h3>
      <p><br/>Мы перезвоним в течение 10 минут</p>
      <div className="inputsinform">
        <input type="text"  className="inputform"/>
        <input type="text"  className="inputform"/>
        <input type="text"  className="inputform"/>
        <input type="text"  className="inputform"/>
      </div>
      <button>Отправить заявку</button>
    </div>
  )
}


export default FormUser;

import React from "react";
import "../css/formuser.css"

const FormUser = () => {
    return (
        <div className="for-form">
            <h3>
                <b>Заполните форму заявки</b>
            </h3>
            <p><br/>Мы перезвоним в течение 10 минут</p>
            <div className="inputs-in-form">
                <input type="text" className="input-form" placeholder="Ваше имя"/>
                <input type="text" className="input-form" placeholder="Ваш телефон"/>
                <input type="text" className="input-form" placeholder="Ваш e-mail"/>
                <input type="text" className="input-form" placeholder="Название вашей компании"/>
            </div>
            <button className="white-button">Отправить заявку</button>
        </div>
    )
}


export default FormUser;

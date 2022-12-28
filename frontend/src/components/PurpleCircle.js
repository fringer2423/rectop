import React from "react";

import "../css/purpleCircle.css";

const PurpleCircle = () => {
    return (
        <div className="block-for-purple-circle">
            <div className="black-block">
                <img
                    src="/images/user.svg"
                    className="pic-of-user"
                    alt="user"
                />
                <h2>Клиенты</h2>
                <p>Делятся впечатлениями</p>
            </div>
            <img
                src="/images/ellipsePurple.png"
                className="purple-arrow"
                alt="purple circle arrow"
            />
            <div className="purple-circle">
                <h1>
                    <b>RecTop</b>
                </h1>
                <hr />
                <p>Мы сводим клиентов и компании вместе!</p>
            </div>
            <img
                src="/images/ellipseBlack.png"
                className="black-arrow"
                alt="black circle arrow"
            />
            <div className="black-blockt">
                <h2>Бизнес</h2>
                <p>Повышает репутацию</p>
                <img
                    src="/images/computer.svg"
                    className="pic-of-computer"
                    alt="computer"
                />
            </div>
        </div>
    );
};

export default PurpleCircle;

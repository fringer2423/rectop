import React from "react";

import "../css/refProg.css"

const Refprogram = () => {
    return (
        <>
            <img
                src="/images/main/bell_right.svg"
                className="bell-ring"
                alt="bell ring"
            />
            <div className="ref-block">
                <h1><b>Реферальная программа</b></h1>
                <p>Каждый твой новый подключённый филиал/приведённый друг - это пожизненный кешбек</p>
            </div>
            <img
                src="/images/main/megaphone.svg"
                className="megaphone"
                alt="megaphone"
            />
        </>
    )
}

export default Refprogram;

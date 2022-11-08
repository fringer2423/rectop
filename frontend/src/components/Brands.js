import React from "react";

import Carousel from './Carousel.js';

import "../css/brands.css";

const brands = [
    {
        src: "/images/main/image49.png",
        title: "Яндекс.Карты",
        text: "55 млн чел./месяц"
    },
    {
        src: "/images/main/image50.png",
        title: "Google карты",
        text: "30 млн чел./месяц"
    },
    {
        src: "/images/main/image51.png",
        title: "2ГИС",
        text: "30 млн чел./месяц"
    },
    {
        src: "/images/main/image52.png",
        title: "Wildberries",
        text: "92 млн чел./месяц"
    },
    {
        src: "/images/main/image54.png",
        title: "Zoon",
        text: "25 млн чел./месяц"
    },
    {
        src: "/images/main/image55.png",
        title: "OZON",
        text: "80 млн чел./месяц"
    },
    {
        src: "/images/main/image56.png",
        title: "Yell",
        text: "3 млн чел./месяц"
    },
    {
        src: "/images/main/image57.png",
        title: "Flamp",
        text: "50 млн чел./месяц"
    }
]

const Brands = () => {
    return (
        <>
            <div id="tab-for-icons">
            {brands.map(brand => {
                return(
                    <div className="brand-icon" key={brand.title}>
                        <div className="icon-in-circle">
                            <img
                                src={brand.src}
                                alt={brand.title}
                            />
                        </div>
                        <h5>{brand.title}</h5>
                        <p>{brand.text}</p>
                    </div>
                )
            })}
            </div>
            <div id="slider-for-icons">
                <Carousel>
                    <div className="slide" >
                        <div className="brand-icon">
                            <div className="icon-in-circle">
                                <img
                                    src="/images/main/image49.png"
                                    alt="Yandex"
                                />
                            </div>
                            <h5>Яндекс.Карты</h5>
                            <p>55 млн чел./месяц</p>
                        </div>
                        <div className="brand-icon">
                            <div className="icon-in-circle">
                                <img
                                    src="/images/main/image50.png"
                                    alt="Google"
                                />
                            </div>
                            <h5>Google карты</h5>
                            <p>30 млн чел./месяц</p>
                        </div>
                    </div>
                    <div className="slide">
                        <div className="brand-icon">
                            <div className="icon-in-circle">
                                <img
                                    src="/images/main/image51.png"
                                    alt="2ГИС"
                                />
                            </div>
                            <h5>2ГИС</h5>
                            <p>30 млн чел./месяц</p>
                        </div>
                        <div className="brand-icon">
                            <div className="icon-in-circle">
                                <img
                                    src="/images/main/image52.png"
                                    alt="Wildberries"
                                />
                            </div>
                            <h5>Wildberries</h5>
                            <p>92 млн чел./месяц</p>
                        </div>
                    </div>
                    <div className="slide">
                        <div className="brand-icon">
                            <div className="icon-in-circle">
                                <img
                                    src="/images/main/image54.png"
                                    alt="Zoon"
                                />
                            </div>
                            <h5>Zoon</h5>
                            <p>24 млн чел./месяц</p>
                        </div>
                        <div className="brand-icon">
                            <div className="icon-in-circle">
                                <img
                                    src="/images/main/image55.png"
                                    alt="OZON"
                                />
                            </div>
                            <h5>OZON</h5>
                            <p>80 млн чел./месяц</p>
                        </div>
                    </div>
                    <div className="slide">
                        <div className="brand-icon">
                            <div className="icon-in-circle">
                                <img
                                    src="/images/main/image56.png"
                                    alt="Yell"
                                />
                            </div>
                            <h5>Yell</h5>
                            <p>3 млн чел./месяц</p>
                        </div>
                        <div className="brand-icon">
                            <div className="icon-in-circle">
                                <img src="/images/main/image57.png"
                                        alt="Flamp"
                                />
                            </div>
                            <h5>Flamp</h5>
                            <p>50 млн чел./месяц</p>
                        </div>
                    </div>
                </Carousel>
            </div>
        </>
    )
}

export default Brands;

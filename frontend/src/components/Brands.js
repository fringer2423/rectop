import React from "react";

import { Carousel } from "react-bootstrap";

import "../css/brands.css";

const brands = [
    {
        src: "/images/main/yandex.svg",
        title: "Яндекс.Карты",
        text: "55 млн чел./месяц",
    },
    {
        src: "/images/main/google.svg",
        title: "Google карты",
        text: "30 млн чел./месяц",
    },
    {
        src: "/images/main/2GIS.svg",
        title: "2ГИС",
        text: "30 млн чел./месяц",
    },
    {
        src: "/images/main/wildberries.svg",
        title: "Wildberries",
        text: "92 млн чел./месяц",
    },
    {
        src: "/images/main/zoon.svg",
        title: "Zoon",
        text: "25 млн чел./месяц",
    },
    {
        src: "/images/main/ozon.svg",
        title: "OZON",
        text: "80 млн чел./месяц",
    },
    {
        src: "/images/main/yell.svg",
        title: "Yell",
        text: "3 млн чел./месяц",
    },
    {
        src: "/images/main/flamp.svg",
        title: "Flamp",
        text: "50 млн чел./месяц",
    },
];

const Brands = () => {
    return (
        <>
            <div id="tab-for-icons">
                {brands.map((brand) => {
                    return (
                        <div className="brand-icon" key={brand.title}>
                            <div className="icon-in-circle">
                                <img src={brand.src} alt={brand.title} />
                            </div>
                            <h5>{brand.title}</h5>
                            <p>{brand.text}</p>
                        </div>
                    );
                })}
            </div>
            <div id="slider-for-icons">
                <Carousel className="carousel-for-brands" interval={null}>
                    <Carousel.Item>
                        <div className="slide">
                            <div className="brand-icon">
                                <div className="icon-in-circle">
                                    <img
                                        src="/images/main/yandex.svg"
                                        alt="Yandex"
                                    />
                                </div>
                                <h5>Яндекс.Карты</h5>
                                <p>55 млн чел./месяц</p>
                            </div>
                            <div className="brand-icon">
                                <div className="icon-in-circle">
                                    <img
                                        src="/images/main/google.svg"
                                        alt="Google"
                                    />
                                </div>
                                <h5>Google карты</h5>
                                <p>30 млн чел./месяц</p>
                            </div>
                        </div>
                    </Carousel.Item>
                    <Carousel.Item>
                        <div className="slide">
                            <div className="brand-icon">
                                <div className="icon-in-circle">
                                    <img
                                        src="/images/main/2GIS.svg"
                                        alt="2ГИС"
                                    />
                                </div>
                                <h5>2ГИС</h5>
                                <p>30 млн чел./месяц</p>
                            </div>
                            <div className="brand-icon">
                                <div className="icon-in-circle">
                                    <img
                                        src="/images/main/wildberries.svg"
                                        alt="Wildberries"
                                    />
                                </div>
                                <h5>Wildberries</h5>
                                <p>92 млн чел./месяц</p>
                            </div>
                        </div>
                    </Carousel.Item>
                    <Carousel.Item>
                        <div className="slide">
                            <div className="brand-icon">
                                <div className="icon-in-circle">
                                    <img
                                        src="/images/main/zoon.svg"
                                        alt="Zoon"
                                    />
                                </div>
                                <h5>Zoon</h5>
                                <p>24 млн чел./месяц</p>
                            </div>
                            <div className="brand-icon">
                                <div className="icon-in-circle">
                                    <img
                                        src="/images/main/ozon.svg"
                                        alt="OZON"
                                    />
                                </div>
                                <h5>OZON</h5>
                                <p>80 млн чел./месяц</p>
                            </div>
                        </div>
                    </Carousel.Item>
                    <Carousel.Item>
                        <div className="slide">
                            <div className="brand-icon">
                                <div className="icon-in-circle">
                                    <img
                                        src="/images/main/yell.svg"
                                        alt="Yell"
                                    />
                                </div>
                                <h5>Yell</h5>
                                <p>3 млн чел./месяц</p>
                            </div>
                            <div className="brand-icon">
                                <div className="icon-in-circle">
                                    <img
                                        src="/images/main/flamp.svg"
                                        alt="Flamp"
                                    />
                                </div>
                                <h5>Flamp</h5>
                                <p>50 млн чел./месяц</p>
                            </div>
                        </div>
                    </Carousel.Item>
                </Carousel>
            </div>
        </>
    );
};

export default Brands;

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
                </Carousel>
            </div>
        </>
    )
}

export default Brands;

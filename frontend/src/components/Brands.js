import React from "react";

import Carousel from 'react-bootstrap/Carousel';

import "../css/brands.css";

const Brands = () => {
  return(
    <>
    <div id="tabforicons">
      <div className="brandicon">
        <div className="iconincircle">
          <img src="/images/main/image49.png"/>
        </div>
        <h5>Яндекс.Карты</h5>
        <p>55 млн чел./месяц</p>
      </div>
      <div className="brandicon">
        <div className="iconincircle">
          <img src="/images/main/image50.png"/>
        </div>
        <h5>Google карты</h5>
        <p>30 млн чел./месяц</p>
      </div>
      <div className="brandicon">
        <div className="iconincircle">
          <img src="/images/main/image51.png"/>
        </div>
        <h5>2ГИС</h5>
        <p>30 млн чел./месяц</p>
      </div>
      <div className="brandicon">
        <div className="iconincircle">
          <img src="/images/main/image52.png"/>
        </div>
        <h5>Wildberries</h5>
        <p>92 млн чел./месяц</p>
      </div>
      <div className="brandicon">
        <div className="iconincircle">
          <img src="/images/main/image54.png"/>
        </div>
        <h5>Zoon</h5>
        <p>25 млн чел./месяц</p>
      </div>
      <div className="brandicon">
        <div className="iconincircle">
          <img src="/images/main/image55.png"/>
        </div>
        <h5>OZON</h5>
        <p>80 млн чел./месяц</p>
      </div>
      <div className="brandicon">
        <div className="iconincircle">
          <img src="/images/main/image56.png"/>
        </div>
        <h5>Yell</h5>
        <p>3 млн чел./месяц</p>
      </div>
      <div className="brandicon">
        <div className="iconincircle">
          <img src="/images/main/image57.png"/>
        </div>
        <h5>Flamp</h5>
        <p>50 млн чел./месяц</p>
      </div>
    </div>
    <div id="sliderforicons">
      <Carousel>
        <Carousel.Item>
          <div className="slide">
            <div className="brandicon">
              <div className="iconincircle">
                <img src="/images/main/image49.png"/>
              </div>
              <h5>Яндекс.Карты</h5>
              <p>55 млн чел./месяц</p>
            </div>
            <div className="brandicon">
              <div className="iconincircle">
                <img src="/images/main/image50.png"/>
              </div>
              <h5>Google карты</h5>
              <p>30 млн чел./месяц</p>
            </div>
          </div>
        </Carousel.Item>
        <Carousel.Item>
        <div className="slide">
          <div className="brandicon">
            <div className="iconincircle">
              <img src="/images/main/image51.png"/>
            </div>
            <h5>2ГИС</h5>
            <p>30 млн чел./месяц</p>
          </div>
          <div className="brandicon">
            <div className="iconincircle">
              <img src="/images/main/image52.png"/>
            </div>
            <h5>Wildberries</h5>
            <p>92 млн чел./месяц</p>
          </div>
          </div>
        </Carousel.Item>
        <Carousel.Item>
        <div className="slide">
          <div className="brandicon">
            <div className="iconincircle">
              <img src="/images/main/image54.png"/>
            </div>
            <h5>Zoon</h5>
            <p>24 млн чел./месяц</p>
          </div>
          <div className="brandicon">
            <div className="iconincircle">
              <img src="/images/main/image55.png"/>
            </div>
            <h5>OZON</h5>
            <p>80 млн чел./месяц</p>
          </div>
          </div>
        </Carousel.Item>
        <Carousel.Item>
        <div className="slide">
          <div className="brandicon">
            <div className="iconincircle">
              <img src="/images/main/image54.png"/>
            </div>
            <h5>Yell</h5>
            <p>3 млн чел./месяц</p>
          </div>
          <div className="brandicon">
            <div className="iconincircle">
              <img src="/images/main/image55.png"/>
            </div>
            <h5>Flamp</h5>
            <p>50 млн чел./месяц</p>
          </div>
          </div>
        </Carousel.Item>
      </Carousel>
    </div>
    </>
  )
}

export default Brands;

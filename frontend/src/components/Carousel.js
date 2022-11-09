import React, {useEffect, useState, Children, cloneElement} from 'react';
import '../css/carousel.css';

import {faArrowRightLong} from '@fortawesome/free-solid-svg-icons';
import {faArrowLeftLong} from '@fortawesome/free-solid-svg-icons';

import {FontAwesomeIcon} from '@fortawesome/react-fontawesome';


const PAGE_WIDTH = 300

const Carousel = ({children}) => {
    const [pages, setPages] = useState([]);
    const [offset, setOffset] = useState(0);


    const handleLeftArrowClick = () => {
        setOffset((currentOffset) => {
            const newOffset = currentOffset + PAGE_WIDTH;
            console.log(newOffset);

            return Math.min(newOffset, 500);
        })
    }
    const handleRightArrowClick = () => {
        setOffset((currentOffset) => {
            const newOffset = currentOffset - PAGE_WIDTH;

            const maxOffset = -(500 + (children.length));


            console.log(newOffset, maxOffset);
            return Math.max(newOffset, maxOffset);
        })
    }

    useEffect(() => {
        setPages(
            Children.map(children, (child) => {
                return cloneElement(child, {
                    style: {
                        minWidth: `300px`,
                        maxWidth: `300px`,
                        height: `${child.scrollHeight}`,
                    },
                })
            })
        )
    }, [])


    return (
        <div
            className="carousel-container"
            style={{
                height: '100%',
                width: '300px',
            }}
        >
            <div className="slider-carousel">
                <div
                    className="slide"
                    style={{
                        transform: `translateX(${offset}px)`,
                    }}
                >
                    {pages}
                </div>
            </div>
            <div className="arrows-in-carousel">
                <div>
                    <FontAwesomeIcon
                        icon={faArrowLeftLong} className="arrow-carousel" onClick={handleLeftArrowClick}/>
                </div>
                <div className="number-of-slides">
                    {
                        pages.map(page => {
                            return (
                                <div className='circle-of-page'>
                                </div>
                            )
                        })
                    }
                </div>
                <div>
                    <FontAwesomeIcon
                        icon={faArrowRightLong} className="arrow-carousel" onClick={handleRightArrowClick}/>
                </div>
            </div>
        </div>
    )
}

export default Carousel;

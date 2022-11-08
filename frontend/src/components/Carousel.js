import React, { useEffect, useState, Children, cloneElement } from 'react';
import '../css/carousel.css';


const PAGE_WIDTH = 233

const Carousel = ({ children }) => {
  const [pages, setPages] = useState([])
  const [offset, setOffset] = useState(0)

  const handleLeftArrowClick = () => {
    setOffset((currentOffset) => {
      const newOffset = currentOffset + PAGE_WIDTH
      console.log(newOffset)
      return Math.min(newOffset, 0)
    })
  }
  const handleRightArrowClick = () => {
    setOffset((currentOffset) => {
      const newOffset = currentOffset - PAGE_WIDTH

      const maxOffset = -(PAGE_WIDTH * (pages.length - 1))

      console.log(newOffset, maxOffset)
      return Math.max(newOffset, maxOffset)
    })
  }

  useEffect(() => {
    setPages(
      Children.map(children, (child) => {
        return cloneElement(child, {
          style: {
            minWidth: `${child.scrollWidth}px`,
            maxWidth: `${child.scrollWidth}px`,
            height: `${child.scrollHeight}px`,
          },
        })
      })
    )
  }, [children])

  return (
    <div className="carousel-container">
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
      <div className="arrow" onClick={handleLeftArrowClick}>-</div>
      <div className="arrow" onClick={handleRightArrowClick}>- </div>
    </div>
  )
}

export default Carousel;

import React, {useState, useRef} from "react";

import "../css/accordion.css"


const Accordion = (props) => {
    const [show, setShow] = useState(false);
    const [height, setHeight] = useState("0px");
    const content = useRef(null);

    const openAccordion = () => {
        setHeight(show === true ? "0px" : `${content.current.scrollHeight}px`);
        setShow(!show);
    }

    return (
        <div className="accordions">
            <div className="accordion-item">
                <div className="title-of-accordion" onClick={openAccordion}>
                    <div>
                        {props.title}
                    </div>
                    <span className="symbol-for-accordion">
                        {show ? "-" : "+"}
                    </span>
                </div>

                <div
                    className="body-of-accordion"
                    ref={content}
                    style={{maxHeight: `${height}`}}
                >
                    <div>
                        {props.text}
                    </div>
                </div>
            </div>
        </div>
    )
}

export default Accordion;

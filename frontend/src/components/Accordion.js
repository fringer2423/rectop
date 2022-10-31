import React, {useState} from "react";

import "../css/accordion.css"


const Accordion = ({title, text}) => {
    const [show, setShow] = useState(false);

    return (
        <div className="accordions">
            <div className="accordion-item">
                <div className="title-of-accordion" onClick={() => setShow(!show)}>
                    <div>
                        {title}
                    </div>
                    <span className="symbol-for-accordion">
                        {show ? "-" : "+"}
                    </span>
                </div>
                {
                    show &&
                    <div className="body-of-accordion">
                        {text}
                    </div>
                }
            </div>
        </div>
    )
}

export default Accordion;

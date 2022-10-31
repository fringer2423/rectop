import React from "react";

import "../css/listofrec.css";

const ListOfRec = () => {
    return (
        <div id="block-of-recs">
            <div className="block-of-rec">
                <div className="rec">
                    <h3><b>01</b></h3>
                    <p><b>Обратитесь по имени </b> и поблагодарите за оставленный отзыв.</p>
                </div>
                <img src="/images/main/mainCard61Img.png" className="arrow"/>
                <img src="/images/main/mainCard61ImgMobile.png" className="arrow-for-mobile"/>
            </div>
            <div className="block-of-rec">
                <img src="/images/main/mainCard62Img.png" className="arrow"/>
                <img src="/images/main/mainCard62ImgMobile.png" className="arrow-for-mobile"/>
                <div className="rec">
                    <h3><b>02</b></h3>
                    <p><b>Извинитесь</b>, даже если вашей вины нет. Всегда будьте доброжелательны!</p>
                </div>
            </div>
            <div className="block-of-rec">
                <div className="rec">
                    <h3><b>03</b></h3>
                    <p><b>Сообщите</b> о вашей готовности помочь в сложившейся ситуации.</p>
                </div>
                <img src="/images/main/mainCard61Img.png" className="arrow"/>
                <img src="/images/main/mainCard61ImgMobile.png" className="arrow-for-mobile"/>
            </div>
            <div className="block-of-rec">
                <div className="rec">
                    <div className="rec-last">
                        <h3><b>04</b></h3>
                        <p><b>Попросите клиента выслать </b> контактные данные на ваш электронный адрес.</p>
                    </div>
                </div>
            </div>
        </div>
    )
}

export default ListOfRec

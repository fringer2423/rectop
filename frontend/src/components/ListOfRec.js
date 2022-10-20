import React from "react";

import "../css/listofrec.css";

const ListOfRec = () => {
  return(
    <div id="blockofrecs">
      <div className="blockofrec">
        <div className="rec">
          <h3><b>01</b></h3>
          <p><b>Обратитесь по имени </b> и поблагодарите за оставленный отзыв.</p>
        </div>
        <img src="/images/main/mainCard61Img.png"/>
      </div>
      <div className="blockofrec">
        <img src="/images/main/mainCard62Img.png"/>
        <div className="rec">
          <h3><b>02</b></h3>
          <p><b>Извинитесь</b>, даже если вашей вины нет. Всегда будьте доброжелательны!</p>
        </div>
      </div>
      <div className="blockofrec">
        <div className="rec">
          <h3><b>03</b></h3>
          <p><b>Сообщите</b> о вашей готовности помочь в сложившейся ситуации.</p>
        </div>
        <img src="/images/main/mainCard61Img.png"/>
      </div>
      <div className="blockofrec">
        <div className="rec">
          <div className="forthrec">
            <h3><b>04</b></h3>
            <p><b>Попросите клиента выслать </b> контактные данные на ваш электронный адрес.</p>
          </div>
        </div>
      </div>
    </div>
  )
}

export default ListOfRec

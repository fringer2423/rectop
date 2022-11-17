export const countPrices = (branchs, duration) => {
    let resultPrice = 0;
    let oldPrice = 0;
    if (branchs < 10){
        return {oldPrice: duration, resultPrice: duration, sale: '0%'};
    }
    if (branchs >= 10 && branchs < 15) {
        // скидка 5%
        oldPrice = duration * branchs
        resultPrice = Math.floor(((duration * branchs) / 100) * 95);
        return {oldPrice: oldPrice, resultPrice: resultPrice, sale: '5%'};
    }
    if (branchs >= 15 && branchs < 25) {
        // скидка 10%
        oldPrice = duration * branchs
        resultPrice = Math.floor(((duration * branchs) / 100) * 90);
        return {oldPrice: oldPrice, resultPrice: resultPrice, sale: '10%'};
    }
    if (branchs >= 25 && branchs < 35) {
        // скидка 15%
        oldPrice = duration * branchs
        resultPrice = Math.floor(((duration * branchs) / 100) * 85);
        return {oldPrice: oldPrice, resultPrice: resultPrice, sale: '15%'};
    }
    if (branchs >= 35 && branchs < 45) {
        // скидка 20%
        oldPrice = duration * branchs
        resultPrice = Math.floor(((duration * branchs) / 100) * 80);
        return {oldPrice: oldPrice, resultPrice: resultPrice, sale: '20%'};
    }
    if (branchs >= 45 && branchs < 55) {
        // скидка 25%
        oldPrice = duration * branchs
        resultPrice = Math.floor(((duration * branchs) / 100) * 75);
        return {oldPrice: oldPrice, resultPrice: resultPrice, sale: '25%'};
    }
    if (branchs >= 55 && branchs < 65) {
        // скидка 30%
        oldPrice = duration * branchs
        resultPrice = Math.floor(((duration * branchs) / 100) * 70);
        return {oldPrice: oldPrice, resultPrice: resultPrice, sale: '30%'};
    }
    if (branchs >= 65 && branchs < 75) {
        // скидка 35%
        oldPrice = duration * branchs
        resultPrice = Math.floor(((duration * branchs) / 100) * 65);
        return {oldPrice: oldPrice, resultPrice: resultPrice, sale: '35%'};
    }
    if (branchs >= 75 && branchs < 85) {
        // скидка 40%
        oldPrice = duration * branchs
        resultPrice = Math.floor(((duration * branchs) / 100) * 60);
        return {oldPrice: oldPrice, resultPrice: resultPrice, sale: '40%'};
    }
    if (branchs >= 85 && branchs < 95) {
        // скидка 45%
        oldPrice = duration * branchs
        resultPrice = Math.floor(((duration * branchs) / 100) * 55);
        return {oldPrice: oldPrice, resultPrice: resultPrice, sale: '45%'};
    }
    if (branchs >= 95 && branchs < 105) {
        // скидка 50%
        oldPrice = duration * branchs
        resultPrice = Math.floor(((duration * branchs) / 100) * 50);
        return {oldPrice: oldPrice, resultPrice: resultPrice, sale: '50%'};
    }
    if (branchs >= 105 && branchs < 115) {
        // скидка 55%
        oldPrice = duration * branchs
        resultPrice = Math.floor(((duration * branchs) / 100) * 45);
        return {oldPrice: oldPrice, resultPrice: resultPrice, sale: '55%'};
    }
    if (branchs >= 115 && branchs < 125) {
        // скидка 60%
        oldPrice = duration * branchs
        resultPrice = Math.floor(((duration * branchs) / 100) * 40);
        return {oldPrice: oldPrice, resultPrice: resultPrice, sale: '60%'};
    }
    if (branchs >= 125 && branchs < 135) {
        // скидка 65%
        oldPrice = duration * branchs
        resultPrice = Math.floor(((duration * branchs) / 100) * 35);
        return {oldPrice: oldPrice, resultPrice: resultPrice, sale: '65%'};
    }
    if (branchs >= 135 && branchs < 145) {
        // скидка 70%
        oldPrice = duration * branchs
        resultPrice = Math.floor(((duration * branchs) / 100) * 30);
        return {oldPrice: oldPrice, resultPrice: resultPrice, sale: '70%'};
    }
    if (branchs >= 145) {
        // скидка 75%
        oldPrice = duration * branchs
        resultPrice = Math.floor(((duration * branchs) / 100) * 25);
        return {oldPrice: oldPrice, resultPrice: resultPrice, sale: '75%'};
    }
}

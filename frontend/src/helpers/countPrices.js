export const countPrices = (numOfFilials, duration) => {
    let resultPrice = 0;
    let oldPrice = 0;
    if (numOfFilials < 10){
        return {oldPrice: duration, resultPrice: duration, sale: '0%'};
    }
    if (numOfFilials >= 10 && numOfFilials < 15) {
        // скидка 5%
        oldPrice = duration * numOfFilials
        resultPrice = Math.floor(((duration * numOfFilials) / 100) * 95);
        return {oldPrice: oldPrice, resultPrice: resultPrice, sale: '5%'};
    }
    if (numOfFilials >= 15 && numOfFilials < 25) {
        // скидка 10%
        oldPrice = duration * numOfFilials
        resultPrice = Math.floor(((duration * numOfFilials) / 100) * 90);
        return {oldPrice: oldPrice, resultPrice: resultPrice, sale: '10%'};
    }
    if (numOfFilials >= 25 && numOfFilials < 35) {
        // скидка 15%
        oldPrice = duration * numOfFilials
        resultPrice = Math.floor(((duration * numOfFilials) / 100) * 85);
        return {oldPrice: oldPrice, resultPrice: resultPrice, sale: '15%'};
    }
    if (numOfFilials >= 35 && numOfFilials < 45) {
        // скидка 20%
        oldPrice = duration * numOfFilials
        resultPrice = Math.floor(((duration * numOfFilials) / 100) * 80);
        return {oldPrice: oldPrice, resultPrice: resultPrice, sale: '20%'};
    }
    if (numOfFilials >= 45 && numOfFilials < 55) {
        // скидка 25%
        oldPrice = duration * numOfFilials
        resultPrice = Math.floor(((duration * numOfFilials) / 100) * 75);
        return {oldPrice: oldPrice, resultPrice: resultPrice, sale: '25%'};
    }
    if (numOfFilials >= 55 && numOfFilials < 65) {
        // скидка 30%
        oldPrice = duration * numOfFilials
        resultPrice = Math.floor(((duration * numOfFilials) / 100) * 70);
        return {oldPrice: oldPrice, resultPrice: resultPrice, sale: '30%'};
    }
    if (numOfFilials >= 65 && numOfFilials < 75) {
        // скидка 35%
        oldPrice = duration * numOfFilials
        resultPrice = Math.floor(((duration * numOfFilials) / 100) * 65);
        return {oldPrice: oldPrice, resultPrice: resultPrice, sale: '35%'};
    }
    if (numOfFilials >= 75 && numOfFilials < 85) {
        // скидка 40%
        oldPrice = duration * numOfFilials
        resultPrice = Math.floor(((duration * numOfFilials) / 100) * 60);
        return {oldPrice: oldPrice, resultPrice: resultPrice, sale: '40%'};
    }
    if (numOfFilials >= 85 && numOfFilials < 95) {
        // скидка 45%
        oldPrice = duration * numOfFilials
        resultPrice = Math.floor(((duration * numOfFilials) / 100) * 55);
        return {oldPrice: oldPrice, resultPrice: resultPrice, sale: '45%'};
    }
    if (numOfFilials >= 95 && numOfFilials < 105) {
        // скидка 50%
        oldPrice = duration * numOfFilials
        resultPrice = Math.floor(((duration * numOfFilials) / 100) * 50);
        return {oldPrice: oldPrice, resultPrice: resultPrice, sale: '50%'};
    }
    if (numOfFilials >= 105 && numOfFilials < 115) {
        // скидка 55%
        oldPrice = duration * numOfFilials
        resultPrice = Math.floor(((duration * numOfFilials) / 100) * 45);
        return {oldPrice: oldPrice, resultPrice: resultPrice, sale: '55%'};
    }
    if (numOfFilials >= 115 && numOfFilials < 125) {
        // скидка 60%
        oldPrice = duration * numOfFilials
        resultPrice = Math.floor(((duration * numOfFilials) / 100) * 40);
        return {oldPrice: oldPrice, resultPrice: resultPrice, sale: '60%'};
    }
    if (numOfFilials >= 125 && numOfFilials < 135) {
        // скидка 65%
        oldPrice = duration * numOfFilials
        resultPrice = Math.floor(((duration * numOfFilials) / 100) * 35);
        return {oldPrice: oldPrice, resultPrice: resultPrice, sale: '65%'};
    }
    if (numOfFilials >= 135 && numOfFilials < 145) {
        // скидка 70%
        oldPrice = duration * numOfFilials
        resultPrice = Math.floor(((duration * numOfFilials) / 100) * 30);
        return {oldPrice: oldPrice, resultPrice: resultPrice, sale: '70%'};
    }
    if (numOfFilials >= 145) {
        // скидка 75%
        oldPrice = duration * numOfFilials
        resultPrice = Math.floor(((duration * numOfFilials) / 100) * 25);
        return {oldPrice: oldPrice, resultPrice: resultPrice, sale: '75%'};
    }
}

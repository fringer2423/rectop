export const countPrices = (numOfBranchs, duration) => {
    let resultPrice = 0;
    let oldPrice = 0;
    if (numOfBranchs < 10) {
        return {oldPrice: duration, resultPrice: duration, sale: '0%'};
    }
    if (numOfBranchs >= 10 && numOfBranchs < 15) {
        // скидка 5%
        oldPrice = duration * numOfBranchs
        resultPrice = Math.floor(((duration * numOfBranchs) / 100) * 95);
        return {oldPrice: oldPrice, resultPrice: resultPrice, sale: '5%'};
    }
    if (numOfBranchs >= 15 && numOfBranchs < 25) {
        // скидка 10%
        oldPrice = duration * numOfBranchs
        resultPrice = Math.floor(((duration * numOfBranchs) / 100) * 90);
        return {oldPrice: oldPrice, resultPrice: resultPrice, sale: '10%'};
    }
    if (numOfBranchs >= 25 && numOfBranchs < 35) {
        // скидка 15%
        oldPrice = duration * numOfBranchs
        resultPrice = Math.floor(((duration * numOfBranchs) / 100) * 85);
        return {oldPrice: oldPrice, resultPrice: resultPrice, sale: '15%'};
    }
    if (numOfBranchs >= 35 && numOfBranchs < 45) {
        // скидка 20%
        oldPrice = duration * numOfBranchs
        resultPrice = Math.floor(((duration * numOfBranchs) / 100) * 80);
        return {oldPrice: oldPrice, resultPrice: resultPrice, sale: '20%'};
    }
    if (numOfBranchs >= 45 && numOfBranchs < 55) {
        // скидка 25%
        oldPrice = duration * numOfBranchs
        resultPrice = Math.floor(((duration * numOfBranchs) / 100) * 75);
        return {oldPrice: oldPrice, resultPrice: resultPrice, sale: '25%'};
    }
    if (numOfBranchs >= 55 && numOfBranchs < 65) {
        // скидка 30%
        oldPrice = duration * numOfBranchs
        resultPrice = Math.floor(((duration * numOfBranchs) / 100) * 70);
        return {oldPrice: oldPrice, resultPrice: resultPrice, sale: '30%'};
    }
    if (numOfBranchs >= 65 && numOfBranchs < 75) {
        // скидка 35%
        oldPrice = duration * numOfBranchs
        resultPrice = Math.floor(((duration * numOfBranchs) / 100) * 65);
        return {oldPrice: oldPrice, resultPrice: resultPrice, sale: '35%'};
    }
    if (numOfBranchs >= 75 && numOfBranchs < 85) {
        // скидка 40%
        oldPrice = duration * numOfBranchs
        resultPrice = Math.floor(((duration * numOfBranchs) / 100) * 60);
        return {oldPrice: oldPrice, resultPrice: resultPrice, sale: '40%'};
    }
    if (numOfBranchs >= 85 && numOfBranchs < 95) {
        // скидка 45%
        oldPrice = duration * numOfBranchs
        resultPrice = Math.floor(((duration * numOfBranchs) / 100) * 55);
        return {oldPrice: oldPrice, resultPrice: resultPrice, sale: '45%'};
    }
    if (numOfBranchs >= 95 && numOfBranchs < 105) {
        // скидка 50%
        oldPrice = duration * numOfBranchs
        resultPrice = Math.floor(((duration * numOfBranchs) / 100) * 50);
        return {oldPrice: oldPrice, resultPrice: resultPrice, sale: '50%'};
    }
    if (numOfBranchs >= 105 && numOfBranchs < 115) {
        // скидка 55%
        oldPrice = duration * numOfBranchs
        resultPrice = Math.floor(((duration * numOfBranchs) / 100) * 45);
        return {oldPrice: oldPrice, resultPrice: resultPrice, sale: '55%'};
    }
    if (numOfBranchs >= 115 && numOfBranchs < 125) {
        // скидка 60%
        oldPrice = duration * numOfBranchs
        resultPrice = Math.floor(((duration * numOfBranchs) / 100) * 40);
        return {oldPrice: oldPrice, resultPrice: resultPrice, sale: '60%'};
    }
    if (numOfBranchs >= 125 && numOfBranchs < 135) {
        // скидка 65%
        oldPrice = duration * numOfBranchs
        resultPrice = Math.floor(((duration * numOfBranchs) / 100) * 35);
        return {oldPrice: oldPrice, resultPrice: resultPrice, sale: '65%'};
    }
    if (numOfBranchs >= 135 && numOfBranchs < 145) {
        // скидка 70%
        oldPrice = duration * numOfBranchs
        resultPrice = Math.floor(((duration * numOfBranchs) / 100) * 30);
        return {oldPrice: oldPrice, resultPrice: resultPrice, sale: '70%'};
    }
    if (numOfBranchs >= 145) {
        // скидка 75%
        oldPrice = duration * numOfBranchs
        resultPrice = Math.floor(((duration * numOfBranchs) / 100) * 25);
        return {oldPrice: oldPrice, resultPrice: resultPrice, sale: '75%'};
    }
}

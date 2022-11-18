const countPrice = (numOfBranchs, duration, sale) => {
    const oldPrice = duration * numOfBranchs;
    const tempPrice = Math.floor((oldPrice / 100) * sale);
    const resultPrice = oldPrice - tempPrice;
    return {oldPrice: oldPrice, resultPrice: resultPrice, sale: sale}
}

export const countPrices = (numOfBranchs, duration) => {
    let resultPrice = 0;
    let oldPrice = 0;
    switch(true) {
        case (numOfBranchs < 10):
            return {oldPrice: duration, resultPrice: duration, sale: 0};
            break;
        case (numOfBranchs >= 10 && numOfBranchs < 15):
            // скидка 5%
            return countPrice(numOfBranchs, duration, 5);
            break;
        case (numOfBranchs >= 15 && numOfBranchs < 25):
            // скидка 10%
            return countPrice(numOfBranchs, duration, 10);
            break;
        case (numOfBranchs >= 25 && numOfBranchs < 35):
            // скидка 15%
            return countPrice(numOfBranchs, duration, 15);
            break;
        case (numOfBranchs >= 35 && numOfBranchs < 45):
            // скидка 20%
            return countPrice(numOfBranchs, duration, 20);
            break;
        case (numOfBranchs >= 45 && numOfBranchs < 55):
            // скидка 25%
            return countPrice(numOfBranchs, duration, 25);
            break;
        case (numOfBranchs >= 55 && numOfBranchs < 65):
            // скидка 30%
            return countPrice(numOfBranchs, duration, 30);
            break;
        case (numOfBranchs >= 65 && numOfBranchs < 75):
            // скидка 35%
            return countPrice(numOfBranchs, duration, 35);
            break;
        case (numOfBranchs >= 75 && numOfBranchs < 85):
            // скидка 40%
            return countPrice(numOfBranchs, duration, 40);
            break;
        case (numOfBranchs >= 85 && numOfBranchs < 95):
            // скидка 45%
            return countPrice(numOfBranchs, duration, 45);
            break;
        case (numOfBranchs >= 95 && numOfBranchs < 105):
            // скидка 50%
            return countPrice(numOfBranchs, duration, 50);
            break;
        case (numOfBranchs >= 105 && numOfBranchs < 115):
            // скидка 55%
            return countPrice(numOfBranchs, duration, 55);
            break;
        case (numOfBranchs >= 115 && numOfBranchs < 125):
            // скидка 60%
            return countPrice(numOfBranchs, duration, 60);
            break;
        case (numOfBranchs >= 125 && numOfBranchs < 135):
            // скидка 65%
            return countPrice(numOfBranchs, duration, 65);
            break;
        case (numOfBranchs >= 135 && numOfBranchs < 145):
            // скидка 70%
            return countPrice(numOfBranchs, duration, 70);
            break;
        case (numOfBranchs >= 145):
            // скидка 75%
            return countPrice(numOfBranchs, duration, 75);
            break;
        }
}

export const countWeekDefaultPrice = (priceMonth) => {
    return Math.floor(priceMonth / 4)
}

export const countYearDefaultPrice = (priceMonth) => {
    return priceMonth * 12
}

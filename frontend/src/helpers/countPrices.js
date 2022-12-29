const countPrice = (numOfBranchs, duration, sale) => {
    const oldPrice = duration * numOfBranchs;
    const tempPrice = Math.floor((oldPrice / 100) * sale);
    const resultPrice = oldPrice - tempPrice;
    return {
        oldPrice: oldPrice,
        resultPrice: resultPrice,
        sale: sale,
    };
};

export const countPrices = (numOfBranchs, duration, sales) => {
    const saleBranchs = Object.keys(sales); // массив с ключами объекта
    const percentSales = Object.values(sales); // массив со значениями объекта
    if (numOfBranchs < Number(saleBranchs[0])) {
        // если количество филиалов меньше первой скидки
        return {
            oldPrice: duration,
            resultPrice: duration,
            sale: 0,
        };
    } else {
        for (let i = 0; i < saleBranchs.length; i++) {
            if (i < saleBranchs.length - 1) {
                // если это не последний элемент массива
                if (
                    numOfBranchs >= Number(saleBranchs[i]) &&
                    numOfBranchs < Number(saleBranchs[i + 1])
                ) {
                    // проверяем что количество филиалов входит в скидку
                    return countPrice(numOfBranchs, duration, percentSales[i]);
                }
            } else {
                if (numOfBranchs >= Number(saleBranchs[i])) {
                    return countPrice(numOfBranchs, duration, percentSales[i]);
                }
            }
        }
    }
};

export const countWeekDefaultPrice = (priceMonth, weekRatio) => {
    return Math.floor(priceMonth * weekRatio);
};

export const countYearDefaultPrice = (priceMonth, yearRatio) => {
    return Math.floor(priceMonth * yearRatio);
};

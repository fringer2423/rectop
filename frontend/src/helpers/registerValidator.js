import {checkMail} from "../validators/validation.js"


export const validateEmail = (email) => {
    if (checkMail.test(email)) {
        return true;
    } else {
        return false;
    }
}

export const validatePassword = (password, passwordRepeat) => {
    if (password === passwordRepeat) {
        return true;
    } else {
        return false;
    }
}

import {checkMail} from "../validators/validation.js"


export const validateEmail = (email) => {
    return checkMail.test(email);
}

export const validatePassword = (password, passwordRepeat) => {
    return password === passwordRepeat;
}

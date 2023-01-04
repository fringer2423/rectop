import {
    QR_CREATE_REQUEST,
    QR_CREATE_SUCCESS,
    QR_CREATE_FAIL,
    QR_ALL_REQUEST,
    QR_ALL_SUCCESS,
    QR_ALL_FAIL,
    QR_GET_ONE_REQUEST,
    QR_GET_ONE_SUCCESS,
    QR_GET_ONE_FAIL,
} from "../constants/QRCodeConstants";

export const QRCreateReducer = (state = {}, action) => {
    switch (action.type) {
        case QR_CREATE_REQUEST:
            return {loading: true};

        case QR_CREATE_SUCCESS:
            return {loading: false, code: action.payload};

        case QR_CREATE_FAIL:
            return {loading: false, error: action.payload};

        default:
            return state;
    }
};

export const QRAllReducer = (state = {}, action) => {
    switch (action.type) {
        case QR_ALL_REQUEST:
            return {loading: true};

        case QR_ALL_SUCCESS:
            return {loading: false, codes: action.payload};

        case QR_ALL_FAIL:
            return {loading: false, error: action.payload};

        default:
            return state;
    }
};

export const QRGetOneReducer = (state = {}, action) => {
    switch (action.type) {
        case QR_GET_ONE_REQUEST:
            return {loading: true};

        case QR_GET_ONE_SUCCESS:
            return {loading: false, code: action.payload};

        case QR_GET_ONE_FAIL:
            return {loading: false, error: action.payload};

        default:
            return state;
    }
};

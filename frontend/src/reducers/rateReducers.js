import {
    RATE_ADD_REQUEST,
    RATE_ADD_SUCCESS,
    RATE_ADD_FAIL,
    RATE_READ_REQUEST,
    RATE_READ_SUCCESS,
    RATE_READ_FAIL,
    RATE_CHANGE_REQUEST,
    RATE_CHANGE_SUCCESS,
    RATE_CHANGE_FAIL,
} from "../constants/rateConstants";


export const rateAddReducer = (state = {}, action) => {
    switch (action.type) {
        case RATE_ADD_REQUEST:
            return {loading: true};

        case RATE_ADD_SUCCESS:
            return {loading: false, rate: action.payload};

        case RATE_ADD_FAIL:
            return {loading: false, error: action.payload};

        default:
            return state;
    }
};

export const rateReadReducer = (state = {}, action) => {
    switch (action.type) {
        case RATE_READ_REQUEST:
            return {loading: true};

        case RATE_READ_SUCCESS:
            return {loading: false, rate: action.payload};

        case RATE_READ_FAIL:
            return {loading: false, error: action.payload};

        default:
            return state;
    }
};

export const rateChangeReducer = (state = {}, action) => {
    switch (action.type) {
        case RATE_CHANGE_REQUEST:
            return {loading: true};

        case RATE_CHANGE_SUCCESS:
            return {loading: false, success: true};

        case RATE_CHANGE_FAIL:
            return {loading: false, error: action.payload};

        default:
            return state;
    }
};
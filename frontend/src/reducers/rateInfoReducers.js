import {
    RATE_INFO_DATA_REQUEST,
    RATE_INFO_DATA_SUCCESS,
    RATE_INFO_DATA_FAIL,
}  from '../constants/rateInfoConstants';

export const rateInfoDataReducer = (state = {}, action) => {
    switch (action.type) {
        case RATE_INFO_DATA_REQUEST:
            return {loading: true}

        case RATE_INFO_DATA_SUCCESS:
            console.log(action.payload, " action.payload in reducers");
            return {loading: false, rateInfo: action.payload}

        case RATE_INFO_DATA_FAIL:
            return {loading: false, error: action.payload}

        default:
            return state
    }
}

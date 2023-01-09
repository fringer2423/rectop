import {
    COMPANY_CREATE_REQUEST,
    COMPANY_CREATE_SUCCESS,
    COMPANY_CREATE_FAIL,
    COMPANY_DELETE_REQUEST,
    COMPANY_DELETE_SUCCESS,
    COMPANY_DELETE_FAIL,
    COMPANY_READ_REQUEST,
    COMPANY_READ_SUCCESS,
    COMPANY_READ_FAIL,
    COMPANY_READ_RESET,
    COMPANY_UPDATE_REQUEST,
    COMPANY_UPDATE_SUCCESS,
    COMPANY_UPDATE_FAIL,
    COMPANY_UPDATE_RESET,
} from "../constants/companyConstants";

export const companyCreateReducer = (state = {}, action) => {
    switch (action.type) {
        case COMPANY_CREATE_REQUEST:
            return {loading: true};

        case COMPANY_CREATE_SUCCESS:
            return {loading: false, success: true};

        case COMPANY_CREATE_FAIL:
            return {loading: false, error: action.payload};

        default:
            return state;
    }
};

export const companyDeleteReducer = (state = {}, action) => {
    switch (action.type) {
        case COMPANY_DELETE_REQUEST:
            return {loading: true};

        case COMPANY_DELETE_SUCCESS:
            return {loading: false, success: true};

        case COMPANY_DELETE_FAIL:
            return {loading: false, error: action.payload};

        default:
            return state;
    }
};

export const companyDetailsReducer = (state = {company: {}}, action) => {
    switch (action.type) {
        case COMPANY_READ_REQUEST:
            return {loading: true};

        case COMPANY_READ_SUCCESS:
            return {loading: false, company: action.payload};

        case COMPANY_READ_FAIL:
            return {loading: false, error: action.payload};
        
        case COMPANY_READ_RESET: 
            return {company: {}};

        default:
            return state;
    }
};

export const companyUpdateReducer = (state = {company: {}}, action) => {
    switch (action.type) {
        case COMPANY_UPDATE_REQUEST:
            return {loading: true};

        case COMPANY_UPDATE_SUCCESS:
            return {loading: false, success: true};

        case COMPANY_UPDATE_FAIL:
            return {loading: false, error: action.payload};
        
        case COMPANY_UPDATE_RESET:
            return {company: {}};

        default:
            return state;
    }
};

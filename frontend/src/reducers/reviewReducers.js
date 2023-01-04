import {
    REVIEW_CREATE_REQUEST,
    REVIEW_ALL_FAIL,
    REVIEW_ALL_REQUEST,
    REVIEW_ALL_SUCCESS,
    REVIEW_CREATE_FAIL,
    REVIEW_CREATE_SUCCESS,
    REVIEW_DELETE_FAIL,
    REVIEW_DELETE_REQUEST,
    REVIEW_DELETE_SUCCESS,
    REVIEW_LIST_FAIL,
    REVIEW_LIST_REQUEST,
    REVIEW_LIST_SUCCESS,
    REVIEW_ONE_FAIL,
    REVIEW_ONE_REQUEST,
    REVIEW_ONE_SUCCESS,
    REVIEW_UPDATE_FAIL,
    REVIEW_UPDATE_REQUEST,
    REVIEW_UPDATE_RESET,
    REVIEW_UPDATE_SUCCESS,
} from "../constants/reviewConstants";


export const reviewCreateReducer = (state = {}, action) => {
    switch (action.type) {
        case REVIEW_CREATE_REQUEST:
            return {loading: true};

        case REVIEW_CREATE_SUCCESS:
            return {loading: false, review: action.payload};

        case REVIEW_CREATE_FAIL:
            return {loading: false, error: action.payload};

        default:
            return state;
    }
};

export const reviewDeleteReducer = (state = {}, action) => {
    switch (action.type) {
        case REVIEW_DELETE_REQUEST:
            return {loading: true};

        case REVIEW_DELETE_SUCCESS:
            return {loading: false, success: true};

        case REVIEW_DELETE_FAIL:
            return {loading: false, error: action.payload};

        default:
            return state;
    }
};

export const reviewAllReducer = (state = {}, action) => {
    switch (action.type) {
        case REVIEW_ALL_REQUEST:
            return {loading: true};

        case REVIEW_ALL_SUCCESS:
            return {loading: false, allReviews: action.payload};

        case REVIEW_ALL_FAIL:
            return {loading: false, error: action.payload};

        default:
            return state;
    }
};

export const reviewListReducer = (state = {}, action) => {
    switch (action.type) {
        case REVIEW_LIST_REQUEST:
            return {loading: true};

        case REVIEW_LIST_SUCCESS:
            return {loading: false, reviewsList: action.payload};

        case REVIEW_LIST_FAIL:
            return {loading: false, error: action.payload};

        default:
            return state;
    }
};

export const reviewGetOneReducer = (state = {}, action) => {
    switch (action.type) {
        case REVIEW_ONE_REQUEST:
            return {loading: true};

        case REVIEW_ONE_SUCCESS:
            return {loading: false, review: action.payload};

        case REVIEW_ONE_FAIL:
            return {loading: false, error: action.payload};

        default:
            return state;
    }
};

export const reviewUpdateReducer = (state = {}, action) => {
    switch (action.type) {
        case REVIEW_UPDATE_REQUEST:
            return {loading: true};

        case REVIEW_UPDATE_SUCCESS:
            return {loading: false, success: true};

        case REVIEW_UPDATE_FAIL:
            return {loading: false, error: action.payload};
        
        case REVIEW_UPDATE_RESET:
            return {review: {}};

        default:
            return state;
    }
};
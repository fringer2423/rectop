import axios from "axios";

import {
    REVIEW_ALL_FAIL,
    REVIEW_ALL_REQUEST,
    REVIEW_ALL_SUCCESS,
    REVIEW_CREATE_FAIL,
    REVIEW_CREATE_REQUEST,
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

export const createReview = (reviewInfo) => async (dispatch, getState) => {
    try {
        dispatch({
            type: REVIEW_CREATE_REQUEST,
        });

        const {
            userLogin: {userInfo},
        } = getState();

        const config = {
            headers: {
                "Content-type": "application/json",
                Authorization: `Bearer ${userInfo.token}`,
            },
        };

        const {data} = await axios.post(
            `/api/review/create/`, 
            reviewInfo, 
            config
        );

        dispatch({
            type: REVIEW_CREATE_SUCCESS,
            payload: data,
        });

    } catch (error) {
        switch (error.response.status) {
            case 400:
                dispatch({
                    type: REVIEW_CREATE_FAIL,
                    payload: 'Ошибка при создании'
                });
                break;
            
            case 403:
                dispatch({
                    type: REVIEW_CREATE_FAIL,
                    payload: 'Ошибка доступа'
                });
                break;

            case 404:
                dispatch({
                    type: REVIEW_CREATE_FAIL,
                    payload: 'Филиал не найден'
                });
                break;
        
            default:
                dispatch({
                    type: REVIEW_CREATE_FAIL,
                    payload: 'Произошла ошибка: ' + error,
                });
                break;
        }
        
    }
} 

export const updateReview = (reviewInfo) => async (dispatch, getState) => {
    try {
        dispatch({
            type: REVIEW_UPDATE_REQUEST,
        });

        const {
            userLogin: {userInfo},
        } = getState();

        const config = {
            headers: {
                "Content-type": "application/json",
                Authorization: `Bearer ${userInfo.token}`,
            },
        };

        const {data} = await axios.put(
            `/api/review/update/${reviewInfo.id}`, 
            reviewInfo,
            config
        );

        dispatch({
            type: REVIEW_UPDATE_SUCCESS,
            payload: data,
        });

    } catch (error) {
        switch (error.response.status) {
            case 400:
                dispatch({
                    type: REVIEW_UPDATE_FAIL,
                    payload: 'Ошибка при запросе'
                });
                break;
            
            case 403:
                dispatch({
                    type: REVIEW_UPDATE_FAIL,
                    payload: 'Ошибка доступа'
                });
                break;

            case 404:
                dispatch({
                    type: REVIEW_UPDATE_FAIL,
                    payload: 'Отзыв не найден'
                });
                break;
        
            default:
                dispatch({
                    type: REVIEW_UPDATE_FAIL,
                    payload: 'Произошла ошибка: ' + error,
                });
                break;
        }
        
    }
}

export const getAllReviews = (reviewsID, reviewPage) => async (dispatch) => {
    try {
        dispatch({
            type: REVIEW_ALL_REQUEST,
        });

        const {
            userLogin: {userInfo},
        } = getState();

        const config = {
            headers: {
                "Content-type": "application/json",
                Authorization: `Bearer ${userInfo.token}`,
            },
        };

        const {data} = await axios.get(
            `/api/review/list/all/${reviewsID}`,
            {page: reviewPage},
            config,
        );

        dispatch({
            type: REVIEW_ALL_SUCCESS,
            payload: data,
        });

    } catch (error) {
        switch (error.response.status) {
            case 400:
                dispatch({
                    type: REVIEW_ALL_FAIL,
                    payload: 'Ошибка при запросе',
                })
                break;

            case 404:
                dispatch({
                    type: REVIEW_ALL_FAIL,
                    payload: 'Отзывы не найдены',
                })
                break;

            default:
                dispatch({
                    type: REVIEW_ALL_FAIL,
                    payload: 'Произошла ошибка: ' + error,
                })
                break;
        }
    }
} 

export const getOneReview = (reviewID) => async (dispatch) => {
    try {
        dispatch({
            type: REVIEW_ONE_REQUEST,
        });

        const {
            userLogin: {userInfo},
        } = getState();

        const config = {
            headers: {
                "Content-type": "application/json",
                Authorization: `Bearer ${userInfo.token}`,
            },
        };

        const {data} = await axios.get(
            `/api/review/read/${reviewID}`,
            config,
        );

        dispatch({
            type: REVIEW_ONE_SUCCESS,
            payload: data,
        });


    } catch (error) {
        switch (error.response.status) {
            case 400:
                dispatch({
                    type: REVIEW_ONE_FAIL,
                    payload: 'Ошибка при запросе',
                })
                break;

            case 403:
                dispatch({
                    type: REVIEW_ONE_FAIL,
                    payload: 'Ошибка доступа',
                })
                break;

            case 404:
                dispatch({
                    type: REVIEW_ONE_FAIL,
                    payload: 'Отзыв не найден',
                })
                break;

            default:
                dispatch({
                    type: REVIEW_ONE_FAIL,
                    payload: 'Произошла ошибка: ' + error,
                })
                break;
        }
    }
}


export const getOneReviewsList = (listID) => async (dispatch) => {
    try {
        dispatch({
            type: REVIEW_LIST_REQUEST,
        });

        const {
            userLogin: {userInfo},
        } = getState();

        const config = {
            headers: {
                "Content-type": "application/json",
                Authorization: `Bearer ${userInfo.token}`,
            },
        };

        const {data} = await axios.get(
            `/api/review/read/list/${listID}`,
            config,
        );

        dispatch({
            type: REVIEW_LIST_SUCCESS,
            payload: data,
        });


    } catch (error) {
        switch (error.response.status) {
            case 400:
                dispatch({
                    type: REVIEW_LIST_FAIL,
                    payload: 'Ошибка при запросе',
                })
                break;

            case 403:
                dispatch({
                    type: REVIEW_LIST_FAIL,
                    payload: 'Ошибка доступа',
                })
                break;

            case 404:
                dispatch({
                    type: REVIEW_LIST_FAIL,
                    payload: 'Отзыв не найден',
                })
                break;

            default:
                dispatch({
                    type: REVIEW_LIST_FAIL,
                    payload: 'Произошла ошибка: ' + error,
                })
                break;
        }
    }
}

export const deleteReview = (reviewID) => async (dispatch, getState) => {
    try {
        dispatch({
            type: REVIEW_DELETE_REQUEST,
        });

        const {
            userLogin: {userInfo},
        } = getState();

        const config = {
            headers: {
                "Content-type": "application/json",
                Authorization: `Bearer ${userInfo.token}`,
            },
        };

        const {data} = await axios.delete(
            `/api/review/delete/${reviewID}`, 
            config
        );

        dispatch({
            type: REVIEW_DELETE_SUCCESS,
        });

    } catch (error) {
        switch (error.response.status) {
            case 400:
                dispatch({
                    type: REVIEW_DELETE_FAIL,
                    payload: 'Ошибка при запросе'
                });
                break;
            
            case 403:
                dispatch({
                    type: REVIEW_DELETE_FAIL,
                    payload: 'Ошибка доступа'
                });
                break;

            case 404:
                dispatch({
                    type: REVIEW_DELETE_FAIL,
                    payload: 'Филиал не найден'
                });
                break;
        
            default:
                dispatch({
                    type: REVIEW_DELETE_FAIL,
                    payload: 'Произошла ошибка: ' + error,
                });
                break;
        }
        
    }
}
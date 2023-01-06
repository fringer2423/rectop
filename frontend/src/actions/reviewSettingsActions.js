import axios from "axios";

import {
    REVIEW_SETTINGS_CREATE_FAIL,
    REVIEW_SETTINGS_CREATE_REQUEST,
    REVIEW_SETTINGS_CREATE_SUCCESS,
    REVIEW_SETTINGS_DELETE_FAIL,
    REVIEW_SETTINGS_DELETE_REQUEST,
    REVIEW_SETTINGS_DELETE_SUCCESS,
    REVIEW_SETTINGS_READ_FAIL,
    REVIEW_SETTINGS_READ_REQUEST,
    REVIEW_SETTINGS_READ_SUCCESS,
    REVIEW_SETTINGS_READ_RESET,
    REVIEW_SETTINGS_UPDATE_FAIL,
    REVIEW_SETTINGS_UPDATE_REQUEST,
    REVIEW_SETTINGS_UPDATE_RESET,
    REVIEW_SETTINGS_UPDATE_SUCCESS,
} from "../constants/reviewSettingsConstants";

export const createReviewSettings = (reviewSettingsInfo) => async (dispatch, getState) => {
    try {
        dispatch({
            type: REVIEW_SETTINGS_CREATE_REQUEST,
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
            `/api/review_settings/create/`, 
            reviewSettingsInfo, 
            config
        );

        dispatch({
            type: REVIEW_SETTINGS_CREATE_SUCCESS,
            payload: data,
        });

    } catch (error) {
        switch (error.response.status) {
            case 400:
                dispatch({
                    type: REVIEW_SETTINGS_CREATE_FAIL,
                    payload: 'Ошибка при создании'
                });
                break;
            
            case 403:
                dispatch({
                    type: REVIEW_SETTINGS_CREATE_FAIL,
                    payload: 'Ошибка доступа'
                });
                break;

            case 404:
                dispatch({
                    type: REVIEW_SETTINGS_CREATE_FAIL,
                    payload: 'Компания не найдена'
                });
                break;
        
            default:
                dispatch({
                    type: REVIEW_SETTINGS_CREATE_FAIL,
                    payload: 'Произошла ошибка: ' + error,
                });
                break;
        }
        
    }
} 

export const getReviewSettings = (reviewSettingsID) => async (dispatch, getState) => {
    try {
        dispatch({
            type: REVIEW_SETTINGS_READ_REQUEST,
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
            `/api/review_settings/read/${reviewSettingsID}`, 
            config
        );

        dispatch({
            type: REVIEW_SETTINGS_READ_SUCCESS,
            payload: data,
        });

    } catch (error) {
        switch (error.response.status) {
            case 400:
                dispatch({
                    type: REVIEW_SETTINGS_READ_FAIL,
                    payload: 'Ошибка при запросе'
                });
                break;
            
            case 403:
                dispatch({
                    type: REVIEW_SETTINGS_READ_FAIL,
                    payload: 'Ошибка доступа'
                });
                break;

            case 404:
                dispatch({
                    type: REVIEW_SETTINGS_READ_FAIL,
                    payload: 'Компания не найдена'
                });
                break;
        
            default:
                dispatch({
                    type: REVIEW_SETTINGS_READ_FAIL,
                    payload: 'Произошла ошибка: ' + error,
                });
                break;
        }
        
    }
}

export const updateReviewSettings = (reviewSettingsInfo) => async (dispatch, getState) => {
    try {
        dispatch({
            type: REVIEW_SETTINGS_UPDATE_REQUEST,
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
            `/api/review_settings/update/${reviewSettingsInfo.id}`, 
            reviewSettingsInfo,
            config
        );

        dispatch({
            type: REVIEW_SETTINGS_UPDATE_SUCCESS,
            payload: data,
        });

    } catch (error) {
        switch (error.response.status) {
            case 400:
                dispatch({
                    type: REVIEW_SETTINGS_UPDATE_FAIL,
                    payload: 'Ошибка при запросе'
                });
                break;
            
            case 403:
                dispatch({
                    type: REVIEW_SETTINGS_UPDATE_FAIL,
                    payload: 'Ошибка доступа'
                });
                break;

            case 404:
                dispatch({
                    type: REVIEW_SETTINGS_UPDATE_FAIL,
                    payload: 'Компания не найдена'
                });
                break;
        
            default:
                dispatch({
                    type: REVIEW_SETTINGS_UPDATE_FAIL,
                    payload: 'Произошла ошибка: ' + error,
                });
                break;
        }
        
    }
}

export const deleteReviewSettings = (reviewSettingsID) => async (dispatch, getState) => {
    try {
        dispatch({
            type: REVIEW_SETTINGS_DELETE_REQUEST,
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
            `/api/reviewSettings/delete/${reviewSettingsID}`, 
            config
        );

        dispatch({
            type: REVIEW_SETTINGS_DELETE_SUCCESS,
        });

        dispatch({
            type: REVIEW_SETTINGS_READ_RESET,
        });

        dispatch({
            type: REVIEW_SETTINGS_UPDATE_RESET,
        });

    } catch (error) {
        switch (error.response.status) {
            case 400:
                dispatch({
                    type: REVIEW_SETTINGS_DELETE_FAIL,
                    payload: 'Ошибка при запросе'
                });
                break;
            
            case 403:
                dispatch({
                    type: REVIEW_SETTINGS_DELETE_FAIL,
                    payload: 'Ошибка доступа'
                });
                break;

            case 404:
                dispatch({
                    type: REVIEW_SETTINGS_DELETE_FAIL,
                    payload: 'Компания не найдена'
                });
                break;
        
            default:
                dispatch({
                    type: REVIEW_SETTINGS_DELETE_FAIL,
                    payload: 'Произошла ошибка: ' + error,
                });
                break;
        }
        
    }
}

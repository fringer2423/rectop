import axios from "axios";

import {
    TELEBOT_CREATE_FAIL,
    TELEBOT_CREATE_REQUEST,
    TELEBOT_CREATE_SUCCESS,
    TELEBOT_DELETE_FAIL,
    TELEBOT_DELETE_REQUEST,
    TELEBOT_DELETE_SUCCESS,
    TELEBOT_READ_FAIL,
    TELEBOT_READ_REQUEST,
    TELEBOT_READ_RESET,
    TELEBOT_READ_SUCCESS,
    TELEBOT_UPDATE_FAIL,
    TELEBOT_UPDATE_REQUEST,
    TELEBOT_UPDATE_RESET,
    TELEBOT_UPDATE_SUCCESS,
} from "../constants/telebotConstants";


export const createTelebot = (telebotID, branchID) => async (dispatch, getState) => {
    try {
        dispatch({
            type: TELEBOT_CREATE_REQUEST,
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
            `/api/telebot/create/`, 
            {tg_id: telebotID, branch_id: branchID},
            config
        );

        dispatch({
            type: TELEBOT_CREATE_SUCCESS,
            payload: data,
        });

    } catch (error) {
        switch (error.response.status) {
            case 400:
                dispatch({
                    type: TELEBOT_CREATE_FAIL,
                    payload: 'Ошибка при создании'
                });
                break;
            
            case 403:
                dispatch({
                    type: TELEBOT_CREATE_FAIL,
                    payload: 'Ошибка доступа'
                });
                break;

            case 404:
                dispatch({
                    type: TELEBOT_CREATE_FAIL,
                    payload: 'Филиал не найден'
                });
                break;
        
            default:
                dispatch({
                    type: TELEBOT_CREATE_FAIL,
                    payload: 'Произошла ошибка: ' + error,
                });
                break;
        }
        
    }
}

export const getTelebot = (telebotID) => async (dispatch, getState) => {
    try {
        dispatch({
            type: TELEBOT_READ_REQUEST,
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
            `/api/telebot/read/${telebotID}`, 
            config
        );

        dispatch({
            type: TELEBOT_READ_SUCCESS,
            payload: data,
        });

    } catch (error) {
        switch (error.response.status) {
            case 400:
                dispatch({
                    type: TELEBOT_READ_FAIL,
                    payload: 'Ошибка при запросе'
                });
                break;
            
            case 403:
                dispatch({
                    type: TELEBOT_READ_FAIL,
                    payload: 'Ошибка доступа'
                });
                break;

            case 404:
                dispatch({
                    type: TELEBOT_READ_FAIL,
                    payload: 'Бот не найден'
                });
                break;
        
            default:
                dispatch({
                    type: TELEBOT_READ_FAIL,
                    payload: 'Произошла ошибка: ' + error,
                });
                break;
        }
        
    }
}

export const updateTelebot = (telebotID, id) => async (dispatch, getState) => {
    try {
        dispatch({
            type: TELEBOT_UPDATE_REQUEST,
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
            `/api/telebot/update/${id}`, 
            {tg_id: telebotID},
            config
        );

        dispatch({
            type: TELEBOT_UPDATE_SUCCESS,
            payload: data,
        });

    } catch (error) {
        switch (error.response.status) {
            case 400:
                dispatch({
                    type: TELEBOT_UPDATE_FAIL,
                    payload: 'Ошибка при запросе'
                });
                break;
            
            case 403:
                dispatch({
                    type: TELEBOT_UPDATE_FAIL,
                    payload: 'Ошибка доступа'
                });
                break;

            case 404:
                dispatch({
                    type: TELEBOT_UPDATE_FAIL,
                    payload: 'Компания не найдена'
                });
                break;
        
            default:
                dispatch({
                    type: TELEBOT_UPDATE_FAIL,
                    payload: 'Произошла ошибка: ' + error,
                });
                break;
        }
        
    }
}

export const deleteTelebot = (telebotID) => async (dispatch, getState) => {
    try {
        dispatch({
            type: TELEBOT_DELETE_REQUEST,
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
            `/api/telebot/delete/${telebotID}`, 
            config
        );

        dispatch({
            type: TELEBOT_DELETE_SUCCESS,
        });

        dispatch({
            type: TELEBOT_READ_RESET,
        });

        dispatch({
            type: TELEBOT_UPDATE_RESET,
        });

    } catch (error) {
        switch (error.response.status) {
            case 400:
                dispatch({
                    type: TELEBOT_DELETE_FAIL,
                    payload: 'Ошибка при запросе'
                });
                break;
            
            case 403:
                dispatch({
                    type: TELEBOT_DELETE_FAIL,
                    payload: 'Ошибка доступа'
                });
                break;

            case 404:
                dispatch({
                    type: TELEBOT_DELETE_FAIL,
                    payload: 'Бот не найден'
                });
                break;
        
            default:
                dispatch({
                    type: TELEBOT_DELETE_FAIL,
                    payload: 'Произошла ошибка: ' + error,
                });
                break;
        }
        
    }
}

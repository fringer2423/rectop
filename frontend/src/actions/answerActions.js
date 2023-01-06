import axios from "axios";

import {
    ANSWER_CREATE_FAIL,
    ANSWER_CREATE_REQUEST,
    ANSWER_CREATE_SUCCESS,
    ANSWER_DELETE_FAIL,
    ANSWER_DELETE_REQUEST,
    ANSWER_DELETE_SUCCESS,
    ANSWER_READ_FAIL,
    ANSWER_READ_REQUEST,
    ANSWER_READ_SUCCESS,
    ANSWER_READ_RESET,
    ANSWER_UPDATE_FAIL,
    ANSWER_UPDATE_REQUEST,
    ANSWER_UPDATE_RESET,
    ANSWER_UPDATE_SUCCESS,
} from "../constants/answerConstants";


export const createAnswer = (answerInfo) => async (dispatch, getState) => {
    try {
        dispatch({
            type: ANSWER_CREATE_REQUEST,
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
            `/api/answer/create/`, 
            answerInfo, 
            config
        );

        dispatch({
            type: ANSWER_CREATE_SUCCESS,
            payload: data,
        });

    } catch (error) {
        switch (error.response.status) {
            case 400:
                dispatch({
                    type: ANSWER_CREATE_FAIL,
                    payload: 'Ошибка при создании'
                });
                break;
            
            case 403:
                dispatch({
                    type: ANSWER_CREATE_FAIL,
                    payload: 'Ошибка доступа'
                });
                break;

            case 404:
                dispatch({
                    type: ANSWER_CREATE_FAIL,
                    payload: 'Отзыв не найден'
                });
                break;

            case 406:
                dispatch({
                    type: ANSWER_CREATE_FAIL,
                    payload: 'Такой ответ уже создан'
                });
                break;
        
            default:
                dispatch({
                    type: ANSWER_CREATE_FAIL,
                    payload: 'Произошла ошибка: ' + error,
                });
                break;
        }
        
    }
} 

export const getAnswer = (answerID) => async (dispatch, getState) => {
    try {
        dispatch({
            type: ANSWER_READ_REQUEST,
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
            `/api/answer/read/${answerID}`, 
            config
        );

        dispatch({
            type: ANSWER_READ_SUCCESS,
            payload: data,
        });

    } catch (error) {
        switch (error.response.status) {
            case 400:
                dispatch({
                    type: ANSWER_READ_FAIL,
                    payload: 'Ошибка при запросе'
                });
                break;
            
            case 403:
                dispatch({
                    type: ANSWER_READ_FAIL,
                    payload: 'Ошибка доступа'
                });
                break;

            case 404:
                dispatch({
                    type: ANSWER_READ_FAIL,
                    payload: 'Ответ не найден'
                });
                break;
        
            default:
                dispatch({
                    type: ANSWER_READ_FAIL,
                    payload: 'Произошла ошибка: ' + error,
                });
                break;
        }
        
    }
}

export const updateAnswer = (answerInfo) => async (dispatch, getState) => {
    try {
        dispatch({
            type: ANSWER_UPDATE_REQUEST,
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
            `/api/answer/update/${answerInfo.id}`, 
            config
        );

        dispatch({
            type: ANSWER_UPDATE_SUCCESS,
            payload: data,
        });

    } catch (error) {
        switch (error.response.status) {
            case 400:
                dispatch({
                    type: ANSWER_UPDATE_FAIL,
                    payload: 'Ошибка при запросе'
                });
                break;
            
            case 403:
                dispatch({
                    type: ANSWER_UPDATE_FAIL,
                    payload: 'Ошибка доступа'
                });
                break;

            case 404:
                dispatch({
                    type: ANSWER_UPDATE_FAIL,
                    payload: 'Ответ не найден'
                });
                break;
        
            default:
                dispatch({
                    type: ANSWER_UPDATE_FAIL,
                    payload: 'Произошла ошибка: ' + error,
                });
                break;
        }
        
    }
}

export const answerDelete = (answerID) => async (dispatch, getState) => {
    try {
        dispatch({
            type: ANSWER_DELETE_REQUEST,
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
            `/api/answer/delete/${answerID}`, 
            config
        );

        dispatch({
            type: ANSWER_DELETE_SUCCESS,
        });

        dispatch({
            type: ANSWER_READ_RESET,
        });

        dispatch({
            type: ANSWER_UPDATE_RESET,
        });

    } catch (error) {
        switch (error.response.status) {
            case 400:
                dispatch({
                    type: ANSWER_DELETE_FAIL,
                    payload: 'Ошибка при запросе'
                });
                break;
            
            case 403:
                dispatch({
                    type: ANSWER_DELETE_FAIL,
                    payload: 'Ошибка доступа'
                });
                break;

            case 404:
                dispatch({
                    type: ANSWER_DELETE_FAIL,
                    payload: 'Ответ не найден'
                });
                break;
        
            default:
                dispatch({
                    type: ANSWER_DELETE_FAIL,
                    payload: 'Произошла ошибка: ' + error,
                });
                break;
        }
        
    }
}
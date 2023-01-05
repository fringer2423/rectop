import axios from "axios";

import {
    RATE_ADD_SUCCESS,
    RATE_ADD_FAIL,
    RATE_ADD_REQUEST,
    RATE_CHANGE_FAIL,
    RATE_CHANGE_REQUEST,
    RATE_CHANGE_SUCCESS,
    RATE_READ_FAIL,
    RATE_READ_REQUEST,
    RATE_READ_SUCCESS,
} from "../constants/rateConstants";

export const rateAdd = (rateType) => async (dispatch, getState) => {
    try {
        dispatch({
            type: RATE_ADD_REQUEST,
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
            "/api/rate/create",
            {type: rateType},
            config,
        );
        
        dispatch({
            type: RATE_ADD_SUCCESS, 
            payload: data,
        });

    } catch (error) {
        switch (error) {
            case 400:
                dispatch({
                    type: RATE_ADD_FAIL,
                    payload: 'Ошибка при создании',
                })
                break;
            case 401:
                dispatch({
                    type: RATE_ADD_FAIL,
                    payload: 'Пустой или неправильный токен',
                })
                break;
            case 403:
                dispatch({
                    type: RATE_ADD_FAIL,
                    payload: 'Ошибка доступа',
                })
                break;
            case 406:
                dispatch({
                    type: RATE_ADD_FAIL,
                    payload: 'У вас уже есть тариф',
                })
                break;
            default:
                dispatch({
                    type: RATE_ADD_FAIL,
                    payload: 'Произошла ошибка: ' + error,
                })
                break;
        }
    }
}

export const rateRead = () => async (dispatch, getState) => {
    try {
        dispatch({
            type: RATE_READ_REQUEST,
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
            'api/rate/read', 
            config,
        );

        dispatch({
            type: RATE_READ_SUCCESS,
            payload: data,
        })

    } catch (error) {
        switch (error) {
            case 400:
                dispatch({
                    type: RATE_READ_FAIL,
                    payload: 'Ошибка при запросе',
                })
                break;
            case 403:
                dispatch({
                    type: RATE_READ_FAIL,
                    payload: 'Ошибка доступа',
                })
                break;
            case 404:
                dispatch({
                    type: RATE_READ_FAIL,
                    payload: 'Тариф не найден',
                })
                break;
        
            default:
                dispatch({
                    type: RATE_READ_FAIL,
                    payload: 'Произошла ошибка: ' + error,
                })
                break;
        }
        
    }
}

export const rateUpdate = (rateType) =>  async (dispatch, getState) => {
    try {
        dispatch({
            type: RATE_CHANGE_REQUEST,
        })

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
            `api/rate/update`,
            {type: rateType},
            config,
        );

        dispatch({
            type: RATE_CHANGE_SUCCESS,
            payload: data,
        });

        dispatch({
            type: RATE_READ_SUCCESS,
            payload: data,
        });

    } catch (error) {
        switch (error) {
            case 400:
                dispatch({
                    type: RATE_CHANGE_FAIL,
                    payload: 'Ошибка при запросе',
                })
                break;
            case 403:
                dispatch({
                    type: RATE_CHANGE_FAIL,
                    payload: 'Ошибка доступа',
                })
                break;
            case 404:
                dispatch({
                    type: RATE_CHANGE_FAIL,
                    payload: 'Тариф не найден',
                })
                break;
        
            default:
                dispatch({
                    type: RATE_CHANGE_FAIL,
                    payload: 'Произошла ошибка: ' + error,
                })
                break;
        }
    }
}
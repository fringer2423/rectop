import axios from "axios";

import {
    CONNECT_ALL_FAIL,
    CONNECT_ALL_REQUEST,
    CONNECT_ALL_SUCCESS,
    CONNECT_CREATE_FAIL,
    CONNECT_CREATE_REQUEST,
    CONNECT_CREATE_SUCCESS,
    CONNECT_DELETE_FAIL,
    CONNECT_DELETE_REQUEST,
    CONNECT_DELETE_SUCCESS,
    CONNECT_GET_ONE_FAIL,
    CONNECT_GET_ONE_REQUEST,
    CONNECT_GET_ONE_RESET,
    CONNECT_GET_ONE_SUCCESS,
    CONNECT_UPDATE_FAIL,
    CONNECT_UPDATE_REQUEST,
    CONNECT_UPDATE_RESET,
    CONNECT_UPDATE_SUCCESS,
} from "../constants/connectConstants";

export const createConnect = (connectInfo) => async (dispatch, getState) => {
    try {
        dispatch({
            type: CONNECT_CREATE_REQUEST,
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
            `/api/connect/create/`, 
            connectInfo, 
            config
        );

        dispatch({
            type: CONNECT_CREATE_SUCCESS,
            payload: data,
        });

    } catch (error) {
        switch (error.response.status) {
            case 400:
                dispatch({
                    type: CONNECT_CREATE_FAIL,
                    payload: 'Ошибка при создании'
                });
                break;
            
            case 403:
                dispatch({
                    type: CONNECT_CREATE_FAIL,
                    payload: 'Ошибка доступа'
                });
                break;

            case 404:
                dispatch({
                    type: CONNECT_CREATE_FAIL,
                    payload: 'Филиал не найден'
                });
                break;

            case 406:
                dispatch({
                    type: CONNECT_CREATE_FAIL,
                    payload: 'Такой connect уже создан для филиала'
                });
                break;
        
            default:
                dispatch({
                    type: CONNECT_CREATE_FAIL,
                    payload: 'Произошла ошибка: ' + error,
                });
                break;
        }
        
    }
}

export const updateConnect = (connectInfo) => async (dispatch, getState) => {
    try {
        dispatch({
            type: CONNECT_UPDATE_REQUEST,
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
            `/api/connect/update/${connectInfo.id}`, 
            connectInfo,
            config
        );

        dispatch({
            type: CONNECT_UPDATE_SUCCESS,
            payload: data,
        });

    } catch (error) {
        switch (error.response.status) {
            case 400:
                dispatch({
                    type: CONNECT_UPDATE_FAIL,
                    payload: 'Ошибка при запросе'
                });
                break;
            
            case 403:
                dispatch({
                    type: CONNECT_UPDATE_FAIL,
                    payload: 'Ошибка доступа'
                });
                break;

            case 404:
                dispatch({
                    type: CONNECT_UPDATE_FAIL,
                    payload: 'Connect не найден'
                });
                break;
        
            default:
                dispatch({
                    type: CONNECT_UPDATE_FAIL,
                    payload: 'Произошла ошибка: ' + error,
                });
                break;
        }
        
    }
}

export const getAllConnects = (connectsID) => async (dispatch) => {
    try {
        dispatch({
            type: CONNECT_ALL_REQUEST,
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
            `/api/connect/read/list/${connectsID}`,
            config,
        );

        dispatch({
            type: CONNECT_ALL_SUCCESS,
            payload: data,
        });

    } catch (error) {
        switch (error.response.status) {
            case 400:
                dispatch({
                    type: CONNECT_ALL_FAIL,
                    payload: 'Ошибка при запросе',
                })
                break;

            case 404:
                dispatch({
                    type: CONNECT_ALL_FAIL,
                    payload: 'Компания не найдена',
                })
                break;

            default:
                dispatch({
                    type: CONNECT_ALL_FAIL,
                    payload: 'Произошла ошибка: ' + error,
                })
                break;
        }
    }
} 

export const getOneConnect = (connectID) => async (dispatch) => {
    try {
        dispatch({
            type: CONNECT_GET_ONE_REQUEST,
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
            `/api/connect/read/${connectID}`,
            config,
        );

        dispatch({
            type: CONNECT_GET_ONE_SUCCESS,
            payload: data,
        });


    } catch (error) {
        switch (error.response.status) {
            case 400:
                dispatch({
                    type: CONNECT_GET_ONE_FAIL,
                    payload: 'Ошибка при запросе',
                })
                break;

            case 403:
                dispatch({
                    type: CONNECT_GET_ONE_FAIL,
                    payload: 'Ошибка доступа',
                })
                break;

            case 404:
                dispatch({
                    type: CONNECT_GET_ONE_FAIL,
                    payload: 'Connect не найден',
                })
                break;

            default:
                dispatch({
                    type: CONNECT_GET_ONE_FAIL,
                    payload: 'Произошла ошибка: ' + error,
                })
                break;
        }
    }
}

export const deleteConnect = (connectID) => async (dispatch, getState) => {
    try {
        dispatch({
            type: CONNECT_DELETE_REQUEST,
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
            `/api/connect/delete/${connectID}`, 
            config
        );

        dispatch({
            type: CONNECT_DELETE_SUCCESS,
        });

    } catch (error) {
        switch (error.response.status) {
            case 400:
                dispatch({
                    type: CONNECT_DELETE_FAIL,
                    payload: 'Ошибка при запросе'
                });
                break;
            
            case 403:
                dispatch({
                    type: CONNECT_DELETE_FAIL,
                    payload: 'Ошибка доступа'
                });
                break;

            case 404:
                dispatch({
                    type: CONNECT_DELETE_FAIL,
                    payload: 'Connect не найден'
                });
                break;
        
            default:
                dispatch({
                    type: CONNECT_DELETE_FAIL,
                    payload: 'Произошла ошибка: ' + error,
                });
                break;
        }
        
    }
}


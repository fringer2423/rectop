import axios from "axios";

import {
    BRANCH_CREATE_REQUEST,
    BRANCH_CREATE_SUCCESS,
    BRANCH_CREATE_FAIL,
    BRANCH_ALL_FAIL,
    BRANCH_ALL_REQUEST,
    BRANCH_ALL_SUCCESS,
    BRANCH_GET_ONE_FAIL,
    BRANCH_GET_ONE_REQUEST,
    BRANCH_GET_ONE_SUCCESS,
    BRANCH_UPDATE_FAIL,
    BRANCH_UPDATE_REQUEST,
    BRANCH_UPDATE_RESET,
    BRANCH_UPDATE_SUCCESS,
} from "../constants/branchConstants";

export const createBranch = (branchInfo) => async (dispatch, getState) => {
    try {
        dispatch({
            type: BRANCH_CREATE_REQUEST,
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
            `/api/branch/create/`,
            branchInfo,
            config,
        );

        dispatch({
            type: BRANCH_CREATE_SUCCESS,
            payload: data,
        });

    } catch (error) {
        switch (error.response.status) {
            case 400:
                dispatch({
                    type: BRANCH_CREATE_FAIL,
                    payload: 'Ошибка при создании',
                });
                break;
            
            case 401: 
                dispatch({
                    type: BRANCH_CREATE_FAIL,
                    payload: 'Пустой или неправильный токен',
                });
                break;
            
            case 403: 
                dispatch({
                    type: BRANCH_CREATE_FAIL,
                    payload: 'Ошибка доступа',
                });
                break;
            
            case 404: 
                dispatch({
                    type: BRANCH_CREATE_FAIL,
                    payload: 'Компания не найдена',
                });
                break;
        
            default:
                dispatch({
                    type: BRANCH_CREATE_FAIL,
                    payload: 'Произошла ошибка' + error,
                });
                break;
        }
    }
}

export const getListBranches = (info, listID) => async (dispatch, getState) => {
    try {
        dispatch({
            type: BRANCH_ALL_REQUEST,
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
            `/branch/read/list/${listID}`,
            info, 
            config,
        );

        dispatch({
            type: BRANCH_ALL_SUCCESS,
            payload: data,
        });

    } catch (error) {
        switch (error.response.status) {
            case 400:
                dispatch({
                    type: BRANCH_ALL_FAIL,
                    payload: 'Ошибка при запросе',
                });
                break;
            
            case 401: 
                dispatch({
                    type: BRANCH_ALL_FAIL,
                    payload: 'Пустой или неправильный токен',
                });
                break;
            
            case 403: 
                dispatch({
                    type: BRANCH_ALL_FAIL,
                    payload: 'Ошибка доступа',
                });
                break;
            
            case 404: 
                dispatch({
                    type: BRANCH_ALL_FAIL,
                    payload: 'Компания не найдена',
                });
                break;
        
            default:
                dispatch({
                    type: BRANCH_ALL_FAIL,
                    payload: 'Произошла ошибка' + error,
                });
                break;
        }
    }
}

export const getOneBranch = (branchID) => async (dispatch, getState) => {
        try {
            dispatch({
                type: BRANCH_GET_ONE_REQUEST,
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
                `/branch/read/${branchID}`,
                config,
            );
    
            dispatch({
                type: BRANCH_GET_ONE_SUCCESS,
                payload: data,
            });

    } catch (error) {
        switch (error.response.status) {
            case 400:
                dispatch({
                    type: BRANCH_GET_ONE_FAIL,
                    payload: 'Ошибка при запросе',
                });
                break;
            
            case 401: 
                dispatch({
                    type: BRANCH_GET_ONE_FAIL,
                    payload: 'Пустой или неправильный токен',
                });
                break;
            
            case 403: 
                dispatch({
                    type: BRANCH_GET_ONE_FAIL,
                    payload: 'Ошибка доступа',
                });
                break;
            
            case 404: 
                dispatch({
                    type: BRANCH_GET_ONE_FAIL,
                    payload: 'Компания не найдена',
                });
                break;
        
            default:
                dispatch({
                    type: BRANCH_GET_ONE_FAIL,
                    payload: 'Произошла ошибка' + error,
                });
                break;
        }
    }
}

export const updateBranch = (branchID, info) => async (dispatch, getState) => {
    try {
        dispatch({
            type: BRANCH_UPDATE_REQUEST,
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
            `/branch/read/list/${branchID}`,
            info, 
            config,
        );

        dispatch({
            type: BRANCH_UPDATE_SUCCESS,
            payload: data,
        });
    } catch (error) {
        switch (error.response.status) {
            case 400:
                dispatch({
                    type: BRANCH_UPDATE_FAIL,
                    payload: 'Ошибка при запросе',
                });
                break;
            
            case 401: 
                dispatch({
                    type: BRANCH_UPDATE_FAIL,
                    payload: 'Пустой или неправильный токен',
                });
                break;
            
            case 403: 
                dispatch({
                    type: BRANCH_UPDATE_FAIL,
                    payload: 'Ошибка доступа',
                });
                break;
            
            case 404: 
                dispatch({
                    type: BRANCH_UPDATE_FAIL,
                    payload: 'Филиал не найден',
                });
                break;
        
            default:
                dispatch({
                    type: BRANCH_UPDATE_FAIL,
                    payload: 'Произошла ошибка' + error,
                });
                break;
        }
    }
}


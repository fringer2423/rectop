import axios from 'axios'
import {
    USER_LOGIN_REQUEST,
    USER_LOGIN_SUCCESS,
    USER_LOGIN_FAIL,

    USER_LOGOUT,

    USER_REGISTER_REQUEST,
    USER_REGISTER_SUCCESS,
    USER_REGISTER_FAIL,

    USER_VERIFY_REQUEST,
    USER_VERIFY_SUCCESS,
    USER_VERIFY_FAIL,

    USER_VERIFY_LOGIN_REQUEST,
    USER_VERIFY_LOGIN_SUCCESS,
    USER_VERIFY_LOGIN_FAIL,

    USER_LOGIN_CHECK_REQUEST,
    USER_LOGIN_CHECK_SUCCESS,
    USER_LOGIN_CHECK_FAIL,

    USER_DETAILS_REQUEST,
    USER_DETAILS_SUCCESS,
    USER_DETAILS_FAIL,
    USER_DETAILS_RESET,

    USER_UPDATE_REQUEST,
    USER_UPDATE_SUCCESS,
    USER_UPDATE_FAIL,

} from '../constants/userConstants'

export const login = (email, password) => async (dispatch) => {
    try {
        dispatch({
            type: USER_LOGIN_REQUEST
        })

        const config = {
            headers: {
                'Content-type': 'application/json'
            }
        }

        const {data} = await axios.post(
            '/api/user/login/',
            {'username': email, 'password': password},
            config
        )

        dispatch({
            type: USER_LOGIN_SUCCESS,
            payload: data
        })

    } catch (error) {
        switch (error.response.status) {
            case 401:
                dispatch({
                    type: USER_LOGIN_FAIL,
                    payload: 'Вы не зарегистрированы',
                })
                break;
            case 400:
                dispatch({
                    type: USER_LOGIN_FAIL,
                    payload: 'Ошибка авторизации. Попробуйте еще раз',
                })
                break;
            default:
                console.log(error.response && error.response.data.detail
                    ? error.response.data.detail
                    : error.message);
                dispatch({
                    type: USER_LOGIN_FAIL,
                    payload: "Ошибка авторизации. ПоCommit a588cd00пробуйте еще раз"
                })

        }

    }
}

export const checkLogin = () => async (dispatch, getState) => {
    try {
        dispatch({
            type: USER_LOGIN_CHECK_REQUEST
        })

        const {
            userLogin: {userInfo},
        } = getState()

        const config = {
            headers: {
                'Content-type': 'application/json',
                Authorization: `Bearer ${userInfo.token}`
            }
        }

        const {data} = await axios.get(
            `/api/user/send_code/`,
            config
        )

        dispatch({
            type: USER_LOGIN_CHECK_SUCCESS,
            payload: data,
        })

    } catch (error) {
        dispatch({
            type: USER_LOGIN_CHECK_FAIL,
            payload: error.response && error.response.data.detail
                ? error.response.data.detail
                : error.message,
        })
    }
}


export const verifyLogin = (code) => async (dispatch, getState) => {
    try {
        dispatch({
            type: USER_VERIFY_LOGIN_REQUEST
        })

        const {
            userLogin: {userInfo},
        } = getState()

        const config = {
            headers: {
                'Content-type': 'application/json',
                Authorization: `Bearer ${userInfo.token}`
            }
        }

        const {data} = await axios.post(
            `/api/user/verify_code/`,
            {'verify_code': code},
            config
        )


        dispatch({
            type: USER_VERIFY_LOGIN_SUCCESS,
            payload: data,
        })


        localStorage.setItem('userInfo', JSON.stringify(userInfo))

    } catch (error) {
        dispatch({
            type: USER_VERIFY_LOGIN_FAIL,
            payload: error.response && error.response.data.detail
                ? error.response.data.detail
                : error.message,
        })
    }
}


export const logout = () => (dispatch) => {
    localStorage.removeItem('userInfo');
    dispatch({type: USER_LOGOUT});
    dispatch({type: USER_DETAILS_RESET});
}


export const register = (first_name, last_name, email, password) => async (dispatch) => {
    try {
        dispatch({
            type: USER_REGISTER_REQUEST
        })

        const config = {
            headers: {
                'Content-type': 'application/json'
            }
        }

        const {data} = await axios.post(
            '/api/user/create/',
            {'first_name': first_name, 'last_name': last_name, 'email': email, 'password': password},
            config
        )

        dispatch({
            type: USER_REGISTER_SUCCESS,
            payload: data
        })

    } catch (error) {
        switch (error.response.status) {
            case 400:
                dispatch({
                    type: USER_REGISTER_FAIL,
                    payload: 'Ошибка при регистрации. Попробуйте позже',
                });
                break;
            case 422:
                dispatch({
                    type: USER_REGISTER_FAIL,
                    payload: 'Вы не заполнили одно из полей',
                });
                break;

            default:
                dispatch({
                    type: USER_REGISTER_FAIL,
                    payload: error.response && error.response.data.detail
                        ? error.response.data.detail
                        : error.message,
                });
                break;
        }
    }
}


export const verify = (code) => async (dispatch) => {
    try {

        dispatch({
            type: USER_VERIFY_REQUEST
        })

        const config = {
            headers: {
                'Content-type': 'application/json'
            }
        }

        const {data} = await axios.get(
            `/api/user/verify/${code}`,
            config
        )

        dispatch({
            type: USER_VERIFY_SUCCESS,
            payload: data
        });

        dispatch({
            type: USER_LOGIN_SUCCESS,
            payload: data
        });

        dispatch({
            type: USER_VERIFY_LOGIN_SUCCESS
        })

        localStorage.setItem('userInfo', JSON.stringify(data))

    } catch (error) {
        switch (error.response.status) {
            case 400:
                dispatch({
                    type: USER_VERIFY_FAIL,
                    payload: 'Ошибка при регистрации. Попробуйте позже',
                });
                break;
            case 401:
                dispatch({
                    type: USER_VERIFY_FAIL,
                    payload: 'Пустой или неправильный токен',
                });
                break;
            case 404:
                dispatch({
                    type: USER_VERIFY_FAIL,
                    payload: 'Пользователь не найден',
                });
                break;
            case 500:
                dispatch({
                    type: USER_VERIFY_FAIL,
                    payload: 'Произошла ошибка. Повторите позже',
                });
                break;
            default:
                dispatch({
                    type: USER_REGISTER_FAIL,
                    payload: error.response && error.response.data.detail
                        ? error.response.data.detail
                        : error.message,
                });
                break;
        }
    }
}

export const getUserDetails = () => async (dispatch, getState) => {
    try {
        dispatch({
            type: USER_DETAILS_REQUEST
        })

        const {
            userLogin: {userInfo},
        } = getState()

        const config = {
            headers: {
                'Content-type': 'application/json',
                Authorization: `Bearer ${userInfo.token}`
            }
        }

        const {data} = await axios.get(
            `/api/user/read/`,
            config
        )

        dispatch({
            type: USER_DETAILS_SUCCESS,
            payload: data
        })


    } catch (error) {
        dispatch({
            type: USER_DETAILS_FAIL,
            payload: error.response && error.response.data.detail
                ? error.response.data.detail
                : error.message,
        })
    }
}


export const updateUser = (user) => async (dispatch, getState) => {
    try {
        dispatch({
            type: USER_UPDATE_REQUEST
        })

        const {
            userLogin: {userInfo},
        } = getState()

        const config = {
            headers: {
                'Content-type': 'application/json',
                Authorization: `Bearer ${userInfo.token}`
            }
        }

        const {data} = await axios.put(
            `/api/user/update/`,
            user,
            config
        )

        dispatch({
            type: USER_UPDATE_SUCCESS,
        })

        dispatch({
            type: USER_DETAILS_SUCCESS,
            payload: data
        })


    } catch (error) {
        dispatch({
            type: USER_UPDATE_FAIL,
            payload: error.response && error.response.data.detail
                ? error.response.data.detail
                : error.message,
        })
    }
}

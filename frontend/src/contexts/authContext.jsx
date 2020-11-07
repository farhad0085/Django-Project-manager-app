import React, { Component, createContext } from 'react';
import axios from '../utils/axios'
import { getHeaders } from '../utils'

let Context = null

const { Provider, Consumer } = Context = createContext()


class AuthProvider extends Component {

    state = {
        isAuthenticated: false,
        token: null,
        loading: false,
        error: '',
        methods: {
            login: (username, password) => this.login(username, password),
            logout: () => this.logout()
        }
    }

    login = (username, password) => {
        
        this.setState({
            loading: true,
            error: ''
        })

        axios.post("/auth/login/", {
            username: username,
            password: password
        })
        .then(({data}) => {
            localStorage.setItem('token', data.key)
            this.setState({
                token: data.key,
                isAuthenticated: true,
                loading: false
            })
        })
        .catch(e => {
            console.log(e)
            this.setState({
                loading: false,
                error: "Failed to login with these credentials"
            })
        })
    }

    logout = () => {
        this.setState({
            loading: true
        })

        axios.post('/auth/logout/', {}, {headers: getHeaders()})
        .then(data => {
            localStorage.removeItem('token')
            this.setState({
                isAuthenticated: false,
                token: '',
                loading: false
            })
        })
        .catch(error => {
            console.log(error);
            this.setState({
                loading: false,
                error: "Unable to logout, please try again"
            })
        })
        
    }

    componentDidMount(){
        this.setState({
            isAuthenticated: localStorage.getItem('token') ? true : false,
            token: localStorage.getItem('token')
        })
    }

    render() {
        return (
            <Provider value={this.state}>
                {this.props.children}
            </Provider>
        );
    }
}

export { AuthProvider, Consumer as AuthConsumer, Context as AuthContext }
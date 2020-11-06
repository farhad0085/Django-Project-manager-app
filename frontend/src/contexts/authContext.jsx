import React, { Component, createContext } from 'react';
import axios from '../utils/axios'


let Context = null

const { Provider, Consumer } = Context = createContext()


class AuthProvider extends Component {

    state = {
        isAuthenticated: false,
        token: null,
        methods: {
            login: (username, password) => this.login(username, password),
            logout: () => this.logout()
        }
    }

    login = (username, password) => {
        axios.post("/auth/login/", {
            username: username,
            password: password
        })
        .then(({data}) => {
            localStorage.setItem('token', data.token)
            this.setState({
                token: data.token,
                isAuthenticated: true
            })
        })
        .catch(e => console.log(e))
    }

    logout = () => {
        localStorage.removeItem('token')
        this.setState({
            isAuthenticated: false,
            token: ''
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
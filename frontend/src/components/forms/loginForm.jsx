import React, { Component } from 'react';
import { AuthContext } from '../../contexts/authContext';


class LoginForm extends Component {

    state = {
        username: "",
        password: ""
    }

    handlChange = (e) => {
        this.setState({
            [e.target.name]: e.target.value
        })
    }

    handleSubmit = (e) => {
        e.preventDefault()
        const {username, password} = this.state
        this.context.methods.login(username, password)
    }

    render() {
        return (
            <div className="card p-4">
                <div className="card-body">
                    <h5 className="card-title">Login</h5>
                    <hr />

                    <form onSubmit={this.handleSubmit}>
                        <div className="form-group">
                            <label htmlFor="username">Username</label>
                            <input
                                type="text"
                                name="username"
                                id="username"
                                onChange={this.handlChange}
                                required
                                className="form-control" />
                        </div>
                        <div className="form-group">
                        <label htmlFor="password">Password</label>
                            <input
                                type="password"
                                name="password"
                                id="password"
                                onChange={this.handlChange}
                                required
                                className="form-control" />
                        </div>

                        <input type="submit" value="Login" className="btn btn-secondary" />

                    </form>
                </div>
            </div>
        );
    }
}

LoginForm.contextType = AuthContext

export default LoginForm;
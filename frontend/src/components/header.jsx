import React from 'react';
import { AuthConsumer } from "../contexts/authContext";
import { Link, NavLink } from "react-router-dom";
import Loading from './loading'

const Header = () => {
    return (
        <AuthConsumer>
            {({ isAuthenticated, methods, loading }) => (
                
                <nav className="navbar navbar-expand-lg navbar-light bg-light">
                    <div className="container">
                        <Link className="navbar-brand" to="/">Project Manager</Link>
                        <button
                            className="navbar-toggler"
                            type="button"
                            data-toggle="collapse"
                            data-target="#navbarSupportedContent"
                            aria-controls="navbarSupportedContent"
                            aria-expanded="false"
                            aria-label="Toggle navigation">
                            <span className="navbar-toggler-icon"></span>
                        </button>

                        <div className="collapse navbar-collapse" id="navbarSupportedContent">
                            <ul className="navbar-nav ml-auto">
                                <li className="nav-item">
                                    <NavLink exact className="nav-link" to="/">Home</NavLink>
                                </li>
                                {isAuthenticated ? (
                                    <li className="nav-item">
                                        <span className="nav-link mouse-pointer" onClick={methods.logout}>Logout</span>
                                        {loading && <Loading />}
                                    </li>
                                ): (
                                    <li className="nav-item">
                                        <NavLink className="nav-link" to="/login">Login</NavLink>
                                    </li>
                                )}

                        </ul>
                        </div>
                    </div>
                </nav>
            )}

        </AuthConsumer>
    );
}

export default Header;
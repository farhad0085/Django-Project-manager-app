import React from 'react';
import { AuthConsumer } from "../contexts/authContext";

const Header = () => {
    return (
        <AuthConsumer>
            {({ isAuthenticated, methods }) => (
                
                <nav className="navbar navbar-expand-lg navbar-light bg-light">
                    <div className="container">
                        <a className="navbar-brand" href="?#">Project Manager</a>
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
                                <li className="nav-item active">
                                    <a className="nav-link" href="?#">Home <span className="sr-only">(current)</span></a>
                                </li>
                                {isAuthenticated ? (
                                    <li className="nav-item">
                                        <span className="nav-link" onClick={methods.logout}>Logout</span>
                                        
                                    </li>
                                ): (
                                    <li className="nav-item">
                                        <a className="nav-link" href="?#">Login</a>
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
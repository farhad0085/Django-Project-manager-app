import React from 'react';
import { Route, Switch } from "react-router-dom";
import Home from './components/home';
import LoginForm from "./components/forms/loginForm";

const SiteRouter = () => {
    return (
        <Switch>
            <Route path="/" exact component={Home} />
            <Route path="/login" component={LoginForm} />
        </Switch>
    )
}

export default SiteRouter
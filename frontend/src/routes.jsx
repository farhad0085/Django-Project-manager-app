import React from 'react';
import { Route, Switch } from "react-router-dom";
import Home from './components/home';
import LoginForm from "./components/forms/loginForm";
import ProjectDetail from './components/project-details'

const SiteRouter = () => {
    return (
        <Switch>
            <Route path="/" exact component={Home} />
            <Route path="/login" component={LoginForm} />
            <Route path="/project/:project_id" component={ProjectDetail} />
        </Switch>
    )
}

export default SiteRouter
import React from 'react';
import { Route, Switch } from "react-router-dom";
import Home from '../components/home';
import LoginForm from "../components/forms/loginForm";
import ProjectDetail from '../components/project-details'
import Board from '../pages/Board/Board';


const Routes = () => {
  return (
    <Switch>
      <Route path="/" exact component={Home} />
      <Route path="/login" component={LoginForm} />
      <Route path="/project/:project_id" component={ProjectDetail} />
      <Route path="/boards/:project_id" component={Board} />
    </Switch>
  )
}

export default Routes
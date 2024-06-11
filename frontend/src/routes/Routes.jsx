import React from 'react';
import { Route, Switch } from "react-router-dom";
import Home from '../components/home';
import LoginForm from "../components/forms/loginForm";
import Board from '../pages/Board/Board';
import NotFound from '../pages/Others/NotFound';
import * as URLS from './urls'
import AccessDenied from '../pages/Others/AccessDenied';
import GuestRoute from './GuestRoute';
import PrivateRoute from './PrivateRoute';


const Routes = () => {
  return (
    <Switch>
      <Route path="/" exact component={Home} />
      <GuestRoute path="/login" component={LoginForm} />
      <PrivateRoute exact path="/project/:project_id" component={Board} />

      <Route exact path={URLS.ACCESS_DENIED_PAGE} component={AccessDenied} />
      <Route component={NotFound} />
    </Switch>
  )
}

export default Routes
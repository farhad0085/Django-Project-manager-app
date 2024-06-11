import React from 'react';
import { Route, Switch } from "react-router-dom";
import Board from '../pages/Board/Board';
import NotFound from '../pages/Others/NotFound';
import * as URLS from './urls'
import AccessDenied from '../pages/Others/AccessDenied';
import GuestRoute from './GuestRoute';
import PrivateRoute from './PrivateRoute';
import Home from '../pages/Home/Home';
import Dashboard from '../pages/Dashboard/Dashboard';
import Login from '../pages/Auth/Login';


const Routes = () => {
  return (
    <Switch>
      <Route path={URLS.HOME} exact component={Home} />
      <GuestRoute path={URLS.LOGIN_PAGE} component={Login} />
      <PrivateRoute path={URLS.DASHBOARD} component={Dashboard} />
      <PrivateRoute exact path="/project/:project_id" component={Board} />

      <Route exact path={URLS.ACCESS_DENIED_PAGE} component={AccessDenied} />
      <Route component={NotFound} />
    </Switch>
  )
}

export default Routes
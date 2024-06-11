import React, { useContext } from "react";
import { Route, Redirect } from "react-router-dom";
import { LOGIN_PAGE } from "./urls";
import { AuthContext } from '../contexts/authContext'


const PrivateRoute = ({ component: Component, ...rest }) => {
  const { isAuthenticated } = useContext(AuthContext)

  return (
    <Route
      {...rest}
      render={(props) => {
        return (
          <>
            {isAuthenticated ? (
              <Component {...props} />
            ) : (
              <Redirect
                to={{
                  pathname: LOGIN_PAGE,
                  state: { from: props.location },
                }}
              />
            )}
          </>
        );
      }}
    />
  );
};

export default PrivateRoute;

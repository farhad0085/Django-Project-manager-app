import React from 'react';


const ErrorMessage = ({message}) => {
    return (
        <div className="d-flex justify-content-center">
            <p className="text-danger">{message}</p>
        </div>
    );
}
 
export default ErrorMessage;
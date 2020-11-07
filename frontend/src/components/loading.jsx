import { BeatLoader } from 'react-spinners'
import React from 'react';

const Loading = ({ size, color, noClass }) => {

    const spinnerColor = color ? color : "#123abc"
    
    if (noClass){console.log("here");
        return <BeatLoader size={size} color={spinnerColor} />
    }
    
    return (
        <div className="d-flex justify-content-center">
            <BeatLoader size={size} color={spinnerColor} />
        </div>
    )
}


export default Loading
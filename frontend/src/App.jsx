import React from 'react';
import Home from './components/home'
import Header from './components/header'
import SiteRouter from './routes'
import { AuthProvider } from './contexts/authContext'


const App = () => {

    return (
        <AuthProvider>
            <Header />
            <div className="container my-4">
                <SiteRouter>
                    <Home />
                </SiteRouter>
            </div>
        </AuthProvider>
    );
}

export default App;

import React from 'react';
import Home from './components/home'
import Header from './components/header'
import SiteRouter from './routes'
import { AuthProvider } from './contexts/authContext'
import { ProjectProvider } from './contexts/projectContext'


const App = () => {

    return (
        <AuthProvider>
            <Header />
            <div className="container my-4">
                <ProjectProvider>
                    <SiteRouter>
                        <Home />
                    </SiteRouter>
                </ProjectProvider>
            </div>
        </AuthProvider>
    );
}

export default App;

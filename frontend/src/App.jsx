import React from 'react';
import { AuthConsumer, AuthProvider } from './contexts/authContext'
import { ProjectProvider } from './contexts/projectContext'

import Header from './components/header'
import Projects from './components/projects'
import LoginForm from './components/forms/loginForm'



const App = () => {

    return (
        <AuthProvider>
            <Header />
            <AuthConsumer>
                {({isAuthenticated}) => (
                    <div className="container my-4">
                        {isAuthenticated ? (
                            <ProjectProvider>
                                <Projects />
                            </ProjectProvider>
                        ):(
                            <LoginForm />
                        )}
                        
                    </div>
                )}
            </AuthConsumer>
        </AuthProvider>
    );
}

export default App;

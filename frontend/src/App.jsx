import React from 'react';
import { AuthProvider } from './contexts/authContext'
import { ProjectProvider } from './contexts/projectContext'
import Routes from './routes/Routes';


const App = () => {

  return (
    <AuthProvider>
      <ProjectProvider>
        <Routes />
      </ProjectProvider>
    </AuthProvider>
  );
}

export default App;

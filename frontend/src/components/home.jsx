import { AuthConsumer } from '../contexts/authContext'
import { ProjectProvider } from '../contexts/projectContext'

import Projects from './projects'
import LoginForm from './forms/loginForm'


const Home = () => (
    <AuthConsumer>
        {({ isAuthenticated }) => (

            <>
                {isAuthenticated ? (
                    <ProjectProvider>
                        <Projects />
                    </ProjectProvider>
                ) : (
                        <LoginForm />
                    )}

            </>
        )}
    </AuthConsumer>
)

export default Home
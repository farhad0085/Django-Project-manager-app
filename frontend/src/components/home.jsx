import { AuthContext } from '../contexts/authContext'

import Projects from './projects'
import LoginForm from './forms/loginForm'
import { useContext } from 'react'


const Home = () => {
    const { isAuthenticated } = useContext(AuthContext)
    return (
        <>
            {isAuthenticated ? (
                <Projects />
            ) : (
                    <LoginForm />
                )}

        </>
    )
}

export default Home
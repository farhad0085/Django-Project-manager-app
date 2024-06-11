import React, { useContext, useState } from 'react'
import { AuthContext } from '../../contexts/authContext'
import ErrorMessage from '../../components/errorMsg'
import Loading from '../../components/loading'
import styles from './styles.module.scss'
import AuthLayout from '../../layouts/AuthLayout'


const Login = () => {

  const { methods, loading, error } = useContext(AuthContext)
  const [username, setUsername] = useState('')
  const [password, setPassword] = useState('')

  const handleSubmit = (e) => {
    e.preventDefault()
    methods.login(username, password)
  }

  return (
    <AuthLayout>
      <div className={styles.container}>
        <form onSubmit={handleSubmit} className={styles.card}>
          <h2 className={styles.cardTitle}>Login</h2>
          <hr />
          <div className="form-group">
            <label htmlFor="username">Username</label>
            <input
              type="text"
              name="username"
              id="username"
              onChange={e => setUsername(e.target.value)}
              required
              className="form-control" />
          </div>
          <div className="form-group">
            <label htmlFor="password">Password</label>
            <input
              type="password"
              name="password"
              id="password"
              onChange={e => setPassword(e.target.value)}
              required
              className="form-control" />
          </div>
          <button type="submit" className={styles.button}>
            {loading ? <Loading size='10px' color="#ffffff" /> : "Login"}
          </button>
          {error && <ErrorMessage message={error} />}
        </form>
      </div>
    </AuthLayout>
  )

}


export default Login
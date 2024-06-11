import React, { useContext } from 'react'
import Layout from '../../layouts/Layout'
import { AuthContext } from '../../contexts/authContext'
import styles from './styles.module.scss'
import { DASHBOARD, LOGIN_PAGE } from '../../routes/urls'
import { useHistory } from 'react-router-dom'


const Home = () => {
  const history = useHistory()
  const { isAuthenticated } = useContext(AuthContext)

  return (
    <Layout>

      <div className={styles.container}>
        <h1 className={styles.title}>Welcome to Trello Board</h1>

        {isAuthenticated ? (
          <button onClick={() => history.push(DASHBOARD)} className={styles.button}>View Dashboard</button>
        ) : (
          <button onClick={() => history.push(LOGIN_PAGE)} className={styles.button}>Login now</button>
        )}
      </div>
    </Layout>
  )

}


export default Home
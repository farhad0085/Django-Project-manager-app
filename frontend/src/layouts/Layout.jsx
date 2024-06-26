import React, { useContext } from 'react'
import { useHistory } from 'react-router-dom'
import { HOME } from '../routes/urls'
import { AuthContext } from '../contexts/authContext'


const Layout = ({ children }) => {

  const { isAuthenticated, methods } = useContext(AuthContext)

  const history = useHistory()

  return (
    <>
      <header className="masthead">
        <div className="boards-menu">
          <button className="boards-btn btn"><i className="fab fa-trello boards-btn-icon"></i>Boards</button>
          <div className="board-search">
            <input type="search" className="board-search-input" aria-label="Board Search" />
            <i className="fas fa-search search-icon" aria-hidden="true"></i>
          </div>
        </div>

        <div className="logo">
          <h1 onClick={() => history.push(HOME)}><i className="fab fa-trello logo-icon" aria-hidden="true"></i>Trello</h1>
        </div>

        <div className="user-settings">
          <button className="user-settings-btn btn" aria-label="Create">
            <i className="fas fa-plus" aria-hidden="true"></i>
          </button>

          <button className="user-settings-btn btn" aria-label="Information">
            <i className="fas fa-info-circle" aria-hidden="true"></i>
          </button>

          <button className="user-settings-btn btn" aria-label="Notifications">
            <i className="fas fa-bell" aria-hidden="true"></i>
          </button>

          {isAuthenticated ? (
            <button className="user-settings-btn btn" onClick={methods.logout} aria-label="User Settings">
              <i className="fas fa-sign-out-alt" aria-hidden="true"></i>
            </button>
          ) : (
            <button className="user-settings-btn btn" aria-label="User Settings">
              <i className="fas fa-key" aria-hidden="true"></i>
            </button>
          )}
        </div>
      </header>

      {children}
    </>
  )

}


export default Layout
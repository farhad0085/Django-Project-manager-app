import React, { useEffect, useState } from 'react'
import './styles.css'
import { useParams } from 'react-router-dom'
import Project from '../../classes/project'
import Layout from '../../layouts/Layout'


const Board = () => {
  const [projectState, setProjectState] = useState({})
  const { project_id } = useParams()

  console.log(projectState)

  useEffect(() => {
    const project = new Project()
    project.getBoard(project_id)
      .then(data => {
        setProjectState(data)
      })
      .catch(err => console.log(err))

    // eslint-disable-next-line
  }, [project_id])

  return (
    <Layout>
      {/* <!-- Board info bar --> */}
      <section className="board-info-bar">

        <div className="board-controls">

          <button className="board-title btn">
            <h2>{projectState.title}</h2>
          </button>

          <button className="star-btn btn" aria-label="Star Board">
            <i className="far fa-star" aria-hidden="true"></i>
          </button>

          <button className="personal-btn btn">Personal</button>

          <button className="private-btn btn"><i className="fas fa-briefcase private-btn-icon" aria-hidden="true"></i>Private</button>

        </div>

        <button className="menu-btn btn"><i className="fas fa-ellipsis-h menu-btn-icon" aria-hidden="true"></i>Show Menu</button>

      </section>
      {/* <!-- End of board info bar --> */}

      {/* <!-- Lists container --> */}
      <section className="lists-container">

        <div className="list">

          <h3 className="list-title">Tasks to Do</h3>

          <ul className="list-items">
            <li>Complete mock-up for client website</li>
            <li>Email mock-up to client for feedback</li>
            <li>Update personal website header background image</li>
            <li>Update personal website heading fonts</li>
            <li>Add google map to personal website</li>
            <li>Begin draft of CSS Grid article</li>
            <li>Read new CSS-Tricks articles</li>
            <li>Read new Smashing Magazine articles</li>
            <li>Read other bookmarked articles</li>
            <li>Look through portfolios to gather inspiration</li>
            <li>Create something cool for CodePen</li>
            <li>Post latest CodePen work on Twitter</li>
            <li>Listen to new Syntax.fm episode</li>
            <li>Listen to new CodePen Radio episode</li>
          </ul>

          <button className="add-card-btn btn">Add a card</button>

        </div>

        <div className="list">

          <h3 className="list-title">Completed Tasks</h3>

          <ul className="list-items">
            <li>Clear email inbox</li>
            <li>Finalise requirements for client web design</li>
            <li>Begin work on mock-up for client website</li>
          </ul>

          <button className="add-card-btn btn">Add a card</button>

        </div>

        <div className="list">

          <h3 className="list-title">Topics/Concepts to Revise</h3>

          <ul className="list-items">
            <li>HTML Elements</li>
            <li>HTML Form Validation</li>
            <li>HTML Structured Data</li>
            <li>Advanced CSS Selectors</li>
            <li>CSS Transforms</li>
            <li>CSS Animations</li>
            <li>CSS Flexbox</li>
            <li>CSS Grid</li>
            <li>CSS Methodologies (BEM, SMACSS etc.)</li>
            <li>SASS/SCSS</li>
            <li>Layout Fallbacks</li>
            <li>Responsive Design</li>
            <li>Design Patterns</li>
            <li>JavaScript Fundamentals</li>
            <li>JavaScript OOP</li>
            <li>JavaScript DOM Manipulation</li>
            <li>JavaScript Debugging Techniques</li>
            <li>Node Package Manager</li>
            <li>Grunt/Gulp</li>
            <li>GitHub</li>
            <li>Git Commands</li>
            <li>Web Accessibility</li>
            <li>Web Performance</li>
            <li>Web Hosting</li>
            <li>Browser Dev Tools</li>
            <li>Google Analytics</li>
            <li>Basic Photoshop/Sketch Usage</li>
          </ul>

          <button className="add-card-btn btn">Add a card</button>

        </div>

        <div className="list">

          <h3 className="list-title">Topics/Concepts to Learn</h3>

          <ul className="list-items">
            <li>HTML 5.2 New Features</li>
            <li>Responsive Images (picture element, srcset/sizes etc.)</li>
            <li>Serverless</li>
            <li>Variable Fonts</li>
            <li>Shadow DOM</li>
            <li>ES6+</li>
            <li>JSON & AJAX</li>
            <li>API's</li>
            <li>JavaScript Patterns</li>
            <li>JavaScript Testing</li>
            <li>jQuery</li>
            <li>SVG</li>
            <li>React JS</li>
            <li>Angular JS</li>
            <li>TypeScript</li>
            <li>Vue JS</li>
            <li>Node JS</li>
            <li>Webpack</li>
            <li>SEO Techniques</li>
            <li>HTML Emails</li>
            <li>WordPress</li>
            <li>Static Site Generators (Jekyll, Hugo, Gatsby etc.)</li>
          </ul>

          <button className="add-card-btn btn">Add a card</button>

        </div>

        <button className="add-list-btn btn">Add a list</button>

      </section>
    </Layout>
  )

}


export default Board
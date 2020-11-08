import React, { useContext, useState } from 'react';
import { ProjectContext } from '../contexts/projectContext'
import Loading from "./loading"
import ErrorMsg from './errorMsg'
import { Link } from 'react-router-dom'
import CreateProjectForm from './forms/projectCreateForm'


const NewButton = ({onClick}) => (
    <div onClick={onClick} className="col-md-12 col-xl-4 my-2">
        <div className="card shadow-nohover new-project mouse-pointer" title="Add new project">
            <div className="card-block p-5">
                <div className="row align-items-center justify-content-center">
                    <p>
                        <i className="fas fa-plus-circle fa-6x"></i>
                    </p>
                </div>
            </div>
        </div>
    </div>
)


const Project = ({ project }) => {
    const projectDetailsUrl = `/project/${project.id}`
    return (
        <div className="col-md-12 col-xl-4 my-2">
            <div className="card shadow-nohover">
                <div className="card-body">
                    <div className="card-title">
                        <h5><Link className="card-link" to={projectDetailsUrl}>{project.title}</Link></h5>
                        <hr />
                    </div>
                    <p>
                        {project.description ? project.description.slice(0, 200) : "No description available"}
                    </p>
                </div>
            </div>
        </div>
    )
}


const Projects = () => {
    const [newProjectBtn, setNewProjectBtn] = useState(false)
    const { projects, count, loading, error } = useContext(ProjectContext)
    return (
        <>
            <h4>Projects ({count})</h4>
            <hr />
            <ErrorMsg message={error} />
            {loading ? <Loading /> : (
                <div className="row">

                    {/* Add new project button */}
                    <NewButton onClick={() => setNewProjectBtn(!newProjectBtn)}/>
                    {newProjectBtn && <CreateProjectForm />}

                    {projects.map(project => <Project key={project.id} project={project} />)}
                </div>
            )}
           
        </>
    );
}

export default Projects;

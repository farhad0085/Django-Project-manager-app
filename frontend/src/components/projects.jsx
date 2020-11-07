import React, { useContext } from 'react';
import { ProjectProvider, ProjectContext } from '../contexts/projectContext'
import Loading from "./loading"
import ErrorMsg from './errorMsg'
import { Link } from 'react-router-dom'
import CreateProjectForm from './forms/projectCreateForm'



const Project = ({ project }) => {
    const projectDetailsUrl = `/project/${project.id}`
    return (
        <div className="col-md-4 col-xl-4 my-2">
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
    const { projects, count, loading, error } = useContext(ProjectContext)
    return (
        <ProjectProvider>
            <CreateProjectForm />
            <h4>Projects {count}</h4>
            <hr />
            <ErrorMsg message={error} />
            {loading ? <Loading /> : (
                <div className="row">
                    {projects.map(project => <Project key={project.id} project={project} />)}
                </div>
            )}

        </ProjectProvider>
    );
}

export default Projects;

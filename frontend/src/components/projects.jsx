import React from 'react';
import { ProjectConsumer, ProjectProvider } from '../contexts/projectContext'
import Loading from "./loading"
import ErrorMsg from './errorMsg'
import { Link } from 'react-router-dom'



const Project = ({ project }) => {
    const projectDetailsUrl = `/project/${project.id}`
    return (
        <div className="col-md-4 col-xl-4 my-2">
            <div className="card">
                <div className="card-body">
                    <div className="card-title">
                        <h5><Link to={projectDetailsUrl}>{project.title}</Link></h5>
                        <hr />
                    </div>
                    <p>
                        {project.description ? project.description : "No description available"}
                    </p>
                </div>
            </div>
        </div>
    )
}


const Projects = () => {

    return (
        <ProjectProvider>
            <ProjectConsumer>
                {({ projects, count, loading, error }) => {
                    return (
                        <>
                            <h2>Projects {count}</h2>
                            <hr />
                            <ErrorMsg message={error} />
                            {loading ? <Loading /> : (
                                <div className="row">
                                    {projects.map(project => <Project key={project.id} project={project} />)}
                                </div>
                            )}
                        </>
                    )
                }}

            </ProjectConsumer>
        </ProjectProvider>
    );
}

export default Projects;

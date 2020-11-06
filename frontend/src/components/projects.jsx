import React from 'react';
import { ProjectConsumer } from '../contexts/projectContext'


const Project = ({ project }) => {
    return (
        <div className="col-md-4 col-xl-4 my-2">
            <div className="card">
                <div className="card-body">
                    <div className="card-title">
                        <h5>{project.title}</h5>
                        <hr/>
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
        <ProjectConsumer>
            {({ projects, count }) => {
                return (
                    <>
                        <h2>Projects ({count})</h2>
                        <hr />
                        <div className="row">
                            {projects.map(project => <Project key={project.id} project={project} />)}
                        </div>
                    </>
                )
            }}

        </ProjectConsumer>
    );
}

export default Projects;

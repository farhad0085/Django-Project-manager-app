import React, { useContext } from 'react';
import { useParams } from 'react-router-dom'
import { ProjectContext } from '../contexts/projectContext';
import Card from './card'

const ProjectDetail = () => {

    // get project_id from URL
    let { project_id } = useParams();
    project_id = parseInt(project_id)

    let { activeProject, getSingleProject } = useContext(ProjectContext)
    
    // projects = getSingleProject()
    // console.log(projects);
    getSingleProject(project_id)
    // const project = projects.find(project => project.id === project_id)
    const project = activeProject
    console.log(project);
    return (
        <>
            <h3>Project - {project.title}</h3>
            <p className="text-muted">{project.description}</p>
            <hr />
            <div className="row">
                {project.card_set.map(card => <Card key={card.id} card={card} />)}
            </div>
        </>
    );
}

export default ProjectDetail;
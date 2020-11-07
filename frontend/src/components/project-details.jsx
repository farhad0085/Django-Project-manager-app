import React from 'react';
import { useParams } from 'react-router-dom'
import { ProjectConsumer } from '../contexts/projectContext';
import Card from './card'

const ProjectDetail = () => {

    // get project_id from URL
    let { project_id } = useParams();
    project_id = parseInt(project_id)

    return (
        <ProjectConsumer>
            {({ projects }) => {
                const project = projects.find(project => project.id === project_id)

                return (
                    <>
                        <h3>Project - {project.title}</h3>
                        <p className="text-muted">{project.description}</p>
                        <hr />
                        <div className="row">
                            {project.card_set.map(card => <Card card={card} />)}
                        </div>
                    </>
                )

            }}
        </ProjectConsumer>
    );
}

export default ProjectDetail;
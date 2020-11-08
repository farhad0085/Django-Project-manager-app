import React, { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom'
import Card from './card'
import Project from '../classes/project'

const project = new Project()

const ProjectDetail = () => {

    const [projectState, setProjectState] = useState({})
    // get project_id from URL
    let { project_id } = useParams();
    project_id = parseInt(project_id)
    

    // useEffect(() => {
    //     setProjectState({ id: project_id })
    //     console.log("Called");
    //     project.getOneProject(project_id)
    //         .then(data => {
    //             console.log(data);
    //             if (data.id !== projectState.id) {
    //                 setProjectState(data)
    //             }
    //         })
    //         .catch(err => console.log(err))
    // })


    return (
        <>
            <h3>Project - {projectState.title}</h3>
            <p className="text-muted">{projectState.description}</p>
            <hr />
            <div className="row">
                {/* {projectState.card_set.map(card => <Card key={card.id} card={card} />)} */}
            </div>
        </>
    );
}

export default ProjectDetail;
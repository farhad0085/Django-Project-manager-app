import React, { useState, useContext } from 'react';
import { ProjectContext } from '../../contexts/projectContext';
import Loading from '../loading'
import ErrorMsg from '../errorMsg'
import { useHistory } from "react-router-dom";


const CreateProjectForm = () => {
    const [title, setTitle] = useState('')
    const [description, setDescription] = useState('')
    const [error, setError] = useState(null)
    const [loading, setLoading] = useState(false)

    let history = useHistory();

    const { createProject } = useContext(ProjectContext)

    const submitHandler = e => {
        e.preventDefault()
        setLoading(true)
        setError('')
        createProject(title, description)
            .then(data => {
                console.log("Data", data);
                setLoading(false)
                setTitle('')
                setDescription('')
                history.push(`/project/${data.id}`)
            })
            .catch(err => {
                console.log(err);
                setLoading(false)
                setError("Failed to create new project")
            })
    }

    return (
        <div className="col-md-12 col-xl-4 my-2">
            <div className="card shadow-nohover p-4">
                <form onSubmit={submitHandler}>
                    <div className="form-group">
                        <input type="text" required onChange={e => setTitle(e.target.value)} value={title} className="form-control" />
                    </div>
                    <div className="form-group">
                        <textarea value={description} onChange={e => setDescription(e.target.value)} className="form-control" />
                    </div>
                    <button className="btn btn-primary">{loading ? <Loading size='10px' color="#ffffff" /> : "Create"}</button>
                    {error && <ErrorMsg message={error} />}
                </form>
            </div>
        </div>
    )

}

export default CreateProjectForm
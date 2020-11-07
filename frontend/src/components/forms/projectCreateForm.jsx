import React, { useState, useContext } from 'react';
import { ProjectContext } from '../../contexts/projectContext';
import Loading from '../loading'

const CreateProjectForm = () => {
    const [title, setTitle] = useState('')
    const [description, setDescription] = useState('')
    // const [error, setError] = useState(null)
    const [loading, setLoading] = useState(false)

    const { createProject } = useContext(ProjectContext)

    const submitHandler = e => {
        e.preventDefault()
        setLoading(true)
        createProject(title, description)
            .then(data => {
                console.log(data);
                setLoading(false)
            })
            .catch(err => {
                console.log(err);
                setLoading(false)
            })
    }

    return (
        <div className="card p-4">
            <form onSubmit={submitHandler}>
                <div className="form-group">
                    <input type="text" required onChange={e => setTitle(e.target.value)} value={title} className="form-control" />
                </div>
                <div className="form-group">
                    <textarea value={description} onChange={e => setDescription(e.target.value)} className="form-control" />
                </div>
                <button className="btn btn-primary">{loading ? <Loading size='10px' color="#ffffff" /> : "Create"}</button>
            </form>
        </div>
    )

}

export default CreateProjectForm
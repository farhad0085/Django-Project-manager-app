import React, { Component, createContext } from 'react';
import axios from '../utils/axios'
import { getHeaders } from '../utils'


let Context = null

const { Provider, Consumer } = Context = createContext()


class ProjectProvider extends Component {

    state = {
        count: 0,
        next: null,
        previous: null,
        projects: [],
        loading: true,
        error: null,
        createProject: (title, description) => this.createProject(title, description),
        getSingleProject: (boardId) => this.getSingleProject(boardId),
    }

    createProject = async (title, description) => {
        try {
            const { data } = await axios.post("/projects/", {
                title,
                description
            }, { headers: getHeaders() })

            this.getBoards()

            return data
        }
        catch (e) {
            throw new Error(e)
        }
    }

    getBoards = () => {
        axios.get("/projects/", { headers: getHeaders() })
            .then(({ data }) => this.setState({
                count: data.count,
                next: data.next,
                previous: data.previous,
                projects: data.results,
                loading: false
            }))
            .catch(e => {
                console.log(e)
                this.setState({ loading: false, error: "Failed to load projects at this moment. Please try again later!" })
            })
    }

    getSingleProject = async(boardId) => {

            // this.setState({ loading: true })
            try {
                const {data } = await axios.get(`/projects/${boardId}/`, { headers: getHeaders() })
                // this.setState({loading: false})
                return data
            }
            catch {
                // this.setState({ loading: false, error: "Failed to load the project!" })
                throw new Error("Failed to load")
            }
    }

    componentDidMount() {
        this.getBoards()
    }

    render() {
        return (
            <Provider value={this.state}>
                {this.props.children}
            </Provider>
        );
    }
}

export { ProjectProvider, Consumer as ProjectConsumer, Context as ProjectContext }
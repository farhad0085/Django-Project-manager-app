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
        activeProject: {},
        createProject: (title, description) => this.createProject(title, description),
        getSingleProject: (projectId) => this.getSingleProject(projectId),
    }

    createProject = async (title, description) => {
        try {
            const { data } = await axios.post("/projects/", {
                title,
                description
            }, { headers: getHeaders() })

            this.getProjects()

            return data
        }
        catch (e) {
            throw new Error(e)
        }
    }

    getProjects = () => {
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

    getSingleProject = (projectId) => {

        this.setState({ loading: true })

        axios.get(`/projects/${projectId}/`, { headers: getHeaders() })
            .then(({ data }) => {
                console.log(data);
                this.setState({
                    ...this.state,
                    activeProject: {...data},
                    loading: false
                }, () => console.log("activeProject", this.state.activeProject))
            })
            .catch(e => {
                console.log(e)
                this.setState({ loading: false, error: "Failed to load projects at this moment. Please try again later!" })
            })
    }

    componentDidMount() {
        this.getProjects()
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
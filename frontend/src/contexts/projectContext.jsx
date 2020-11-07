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
        error: null
    }

    getProjects = () => {
        axios.get("/projects/", {headers: getHeaders()})
        .then(({data}) => this.setState({
            count: data.count,
            next: data.next,
            previous: data.previous,
            projects: data.results,
            loading: false
        }))
        .catch(e => {
            console.log(e)
            this.setState({loading: false, error: "Failed to load projects at this moment. Please try again later!"})
        })
    }

    componentDidMount(){
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
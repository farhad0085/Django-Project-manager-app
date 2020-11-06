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
        projects: []
    }

    getProjects = () => {
        axios.get("/projects/", {headers: getHeaders()})
        .then(({data}) => this.setState({
            count: data.count,
            next: data.next,
            previous: data.previous,
            projects: data.results,
        }))
        .catch(e => console.log(e))
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
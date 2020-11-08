import axios from '../utils/axios'
import { getHeaders } from '../utils/index'

class Project {
    constructor() {
        this.projectId = null
        this.totalProject = 0
        this.headers = getHeaders()
    }

    async getProjects() {

        try {
            const { data } = await axios.get("/projects", { headers: this.headers })
            return data
        }
        catch {
            throw new Error("Error loading projects")
        }
    }

    async getOneProject(id) {

        try {
            const { data } = await axios.get(`/projects/${id}`, { headers: this.headers })
            return data
        }
        catch {
            throw new Error("Error loading projects")
        }
    }

}

export default Project
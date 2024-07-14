import axios from '../utils/axios'
import { getHeaders } from '../utils/index'

class Project {
    constructor() {
        this.boardId = null
        this.headers = getHeaders()
    }

    async getBoards() {

        try {
            const { data } = await axios.get("/boards", { headers: this.headers })
            return data
        }
        catch {
            throw new Error("Error loading boards")
        }
    }

    async getBoard(id) {

        try {
            const { data } = await axios.get(`/boards/${id}`, { headers: this.headers })
            return data
        }
        catch {
            throw new Error("Error loading board")
        }
    }

}

export default Project
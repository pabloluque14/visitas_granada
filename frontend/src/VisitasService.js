import axios from 'axios';
const API_URL = 'http://127.0.0.1:8000/visitas_granada/api/visitas/';

export default class VisitasService{
	
    constructor(){}
    
	getVisita(pk) {
		const url = `${API_URL}/${pk}`;
		return axios.get(url).then(response => response.data);
    }
    
    getVisitas(){
        const url = `${API_URL}`;
		return axios.get(url).then(response => response.data);

    }

	
}
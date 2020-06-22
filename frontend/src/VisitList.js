import React, { Component } from 'react';
import VisitasService from './VisitasService';

const visitasService = new VisitasService();

class VisitList extends Component {
  
  constructor(props) {
    super(props);

    this.state = {
      visitas: [],
    };

    
  }  
  componentDidMount() {
    var self = this;
    visitasService.getVisitas().then(function (result) {
      console.log(result);
      self.setState({ visitas: result.data})
    });
  }

  
  render() {
    return (
      <div className="customers--list">
          <table className="table">
          <thead key="thead">
          <tr>
            <th>#</th>
            <th>Nombre</th>
            <th>Descripcion</th>
            <th>Likes</th> 
          </tr>
          </thead>

            <tbody>
            {this.state.visitas.map( vi =>

              <tr key={vi.pk}>
                <td>{vi.pk} </td>
                <td>{vi.nombre}</td>
                <td>{vi.descripción}</td>
                <td>{vi.likes}</td>
                
              </tr>)}
              </tbody>
          </table>

      </div>
    );
  }
}

export default VisitList;
import React, { Component } from 'react';

class Detail extends Component {
  state = {
    visitas: []
  };

  async componentDidMount() {
    try {
      const res = await fetch('http://127.0.0.1:8000/visitas_granada/api/visitas/');
      const visitas = await res.json();
      this.setState({
        visitas
      });
    } catch (e) {
      console.log(e);
    }
  }

  render() {
    return (
      <div>
        {this.state.visitas.map(item => (
          <div key={item.id}>
            <h1>{item.nombre}</h1>
            <span>{item.descripción}</span>
            <li>{item.likes}</li>
            
          </div>
        ))}
      </div>
    );
  }
}


export default Detail;
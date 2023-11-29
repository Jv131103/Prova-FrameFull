import React, { useState } from 'react';

function Produto() {

  var id = 3;
  const [name, setName] = useState('');
  const [celular, setCelular] = useState('');  
  const [result, setResult] = useState('');  

  const setNameChange = (e) => {
    setName(e.target.value);
  };

  const setCelularChange = (e) => {
    setCelular(e.target.value);
  };

  const CadastroSubmit = (e) => {
    e.preventDefault();

    id=id+1;
  
    var myHeaders = new Headers();
    myHeaders.append("Content-Type", "application/json");

    var raw = JSON.stringify({
      "id": id,
      "name": name,
      "celular": celular
    });

    var dados = {
      method: 'POST',
      headers: myHeaders,
      body: raw,
      redirect: 'follow'
    };

    fetch("http://127.0.0.1:5000/produtos", dados)
      .then(response => response.text())
      .then(result => setResult(result))
      .catch(error => console.log('error', error));

  };

  return (
    <div className="login-container">
      <h2>Cadastro Produto</h2>
      <form onSubmit={CadastroSubmit} className="login-form">
        <label>
          Nome do Produto:
          <input type="text" value={name} onChange={setNameChange} />
        </label>
        <br />
        <label>
          Celular:
          <input type="text" value={celular} onChange={setCelularChange} />
        </label>
        <br />
        <button type="submit">Cadastrar</button>        
      </form> 
      {result}     
    </div>
  );
};

export default Produto;
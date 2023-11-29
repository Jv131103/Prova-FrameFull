import React, { useState, useEffect } from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';

function Login() {

  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');

  const setEmailChange = (e) => {
    setEmail(e.target.value);
  };

  const setPasswordChange = (e) => {
    setPassword(e.target.value);
  };

  const LoginSubmit = (e) => {
    e.preventDefault();

    // Validate password length
    if (password.length < 4) {
      alert('A senha precisa ter 4 digito');
      return false;
    }

    // Fetch users from Flask API
    const fetchUsersAPI = 'http://localhost:5000/api/users';

    // Fetch users from the API
    fetch(fetchUsersAPI)
      .then((response) => response.json())
      .then((data) => {
        const users = data.data;
        let valor = false;
        users.forEach(element => {
          //console.log(element)
          if (email === element.email){
            //console.log(element.email)
            if (password === element.senha){
              //console.log(element.senha)
              valor = true;
            }
          }
      });
      if (valor === true){
        alert("Usuário logado com sucesso")
      }else{
        alert("Usuário não reconhecido")
      }
      })
      .catch((error) => {
        console.error(error);
        alert('Erro ao conectar com o servidor');
        return false;
  });

};
  return (
    <div className="login-container">
      <h2>Login</h2>
      <form onSubmit={LoginSubmit} className="login-form">
        <label>
          Email:
          <input type="email" value={email} onChange={setEmailChange} />
        </label>
        <br />
        <label>
          Senha:
          <input type="password" value={password} onChange={setPasswordChange} />
        </label>
        <br />
        <button type="submit">Entrar</button>
      </form>
    </div>
  );
};
export default Login;
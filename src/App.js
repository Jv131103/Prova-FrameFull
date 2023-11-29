import React from 'react';
import { BrowserRouter as Router, Routes, Route, Link } from 'react-router-dom';
import Produto from './componentes/Produto';
import Login from './componentes/Log';

const App = () => {
  return (
    <Router>
      <div>
        <nav>
          <ul>
            
            <li>
              <Link to="/Login">Login</Link>
            </li>
            <li>
              <Link to="/cadastar-produto">Cadastro de produto</Link>
            </li>
          </ul>
        </nav>

        <hr />

        <Routes>
          <Route path="/Login" element={<Login />} />
          <Route path="/cadastar-produto" element={<Produto />} />          
        </Routes>
      </div>
    </Router>
  );
};

export default App;
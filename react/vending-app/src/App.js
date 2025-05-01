import React, { useState, useEffect } from 'react';
import api from './api'; // Asegúrate de que api.js tenga baseURL correcta (ej: http://localhost:8000)

const App = () => {
  // 1. Estados para almacenar máquinas y controlar carga/errores
  const [maquinas, setMaquinas] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  // 2. Obtener máquinas al cargar el componente
  useEffect(() => {
    const fetchMaquinas = async () => {
      try {
        const response = await api.get('/maquinas/'); // Ruta coincide con tu FastAPI
        setMaquinas(response.data);
      } catch (err) {
        setError("Error al cargar máquinas: " + err.message);
      } finally {
        setLoading(false);
      }
    };
    fetchMaquinas();
  }, []); // Se ejecuta solo al inicio

  // 3. Renderizado
  return (
    <div style={{ padding: '20px', fontFamily: 'Arial' }}>
      <h1>Máquinas Expendedoras</h1>
      
      {loading ? (
        <p>Cargando...</p>
      ) : error ? (
        <p style={{ color: 'red' }}>{error}</p>
      ) : (
        <ul style={{ listStyle: 'none', padding: 0 }}>
          {maquinas.map((maquina) => (
            <li 
              key={maquina.id}
              style={{ 
                margin: '10px 0', 
                padding: '15px', 
                border: '1px solid #ddd',
                borderRadius: '5px',
                backgroundColor: '#f9f9f9'
              }}
            >
              <h3>{maquina.name}</h3>
              <p><strong>ID:</strong> {maquina.id}</p>
              <p><strong>Ubicación:</strong> {maquina.ubication}</p>
            </li>
          ))}
        </ul>
      )}
    </div>
  );
};

export default App;
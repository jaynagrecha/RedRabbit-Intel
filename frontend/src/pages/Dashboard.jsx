// src/pages/Dashboard.jsx
import React, { useEffect, useState } from 'react';
import axios from 'axios';

const Dashboard = () => {
  const [iocs, setIocs] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchIOCs = async () => {
      try {
        const res = await axios.get(`${import.meta.env.VITE_API_BASE_URL}/api/ioc/all`);
        setIocs(res.data);
      } catch (err) {
        console.error('Error fetching IOCs:', err);
      } finally {
        setLoading(false);
      }
    };
    fetchIOCs();
  }, []);

  return (
    <div className="p-6 bg-gray-100 min-h-screen">
      <h1 className="text-3xl font-bold mb-6">Red Rabbit Intelligence Dashboard</h1>
      {loading ? (
        <p>Loading IOCs...</p>
      ) : (
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
          {iocs.map((ioc, index) => (
            <div
              key={index}
              className="bg-white rounded-xl shadow-md p-4 border border-gray-200 hover:shadow-lg transition"
            >
              <h2 className="text-xl font-semibold">{ioc.indicator}</h2>
              <p className="text-sm text-gray-600">Type: {ioc.type}</p>
              <p className="text-sm text-gray-600">Source: {ioc.source}</p>
            </div>
          ))}
        </div>
      )}
    </div>
  );
};

export default Dashboard;
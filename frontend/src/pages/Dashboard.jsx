import React from 'react';

const Dashboard = () => {
  return (
    <div className="p-6">
      <h1 className="text-2xl font-bold mb-4">Red Rabbit Intelligence</h1>
      <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
        <div className="bg-white p-4 rounded shadow">
          <h2 className="font-semibold">IOC Feed</h2>
          <p>Live view of indicators of compromise.</p>
        </div>
        <div className="bg-white p-4 rounded shadow">
          <h2 className="font-semibold">Alerts</h2>
          <p>Recent high-severity alerts triggered by collectors.</p>
        </div>
      </div>
    </div>
  );
};

export default Dashboard;

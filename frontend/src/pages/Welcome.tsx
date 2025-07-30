import React from 'react';

const Welcome: React.FC = () => {
  return (
    <div className="min-h-screen flex items-center justify-center bg-gray-100">
      <div className="text-center">
        <h1 className="text-4xl font-bold text-gray-900 mb-4">
          Welcome to Basketball Player Ranking
        </h1>
        <p className="text-xl text-gray-600">
          Your platform for analyzing and ranking basketball players
        </p>
      </div>
    </div>
  );
};

export default Welcome;

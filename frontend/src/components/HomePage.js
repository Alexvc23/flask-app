import React from 'react';
import { Link } from 'react-router-dom';

function HomePage() {
  return (
    <div className="min-h-screen bg-blue-50 flex flex-col justify-center items-center">
      <h1 className="text-4xl font-bold text-blue-700 mb-8">Welcome to Our Application</h1>
      <p className="text-lg text-blue-600 mb-4">Navigate through the application:</p>
      <div className="space-x-4">
        <Link to="/affaire-form" className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded">
          Go to Affaire Form
        </Link>
        {/* Add more links as needed */}
      </div>
    </div>
  );
}

export default HomePage;

export default function App() {
  return (
    <div className="min-h-screen flex flex-col">
      {/* Navbar */}
      <nav className="bg-white shadow-md">
        <div className="max-w-7xl mx-auto px-6 py-4 flex justify-between items-center">
          <h1 className="text-2xl font-bold text-blue-600">Ethical Decision Simulator</h1>
          <ul className="flex space-x-6">
            <li><a href="/" className="text-gray-700 hover:text-blue-600">Home</a></li>
            <li><a href="/about" className="text-gray-700 hover:text-blue-600">About</a></li>
            <li><a href="/contact" className="text-gray-700 hover:text-blue-600">Contact</a></li>
          </ul>
        </div>
      </nav>

      {/* Hero Section */}
      <header className="flex-1 flex items-center justify-center bg-gradient-to-r from-blue-500 to-purple-600 text-white">
        <div className="text-center px-6">
          <h2 className="text-4xl md:text-6xl font-extrabold mb-4">
            Make Ethical Decisions Smarter
          </h2>
          <p className="text-lg md:text-xl mb-6">
            An AI-powered simulator to explore moral dilemmas and decision-making.
          </p>
          <a href="/simulator">
            <button className="px-6 py-3 bg-white text-blue-600 rounded-lg font-semibold hover:bg-gray-100 transition">
            Try the Simulator
          </button>
          </a>
        </div>
      </header>

      {/* Footer */}
      <footer className="bg-gray-900 text-gray-300 py-6">
        <div className="max-w-7xl mx-auto px-6 text-center">
          <p>&copy; {new Date().getFullYear()} Ethical Decision Simulator. All rights reserved.</p>
        </div>
      </footer>
    </div>
  );
}

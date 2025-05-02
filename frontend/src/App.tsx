// src/App.tsx

import React, { useState } from "react";
import FileUpload from "./components/FileUpload";
import StrategySelector from "./components/StrategySelector";
import Results from "./components/Results";
import ThemeToggle from "./components/ThemeToggle";


function App() {
  const [darkMode, setDarkMode] = useState(true);
  const [isLoading, setIsLoading] = useState(false);
  const [file, setFile] = useState<File | null>(null);
  const [strategy, setStrategy] = useState("");
  const [result, setResult] = useState<null | {
    strategy: string;
    success: boolean;
    output: string;
  }>(null);

  const handleSubmit = async () => {
    if (!file || !strategy) return alert("Please select both file and strategy.");

    const formData = new FormData();
    formData.append("file", file);
    formData.append("strategy", strategy);

    try {
      setIsLoading(true);
      const res = await fetch("http://localhost:8000/upload", {
        method: "POST",
        body: formData,
      });
      const data = await res.json();
      setResult(data);
      setIsLoading(false);
    } catch (err) {
      alert("Upload failed");
    }
  };

  return (
    <div className={darkMode ? "dark" : ""}>
      <div className="min-h-screen bg-gray-100 dark:bg-gray-900 p-6 transition-colors duration-300">
        <div className="max-w-4xl mx-auto bg-white dark:bg-gray-800 p-8 rounded-lg shadow-lg animate-fadeIn">
          <div className="mb-6 flex flex-col items-center justify-center gap-4 text-center sm:flex-row sm:justify-between">
            <h1 className="text-3xl font-bold text-gray-800 dark:text-white text-center">
              Probatio
            </h1>
            <ThemeToggle darkMode={darkMode} toggle={() => setDarkMode(!darkMode)} />
          </div>
          <FileUpload onFileSelect={setFile} selectedFile={file} />
          <StrategySelector strategy={strategy} setStrategy={setStrategy} />
          {isLoading && (
            <div className="mt-4 text-blue-500 font-medium animate-pulse text-center">
              Running tests...
            </div>
          )}
          <button
            onClick={handleSubmit}
            className="mt-6 w-full bg-green-600 text-white py-3 rounded shadow hover:bg-green-700 hover:shadow-glow transition duration-200 font-semibold"
          >
            Run Test
          </button>

          {result && <Results {...result} />}
        </div>
      </div>
    </div>
  );
}

export default App;

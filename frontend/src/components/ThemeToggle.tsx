// src/components/ThemeToggle.tsx

import { useEffect } from "react";
import { Moon, Sun } from "lucide-react";

interface Props {
  darkMode: boolean;
  toggle: () => void;
}

const ThemeToggle: React.FC<Props> = ({ darkMode, toggle }) => {
  useEffect(() => {
    document.documentElement.classList.toggle("dark", darkMode);
  }, [darkMode]);

  return (
    <div className="flex items-center space-x-4">
      <span className="text-sm font-medium text-gray-800 dark:text-gray-100">
        {darkMode ? "Dark Mode" : "Light Mode"}
      </span>
      <button
        onClick={toggle}
        className={`w-14 h-8 rounded-full flex items-center px-1 transition 
        ${darkMode ? "bg-blue-600 justify-end" : "bg-gray-300 justify-start"}`}
      >
        {darkMode ? (
          <Moon size={18} className="text-white" />
        ) : (
          <Sun size={18} className="text-yellow-500" />
        )}
      </button>
    </div>
  );
};

export default ThemeToggle;

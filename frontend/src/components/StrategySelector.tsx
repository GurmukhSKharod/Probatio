// src/components/StrategySelector.tsx

import React from "react";

interface Props {
  strategy: string;
  setStrategy: (value: string) => void;
}

const StrategySelector: React.FC<Props> = ({ strategy, setStrategy }) => {
  return (
    <select
    className="mt-6 w-full p-3 border border-gray-300 rounded 
    text-gray-800 bg-white dark:bg-gray-700 dark:text-gray-100 
    focus:outline-none focus:ring-2 focus:ring-blue-500 
    transition-all duration-300 ease-in-out animate-fadeIn"
      value={strategy}
      onChange={(e) => setStrategy(e.target.value)}
    >
      <option value="">Select a test strategy</option>
      <option value="unit">Unit Testing</option>
      <option value="property">Property-Based Testing</option>
      <option value="random">Random Testing</option> 
    </select>
  );
};

export default StrategySelector;

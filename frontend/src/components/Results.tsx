// src/components/Results.tsx

import React from "react";
import Chart from "./Chart";

interface Props {
  strategy: string;
  success: boolean;
  output: string;
}

const Results: React.FC<Props> = ({ strategy, success, output }) => {
  return (
    <div
      className="mt-8 p-6 border rounded-xl shadow-lg 
      bg-white dark:bg-gray-900 
      text-gray-800 dark:text-gray-100 
      border-gray-300 dark:border-gray-700 
      animate-fadeIn transition-all duration-700 ease-in-out"
    >
      <h2 className="font-bold text-2xl mb-6 text-gray-800 dark:text-gray-100 tracking-wide">
        Results
      </h2>

      <div className="flex flex-col sm:flex-row sm:items-center sm:justify-between mb-6 space-y-4 sm:space-y-0">
        <div className="text-lg">
          <span className="font-medium text-gray-600 dark:text-gray-300">Strategy:</span>{" "}
          <span className="text-indigo-600 dark:text-indigo-400 font-semibold capitalize">
            {strategy}
          </span>
        </div>
        <div className="text-lg">
          <span className="font-medium text-gray-600 dark:text-gray-300">Status:</span>{" "}
          <span
            className={`font-semibold px-2 py-1 rounded transition-colors duration-300
              ${
                success
                  ? "bg-green-100 dark:bg-green-900 text-green-700 dark:text-green-300"
                  : "bg-red-100 dark:bg-red-900 text-red-700 dark:text-red-300"
              }`}
          >
            {success ? "Passed" : "Failed"}
          </span>
        </div>
      </div>

      <div className="mb-6">
        <Chart passCount={success ? 1 : 0} failCount={success ? 0 : 1} />
      </div>

      <pre
        className="mt-4 p-4 bg-gray-100 dark:bg-gray-800 
        text-sm text-gray-800 dark:text-gray-100 
        overflow-auto whitespace-pre-wrap max-h-96 rounded-lg border border-gray-300 dark:border-gray-600
        animate-fadeIn transition-all duration-700 ease-in-out"
      >
        {output}
      </pre>
    </div>
  );
};

export default Results;

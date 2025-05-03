// src/components/Results.tsx

import React from "react";
import Chart from "./Chart";

interface Props {
  strategy: string;
  success: boolean;
  output: string;
}

const Results: React.FC<Props> = ({ strategy, success, output }) => {
  // Dynamically count PASS and FAIL from output string
  const passCount = (output.match(/PASS/g) || []).length;
  const failCount = (output.match(/FAIL/g) || []).length;

  return (
    <div
      className="mt-8 p-6 border rounded shadow-sm 
      bg-white dark:bg-gray-900 
      text-gray-800 dark:text-gray-100 
      border-gray-300 dark:border-gray-700 
      animate-slideUp transition-all duration-500"
    >
      <h2 className="font-bold text-xl mb-3 text-gray-800 dark:text-gray-100">Results</h2>

      <p className="text-gray-700 dark:text-gray-300">
        <strong>Strategy:</strong>{" "}
        <span className="text-blue-600 dark:text-blue-400">{strategy}</span>
      </p>

      <p className="text-gray-700 dark:text-gray-300">
        <strong>Status:</strong>{" "}
        <span
          className={`font-medium ${
            success
              ? "text-green-600 dark:text-green-400"
              : "text-red-600 dark:text-red-400"
          }`}
        >
          {success ? "Passed" : "Failed"}
        </span>
      </p>

      {/* Chart */}
      <div className="mt-6 max-w-xs">
        <Chart passCount={passCount} failCount={failCount} />
      </div>

      {/* Output box */}
      <pre
        className="mt-4 p-4 bg-gray-100 dark:bg-gray-800 
        text-sm text-gray-800 dark:text-gray-100 
        overflow-auto whitespace-pre-wrap max-h-96 rounded border border-gray-300 dark:border-gray-600"
      >
        {output}
      </pre>
    </div>
  );
};

export default Results;

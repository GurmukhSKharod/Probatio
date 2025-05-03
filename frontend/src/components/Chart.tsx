// src/components/Chart.tsx

import React from "react";
import { Pie } from "react-chartjs-2";
import {
  Chart as ChartJS,
  ArcElement,
  Tooltip,
  Legend,
} from "chart.js";

ChartJS.register(ArcElement, Tooltip, Legend);

interface Props {
  passCount: number;
  failCount: number;
}

const Chart: React.FC<Props> = ({ passCount, failCount }) => {
  const data = {
    labels: ["Pass", "Fail"],
    datasets: [
      {
        label: "# of Results",
        data: [passCount, failCount],
        backgroundColor: ["#10B981", "#EF4444"], // green, red
        borderWidth: 1,
      },
    ],
  };

  const options = {
    plugins: {
      legend: {
        display: false, // hide default legend
      },
    },
    maintainAspectRatio: false,
  };

  return (
    <div className="relative bg-gray-100 dark:bg-gray-800 p-4 rounded shadow w-full flex justify-center">
      {/* Pass and Fail labels */}
      <div className="absolute top-3 left-4 flex items-center space-x-2">
        <div className="w-4 h-4 bg-green-500 rounded-sm"></div>
        <span className="text-sm text-gray-800 dark:text-gray-200 font-medium">Pass</span>
      </div>
      <div className="absolute top-3 right-4 flex items-center space-x-2">
        <div className="w-4 h-4 bg-red-500 rounded-sm"></div>
        <span className="text-sm text-gray-800 dark:text-gray-200 font-medium">Fail</span>
      </div>

      {/* Pie Chart */}
      <div className="w-full sm:w-1/2 h-64">
        <Pie data={data} options={options} />
      </div>
    </div>
  );
};

export default Chart;

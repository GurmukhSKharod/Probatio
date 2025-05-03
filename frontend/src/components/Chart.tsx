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

  return (
    <div className="bg-white dark:bg-gray-800 p-4 rounded shadow">
      <Pie data={data} />
    </div>
  );
};

export default Chart;

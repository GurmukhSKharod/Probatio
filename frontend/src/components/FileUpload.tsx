// src/components/FileUpload.tsx

import React, { useRef } from "react";

interface FileUploadProps {
  onFileSelect: (file: File) => void;
  selectedFile?: File | null;
}

const FileUpload: React.FC<FileUploadProps> = ({ onFileSelect, selectedFile }) => {
  const inputRef = useRef<HTMLInputElement | null>(null);

  const handleDrop = (e: React.DragEvent) => {
    e.preventDefault();
    const file = e.dataTransfer.files[0];
    if (file) onFileSelect(file);
  };

  return (
    <div
      onDrop={handleDrop}
      onDragOver={(e) => e.preventDefault()}
      className="border-2 border-dashed border-blue-400 p-6 rounded-lg text-center text-sm 
        text-gray-800 dark:text-gray-200 bg-white dark:bg-gray-700 transition-all duration-300 
        hover:shadow-glow animate-slideUp"
    >
      {selectedFile ? (
        <p className="font-medium text-green-700 dark:text-green-400">
          Selected file: <span className="font-semibold">{selectedFile.name}</span>
        </p>
      ) : (
        <>
          <p className="mb-2">Drag & drop a Python file here</p>
          <p className="mb-2">or</p>
          <button
            className="px-4 py-2 bg-blue-500 text-white rounded hover:bg-blue-600 hover:shadow-glow 
              transition duration-200"
            onClick={() => inputRef.current?.click()}
          >
            Browse
          </button>
        </>
      )}

      <input
        type="file"
        accept=".py"
        ref={inputRef}
        className="hidden"
        onChange={(e) => {
          const file = e.target.files?.[0];
          if (file) onFileSelect(file);
        }}
      />
    </div>
  );
};

export default FileUpload;

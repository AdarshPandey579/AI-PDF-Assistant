import { useRef, useState } from "react";
import api from "../services/api.js";
// import { FiUploadCloud } from "react-icons/fi";

function UploadCard({ setSummary, loading, setLoading}) {
  const inputRef = useRef(null);
  const [file, setFile] = useState(null);
  const [dragActive, setDragActive] = useState(false);

  const handleBrowseClick = () => {
    inputRef.current.click();
  };

  const handleFileChange = (event) => {
    const selectedFile = event.target.files[0];
    // No file selected
    if (!selectedFile) return;
    // Allow only PDF files
    if (selectedFile.type !== "application/pdf") {
      alert("Please select a PDF file.");
      event.target.value = ""; // Reset file input
      return;
    }
    const MAX_FILE_SIZE = 20 * 1024 * 1024;
    if (selectedFile.size > MAX_FILE_SIZE) {
      alert("File size must be less than 20 MB.");
      event.target.value = "";
      return;
    }
    setFile(selectedFile);
    // Clear previous summary
    setSummary("");
  };

  const handleDragOver = (event) => {
    event.preventDefault();
    setDragActive(true);
  };

  const handleDragLeave = (event) => {
    event.preventDefault();
    setDragActive(false);
  };

  const handleDrop = (event) => {
    event.preventDefault();
    setDragActive(false);

    const droppedFile = event.dataTransfer.files[0];

    if (!droppedFile) return;

    if (droppedFile.type !== "application/pdf") {
      alert("Please drop a PDF file.");
      return;
    }

    setFile(droppedFile);
    setSummary("");
  };

  const handleGenerateSummary = async () => {
    if (!file) return;
    const formData = new FormData();
    formData.append("file", file);
    try {
      setLoading(true);
      const response = await api.post(
        "/summarize",
        formData
      );
      setSummary(response.data.summary);
    } catch (error) {
      console.error(error);
      alert("Failed to generate summary.");

    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="max-w-3xl mx-auto mt-12 bg-white rounded-xl shadow-lg p-8">

      <h2 className="text-3xl font-bold text-center mb-6">
        Upload PDF
      </h2>

      <div
        onDragOver={handleDragOver}
        onDragLeave={handleDragLeave}
        onDrop={handleDrop}
        className={`border-2 border-dashed rounded-lg p-10 text-center transition-all duration-300 ${
          dragActive
            ? "border-blue-600 bg-blue-50"
            : "border-gray-300"
        }`}
      >
        {/* <FiUploadCloud
          size={70}
          className="mx-auto text-blue-600 mb-5"
        /> */}
        <p className="text-gray-600 text-lg">
          {dragActive
            ? "Drop your PDF here"
            : "Drag & Drop your PDF here"}
        </p>

        <p className="my-4 text-gray-400">or</p>

        <button
          disabled={loading}
          onClick={handleBrowseClick}
          className="bg-blue-600 hover:bg-blue-700 disabled:bg-gray-400 text-white px-6 py-2 rounded-lg"
        >
          Browse File
        </button>

        <input
          type="file"
          accept=".pdf"
          ref={inputRef}
          onChange={handleFileChange}
          className="hidden"
        />
        {file && (
          <p className="mt-4 text-green-600 font-medium">
            Selected: {file.name}
          </p>
        )}
      </div>

      <button
        onClick={handleGenerateSummary}
        disabled={!file || loading}
        className={`w-full mt-8 py-3 rounded-lg text-lg font-semibold text-white transition ${
          !file || loading
            ? "bg-gray-400 cursor-not-allowed"
            : "bg-green-600 hover:bg-green-700"
        }`}
      >
        Generate Summary
      </button>

    </div>
  );
}

export default UploadCard;
import { useState } from "react";
import api from "../../services/api";

function UploadSection() {
  const [files, setFiles] = useState([]);
  const [loading, setLoading] = useState(false);
  const [uploaded, setUploaded] = useState(false);

  function handleFileChange(event) {
      setFiles(Array.from(event.target.files));
      setUploaded(false);
  }

  const handleUpload = async () => {
    if (files.length === 0) return;
    const formData = new FormData();
    files.forEach((file) => {
        formData.append("files", file);
    });
    try {
        setLoading(true);
        const response = await api.post("/upload", formData);
        console.log(response.data);
        setUploaded(true);
    } catch (error) {
        console.error(error);
        alert("Failed to upload PDFs.");
    } finally {
        setLoading(false);
    }
  };

  return (
    <div className="bg-white rounded-xl shadow-lg p-6 mb-6">

      <h2 className="text-xl font-bold mb-4">
        Upload PDFs
      </h2>

      <input
        type="file"
        multiple
        accept=".pdf"
        onChange={handleFileChange}
      />
      <ul className="mt-3 space-y-1">
          {files.map((file) => (
              <li key={file.name}>
                  📄 {file.name}
              </li>
          ))}
      </ul>

      {uploaded && (
          <p className="text-green-600 mt-3">
              ✅ PDFs uploaded successfully
          </p>
      )}

      <button
          onClick={handleUpload}
          disabled={loading}
          className="bg-pink-500 text-white px-6 py-2 rounded-lg mt-4 disabled:bg-gray-400"
      >
          {loading ? "Uploading..." : "Upload"}
      </button>

    </div>
  );
}

export default UploadSection;
import { useState } from "react";

import Navbar from "../components/Navbar";
import Footer from "../components/Footer";

import UploadCard from "../components/summarizer/UploadCard";
import Summary from "../components/summarizer/Summary";
import Loader from "../components/summarizer/Loader";
import ActionButtons from "../components/summarizer/CopyButtons";
import DownloadButtons from "../components/summarizer/DownloadButtons";


function SummarizerPage() {
  const [summary, setSummary] = useState("");
  const [loading, setLoading] = useState(false);

  return (
    <div className="min-h-screen bg-gray-100">
      <Navbar />

      <main className="max-w-5xl mx-auto p-6">
        <UploadCard
          setSummary={setSummary}
          loading={loading}
          setLoading={setLoading}
        />

        <Loader loading={loading} />

        <Summary summary={summary} />

        {summary && (
          <div className="flex justify-evenly items-center mt-6">
            <DownloadButtons summary={summary} />
            <ActionButtons summary={summary} />
          </div>
        )}
      </main>

      <Footer />
    </div>
  );
}

export default SummarizerPage;
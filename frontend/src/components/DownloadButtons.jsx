import jsPDF from "jspdf";

function DownloadButtons({ summary }) {
  if (!summary) return null;

  const downloadPDF = () => {
    const pdf = new jsPDF();

    const lines = pdf.splitTextToSize(summary, 180);

    pdf.text(lines, 15, 20);

    pdf.save("summary.pdf");
  };

  return (
      <button
        onClick={downloadPDF}
        className="bg-red-600 hover:bg-red-700 text-white px-5 py-2 rounded-lg"
      >
        Download PDF
    </button>
  );
}

export default DownloadButtons;
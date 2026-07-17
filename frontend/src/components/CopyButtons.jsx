function ActionButtons({ summary }) {

  if (!summary) return null;

  const handleCopy = async () => {
    try {
      await navigator.clipboard.writeText(summary);
      alert("Summary copied!");
    } catch (error) {
      console.error(error);
      alert("Failed to copy summary.");
    }
  };

  return (
      <button
        onClick={handleCopy}
        className="bg-blue-600 hover:bg-blue-700 text-white px-5 py-2 rounded-lg"
      >
        Copy Summary
      </button>
  );
}

export default ActionButtons;
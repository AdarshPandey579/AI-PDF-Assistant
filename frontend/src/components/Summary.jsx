import ReactMarkdown from "react-markdown";

function Summary({ summary }) {
  if (!summary) return null;

  return (
    <div className="mt-8 bg-white rounded-xl shadow-lg p-8">
      <h2 className="text-3xl font-bold mb-6">
        Summary
      </h2>

      <div className="prose prose-lg max-w-none">
        <ReactMarkdown>
          {summary}
        </ReactMarkdown>
      </div>
    </div>
  );
}

export default Summary;
import ReactMarkdown from "react-markdown";

function Summary({ summary }) {
  if (!summary) return null;

  return (
    <div className="mt-8 bg-white rounded-xl shadow-lg p-8">
      <h2 className="text-3xl font-bold mb-6">
        Summary
      </h2>

      <div>
        <ReactMarkdown
          components={{
            h1: ({ children }) => (
              <h1 className="text-2xl font-bold mt-4 mb-2">{children}</h1>
            ),
            h2: ({ children }) => (
              <h2 className="text-xl font-semibold mt-4 mb-2">{children}</h2>
            ),
            h3: ({ children }) => (
              <h3 className="text-lg font-semibold mt-3 mb-2">{children}</h3>
            ),
          }}
        >
          {summary}
        </ReactMarkdown>
      </div>
    </div>
  );
}

export default Summary;
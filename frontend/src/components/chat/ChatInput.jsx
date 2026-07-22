import { useState } from "react";
import api from "../../services/api";

function ChatInput({ setMessages }) {
  const [question, setQuestion] = useState("");

  const handleSend = async () => {
    const userQuestion = question;
    setMessages((prevMessages) => [...prevMessages, { role: "user", content: userQuestion }]);
    setQuestion("");
    const response = await api.post("/chat", { question: userQuestion });
    setMessages((prevMessages) => [...prevMessages, { role: "assistant", content: response.data.answer }]);
  }

  return (
    <div className="flex gap-4">

      <form onSubmit={(e)=>{e.preventDefault(); handleSend()}}>
        <input
          type="text"
          placeholder="Ask something..."
          value={question}
          onChange={(e) => setQuestion(e.target.value)}
          className="flex-1 border rounded-lg px-4 py-3"
        />

        <button
          type="submit"
          className="bg-pink-500 hover:bg-pink-600 text-white px-6 rounded-lg"
        >
          Send
        </button>
      </form>

    </div>
  );
}

export default ChatInput;



// User clicks Send
//         │
//         ▼
// Save question
//         │
//         ▼
// Show user message immediately
//         │
//         ▼
// Clear input
//         │
//         ▼
// POST /chat
//         │
//         ▼
// Backend searches Qdrant
//         │
//         ▼
// LLM generates answer
//         │
//         ▼
// Receive response
//         │
//         ▼
// Show assistant message
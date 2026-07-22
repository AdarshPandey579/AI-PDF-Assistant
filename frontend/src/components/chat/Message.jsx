import ReactMarkdown from "react-markdown";

function Message({ role, content }) {

    return (
        <div
            className={`flex mb-4 ${
                role === "user" ? "justify-end" : "justify-start"
            }`}
        >
            <div
                className={`max-w-[70%] rounded-xl px-4 py-3 ${
                    role === "user"
                        ? "bg-pink-500 text-white"
                        : "bg-gray-200 text-black"
                }`}
            >
                <ReactMarkdown>{content}</ReactMarkdown>
            </div>
        </div>
    );
}

export default Message;
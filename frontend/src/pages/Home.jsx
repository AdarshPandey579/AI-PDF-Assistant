import { useNavigate }  from "react-router-dom";
import Navbar from "../components/Navbar";
import Footer from "../components/Footer";


function Home() {
  const navigate = useNavigate();

  return(
    <div className="min-h-screen bg-gray-100 flex flex-col">
      <Navbar />

      <main className="flex-1 flex items-center justify-center">
        <div className="w-full max-w-5xl grid grid-cols-1 md:grid-cols-2 gap-8">
          <div
            onClick={() => navigate("/chat")}
            className="cursor-pointer bg-gradient-to-r from-pink-600 to-fuchsia-500 text-white rounded-xl shadow-lg p-10 hover:scale-105 transition duration-300"
          >
            <h2 className="text-2xl font-bold text-center">
              Chat with PDFs
            </h2>
          </div>
          <div
            onClick={() => navigate("/summarizer")}
            className="cursor-pointer bg-gradient-to-r from-emerald-600 to-teal-500 text-white rounded-xl shadow-lg p-10 hover:scale-105 transition duration-300"
          >
            <h2 className="text-2xl font-bold text-center">
              PDF Summarizer
            </h2>
          </div>
        </div>
      </main>

      <Footer />
    </div>
  )
}

export default Home;
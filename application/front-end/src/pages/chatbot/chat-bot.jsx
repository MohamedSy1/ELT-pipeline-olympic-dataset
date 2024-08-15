import { useState } from "react";
import Sidebar from "../../components/sidebar";
import OutgoingMessage from "../../components/outgoingMessage";
import IncomingMessage from "../../components/incomingMessage";

export default function Chatbot() {
    const [result, setResult] = useState([]);
    const [question, setQuestion] = useState([]);

    const handleQuestionChange = (event) => {
        setQuestion(event.target.value);
    }

    const handleSubmit = (event) => {
        event.preventDefault();

        const formData = new FormData();

        if (question) {
            formData.append('question', question);
        }

        fetch('http://127.0.0.1:5000/predict', {
            mode: "cors",
            method: "POST",
            body: formData
        })
            .then((response) => response.json())
            .then((data) => {
                setResult([...result, data.result]);
            })
            .catch((error) => {
                console.error("Error", error);
            });
    }

    return (
        <div className="min-h-screen bg-gray-100 dark:bg-gray-900">
            <section className="max-w-3xl mx-auto pt-28 px-4">
                <IncomingMessage question={question} />
                <OutgoingMessage result={result} />
            </section>
            <div className="fixed inset-x-0 bottom-0 flex justify-center p-4 bg-gray-50 dark:bg-gray-800">
                <form onSubmit={handleSubmit} className="w-full max-w-2xl">
                    <label htmlFor="chat" className="sr-only">Your message</label>
                    <div className="flex items-center px-3 py-2 rounded-lg bg-gray-50 dark:bg-gray-700">
                        <textarea
                            id="chat"
                            rows="1"
                            className="block w-full px-4 py-2 text-sm bg-white border border-gray-300 rounded-lg text-gray-900 focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-800 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
                            placeholder="Ask question about olympic 2021"
                            onChange={handleQuestionChange}
                            value={question}
                        ></textarea>
                        <button
                            type="submit"
                            className="inline-flex justify-center p-2 text-blue-600 rounded-full hover:bg-blue-100 dark:text-blue-500 dark:hover:bg-gray-600"
                            disabled={!question}
                        >
                            <svg className="w-5 h-5 rotate-90" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="currentColor" viewBox="0 0 18 20">
                                <path d="m17.914 18.594-8-18a1 1 0 0 0-1.828 0l-8 18a1 1 0 0 0 1.157 1.376L8 18.281V9a1 1 0 0 1 2 0v9.281l6.758 1.689a1 1 0 0 0 1.156-1.376Z" />
                            </svg>
                            <span className="sr-only">Send message</span>
                        </button>
                    </div>
                </form>
            </div>
        </div>
    );
}

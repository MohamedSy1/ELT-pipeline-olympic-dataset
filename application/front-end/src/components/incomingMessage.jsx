import { useEffect } from "react"

const IncomingMessage = ({ message }) => {
    useEffect(() => {
        console.log("Message has changed:", message);

    }, [message]);

    return (
        <div>
            {message?.map((item, index) => (
                <div key={index} className="flex justify-end mb-4 cursor-pointer">
                    <div className="flex bg-indigo-500 text-white rounded-lg p-3 max-w-xs lg:max-w-sm">
                        <p>{item}</p>
                    </div>
                    <div className="w-9 h-9 rounded-full flex items-center justify-center ml-2">
                        <img src="https://placehold.co/200x/b7a8ff/ffffff.svg?text=ʕ•́ᴥ•̀ʔ&font=Lato" alt="My Avatar" className="w-8 h-8 rounded-full" />
                    </div>
                </div>
            ))}
        </div>
    )
}

export default IncomingMessage;
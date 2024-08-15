import { useEffect } from "react";

const OutgoingMessage = ({ result }) => {
    useEffect(() => {
        console.log("Result has changed:", result);
    }, [result]);

    return (
        <div>
            {result?.map((item, index) => (
                <div key={index} className="flex mb-4 cursor-pointer">
                    <div className="w-9 h-9 rounded-full flex items-center justify-center mr-2">
                        <img src="https://placehold.co/200x/ffa8e4/ffffff.svg?text=ʕ•́ᴥ•̀ʔ&font=Lato" alt="User Avatar" className="w-8 h-8 rounded-full" />
                    </div>
                    <div className="flex bg-white text-gray-700 rounded-lg p-3 max-w-xs lg:max-w-sm dark:bg-white-800">
                        <p>{item}</p>
                    </div>
                </div>
            ))}
        </div>
    )
}


export default OutgoingMessage;
import React, { useState } from 'react';

function Home() {
    const [input, setInput] = useState(''); 
    const [messages, setMessages] = useState([]); 

    const handleInputChange = (e) => {
        setInput(e.target.value); 
    };

    const handleSubmit = (e) => {
        e.preventDefault(); 
        if (!input.trim()) return; 
        setMessages([...messages, input]);
        setInput(''); 
    };

    return (
        <div className="home">
            <h2>Math Chat</h2>
            <div className="chatBox">
                {messages.map((message, index) => (
                    <div key={index} className="message">
                        {message}
                    </div>
                ))}
            </div>
            <form onSubmit={handleSubmit}>
                <input
                    type="text"
                    value={input}
                    onChange={handleInputChange}
                    placeholder="Enter Math Problem"
                />
                <button type="submit">Send</button>
            </form>
        </div>
    );
}

export default Home;

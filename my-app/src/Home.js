import React, { useState, useEffect, useRef } from 'react';
import './Home.css';
import backgroundImage from './pic2.jpg';

function Home() {
    const [input, setInput] = useState('');
    const [messages, setMessages] = useState([]);
    const messagesEndRef = useRef(null); // Create a ref for scrolling

    const handleInputChange = (e) => {
        setInput(e.target.value);
    };

    const handleSubmit = (e) => {
        e.preventDefault();
        if (!input.trim()) return;
        setMessages([...messages, input]);
        setInput('');
    };

    const handleGetHint = () => {
        const hint = "Here's a hint for your math problem.";
        setMessages([...messages, hint]);
    };

    const handleGetAnswer = () => {
        const answer = "The answer to your math problem is 42.";
        setMessages([...messages, answer]);
    };

    useEffect(() => {
        // Scroll to the bottom of messages container
        messagesEndRef.current?.scrollIntoView({ behavior: "smooth" });
    }, [messages]); // This effect runs every time `messages` changes

    return (
        <div className="home" style={{ backgroundImage: `url(${backgroundImage})`, backgroundSize: 'cover', backgroundPosition: 'center', height: '100vh' }}>
            <div className="main-content">
                <h2 className="ethicalBotHeading">Ethical Mathwhiz</h2>
                <br />
                <div className="textbox welcomeTextbox">
                <p className="welcomeText" style={{ color: '#ffffff' }}>Welcome to the Ethical Mathbot, to get started enter a math word problem and the bot will give you hints,</p>
                </div>
                
                <div className="chatBox">
                    {messages.map((message, index) => (
                        <div key={index} className="message">
                            {message}
                        </div>
                    ))}
                    <div ref={messagesEndRef} /> {/* Invisible element to scroll to */}
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
                <div>
                    {/* <button onClick={handleGetHint}>Get Hint</button> */}
                    <button onClick={handleGetAnswer}>Get Answer</button>
                </div>
            </div>
        </div>
    );
}

export default Home;

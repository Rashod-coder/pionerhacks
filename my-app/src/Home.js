import React, { useState } from 'react';
import './Home.css';
import backgroundImage from './pic2.jpg';

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

    const handleGetHint = () => {
        // Logic to get a hint
        const hint = "Here's a hint for your math problem.";
        setMessages([...messages, hint]);
    };

    const handleGetAnswer = () => {
        // Logic to get the answer
        const answer = "The answer to your math problem is 42.";
        setMessages([...messages, answer]);
    };

    return (
        <div className="home" style={{ backgroundImage: `url(${backgroundImage})`, backgroundSize: 'cover', backgroundPosition: 'center', height: '100vh' }}>
            <div className="main-content">
            <h2 className="ethicalBotHeading">Ethical Bot</h2>
                <br />
                <div className="textbox welcomeTextbox">
                    <p className="welcomeText">Welcome to the Ethical Mathbot, to get started enter a math word problem and the bot will give you hints,</p>
                </div>
                <br />
                <div className="textbox hintTextbox">
                    <p className="hintText">If you need more hints hit the [Get another Hint] button</p>
                </div>

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
                <div>
                    <button onClick={handleGetHint}>Get Hint</button>
                    <button onClick={handleGetAnswer}>Get Answer</button>
                </div>
            </div>
        </div>
    );
}

export default Home;

import React from 'react';
import pic2 from './pic2.jpg'; // Make sure the path to your image is correct

function About() {
  return (
    <div style={{ 
      backgroundImage: `url(${pic2})`, 
      backgroundSize: 'cover', 
      height: '100vh', 
      color: 'white' 
    }}>
      <h1 style={{ textAlign: 'center', paddingTop: '20px', fontSize: '36px' }}>About Page</h1>
      <div style={{ display: 'flex', justifyContent: 'center', marginTop: '20px' }}>
        <input 
          type="text" 
          value="Ethical Math Bot..."
          readOnly 
          style={{ 
            padding: '10px', 
            fontSize: '24px', 
            border: 'none', 
            borderRadius: '5px' 
          }} 
        />
      </div>
      <div style={{ display: 'flex', justifyContent: 'center', marginTop: '20px' }}>
        <input 
          type="text" 
          value="This bot can solve math word problems."
          readOnly 
          style={{ 
            padding: '10px', 
            fontSize: '18px', 
            border: 'none', 
            borderRadius: '5px' 
          }} 
        />
      </div>
    </div>
  );
}

export default About;

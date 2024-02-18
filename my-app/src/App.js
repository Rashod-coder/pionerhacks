import 'bootstrap/dist/css/bootstrap.min.css';
import { Nav, Navbar } from 'react-bootstrap';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom'; // Note the change here
import { Link } from 'react-router-dom'; // Import Link for internal navigation

import About from './About';
import Home from './Home';

function App() {
  return (
    <Router>
      <div className='App'>
        <Navbar bg='dark' variant='dark'>
          <Navbar.Brand href='/'>Math Bot</Navbar.Brand>
          <Nav>
            <Nav.Link href='/about'>About</Nav.Link> {/* Adjusted for consistency */}
            {/* <Nav.Link href='/login'>Login</Nav.Link> */}
          </Nav>
        </Navbar>

        <Routes> 
          <Route path='/about' element={<About />} /> 
          <Route path='/' element={<Home />} />
          {/* <Route path='/login' element={<Login />} /> */}
        </Routes>
      </div>
    </Router>
  );
}

export default App;

import 'bootstrap/dist/css/bootstrap.min.css';
import { Nav, Navbar } from 'react-bootstrap';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom'; // Note the change here
import About from './About';

function App() {
  return (
    <Router>
      <div className='App'>
        <Navbar bg='dark' variant='dark'>
          <Navbar.Brand href='/'>Math Bot</Navbar.Brand>
          <Nav>
            <Nav.Link href='/about'>About</Nav.Link> {/* Adjusted for consistency */}
          </Nav>
        </Navbar>

        <Routes> {/* Changed from Switch to Routes */}
          <Route path='/about' element={<About />} /> {/* Note the change in syntax here */}
        </Routes>
      </div>
    </Router>
  );
}

export default App;

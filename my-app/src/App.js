import 'bootstrap/dist/css/bootstrap.min.css';
import { Nav, Navbar } from 'react-bootstrap';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom'; // Note the change here
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
          </Nav>
        </Navbar>

        <Routes> 
          <Route path='/about' element={<About />} /> 
          <Route path='/' element={<Home />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;

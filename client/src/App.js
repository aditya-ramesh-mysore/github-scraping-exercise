import logo from './logo.svg';
import './App.css';
import { BrowserRouter as Router, Route, Routes, Link } from 'react-router-dom';
import PageLayout from './layouts/PageLayout';
import Button from 'react-bootstrap/Button';
import React from 'react'; 
import Container from 'react-bootstrap/Container'
import Row from 'react-bootstrap/Row'
import Col from 'react-bootstrap/Col'
import Nav from 'react-bootstrap/Nav'
import Navbar from 'react-bootstrap/Navbar'
import 'bootstrap/dist/css/bootstrap.min.css';
import Landing from './components/Landing';

function App() {
  return (
    <Router>
      <Navbar bg="dark" variant="dark" expand="lg">
        <Container>
          <Navbar.Brand as={Link} to="/">
            GitHub Scraper UI
          </Navbar.Brand>
          <Navbar.Toggle aria-controls="basic-navbar-nav" />
          <Navbar.Collapse id="basic-navbar-nav">
            <Nav className="me-auto">
              <Nav.Link as={Link} to="/repositories">
                User Repositories
              </Nav.Link>
              <Nav.Link as={Link} to="/recent-users">
                Recent Users
              </Nav.Link>
              <Nav.Link as={Link} to="/starred-projects">
                Starred Projects
              </Nav.Link>
            </Nav>
          </Navbar.Collapse>
        </Container>
      </Navbar>
      <PageLayout>
        <Landing />
      </PageLayout>
      <Container className="my-5">
        <Routes>
          {/* <Route path="/repositories" element={<UserRepositories />} />
          <Route path="/recent-users" element={<RecentUsers />} />
          <Route path="/starred-projects" element={<StarredProjects />} /> */}
        </Routes>
      </Container>
    </Router>
  );
}

export default App;

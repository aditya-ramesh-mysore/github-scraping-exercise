import logo from './logo.svg';
import './App.css';
import { BrowserRouter as Router, Route, Routes, Link } from 'react-router-dom';
import PageLayout from './layouts/PageLayout';
import Button from 'react-bootstrap/Button';
import React from 'react'; 
import Container from 'react-bootstrap/Container'
import Row from 'react-bootstrap/Row'
import Col from 'react-bootstrap/Col'
import 'bootstrap/dist/css/bootstrap.min.css';
import Landing from './components/Landing';
import NavBar from './components/NavBar';

function App() {
  return (
    <Router>
      <NavBar />

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

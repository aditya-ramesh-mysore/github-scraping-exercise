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
import UserRepositoriesPage from './pages/UserRepositoriesPage';
import RecentUsersPage from './pages/RecentUsersPage';
import StarredProjectsPage from './pages/StarredProjectsPage';

function App() {
  return (
    <Router>
      <NavBar />
      <PageLayout>
          <Routes>
            <Route path='/' element={<Landing />} />
            <Route path="/repositories" element={<UserRepositoriesPage />} />
            <Route path="/recent-users" element={<RecentUsersPage />} />
            <Route path="/starred-projects" element={<StarredProjectsPage />} />
          </Routes>
        </PageLayout>
    </Router>
  );
}

export default App;

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
import LandingPage from './pages/LandingPage';
import NavBar from './components/NavBar';
import UserRepositoriesPage from './pages/UserRepositoriesPage';
import RecentUsersPage from './pages/RecentUsersPage';
import StarredProjectsPage from './pages/StarredProjectsPage';
import { AlertProvider } from './hooks/useAlert';

function App() {
  return (
    <Router>
      <AlertProvider>
        <NavBar />
        <PageLayout>
          <Routes>
            <Route path='/' element={<LandingPage />} />
            <Route path="/repositories" element={<UserRepositoriesPage />} />
            <Route path="/recent-users" element={<RecentUsersPage />} />
            <Route path="/projects" element={<StarredProjectsPage />} />
          </Routes>
        </PageLayout>
      </AlertProvider>
    </Router>
  );
}

export default App;

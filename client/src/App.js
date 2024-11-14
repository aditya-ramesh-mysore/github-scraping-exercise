import './App.css';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import PageLayout from './layouts/PageLayout';
import React from 'react'; 
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
      
        <NavBar />
        <PageLayout>
        <AlertProvider>
          <Routes>
            <Route path='/' element={<LandingPage />} />
            <Route path="/repositories" element={<UserRepositoriesPage />} />
            <Route path="/recent-users" element={<RecentUsersPage />} />
            <Route path="/projects" element={<StarredProjectsPage />} />
          </Routes>
        </AlertProvider>
        </PageLayout>

    </Router>
  );
}

export default App;

import React from 'react';
import Button from 'react-bootstrap/Button'
import Col from 'react-bootstrap/esm/Col';
import { useNavigate } from 'react-router-dom';
import {ReactTyped} from 'react-typed'

// Main landing page 
export default function Landing() {
  const navigate = useNavigate();

  return (
    <React.Fragment>
      <Col lg={{ span: 8, offset: 2 }}>
        
        <ReactTyped 
          className="display-4" 
          style={{color: 'black'}}
          strings={["Discover the power of Github Scraper."]} 
          typeSpeed={50} 
          />

      </Col>
      <p className="lead">
      Easily explore user repositories, discover recent users, and find the most popular projects.
      </p>
      <Button onClick={() => navigate("/repositories")} variant="success" size="lg" className="me-3">Get Started</Button>
      <Button onClick={() => navigate("/projects")} variant="outline-dark" size="lg">Projects</Button>
    </React.Fragment>
  );
}

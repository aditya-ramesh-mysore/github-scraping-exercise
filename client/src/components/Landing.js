import React from 'react';
import Button from 'react-bootstrap/Button'
import Col from 'react-bootstrap/esm/Col';
import {ReactTyped} from 'react-typed'

export default function Landing() {
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
      Easily explore user repositories, discover recent contributors, and find the most popular projects.
      </p>
      <Button variant="success" size="lg" className="me-3">Get Started</Button>
      <Button variant="outline-dark" size="lg">Learn More</Button>
    </React.Fragment>
  );
}

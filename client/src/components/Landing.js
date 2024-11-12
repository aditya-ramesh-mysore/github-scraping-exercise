import React from 'react';
import Button from 'react-bootstrap/Button'

export default function Landing() {
  return (
    <>
      <h1 className="display-4" style={{color: 'black'}}>Programming Landing Page</h1>
      <p className="lead">
        Github Scraper
      </p>
      <Button variant="primary" size="lg" className="me-3">Get Started</Button>
      <Button variant="outline-light" size="lg">Learn More</Button>
    </>
  );
}

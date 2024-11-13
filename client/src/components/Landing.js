import React from 'react';
import Button from 'react-bootstrap/Button'

export default function Landing() {
  return (
    <React.Fragment>
      <h1 className="display-4">Discover the power of Github Scraper.</h1>
      <p className="lead">
      Easily explore user repositories, discover recent contributors, and find the most popular projects.
      </p>
      <Button variant="success" size="lg" className="me-3">Get Started</Button>
      <Button variant="outline-dark" size="lg">Learn More</Button>
    </React.Fragment>
  );
}

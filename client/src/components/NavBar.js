import React from 'react';
import Navbar from 'react-bootstrap/Navbar'
import Container from 'react-bootstrap/Container';
import Nav from 'react-bootstrap/Nav'
import Form from 'react-bootstrap/Form'
import Button from 'react-bootstrap/Button';
import { Link, useLocation } from 'react-router-dom';

export default function NavBar() {

    return ( 
    <Navbar bg="dark" variant="dark" expand="lg">
        <Container fluid>
            <Navbar.Brand as={Link} to="/">
                <img
                    src="/logo.svg"
                    alt="Logo"
                    width="30"
                    height="30"
                    className="d-inline-block align-top me-2"/>
                GitHub Scraper UI
            </Navbar.Brand>
            <Navbar.Toggle aria-controls="basic-navbar-nav"/>
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
  );
}
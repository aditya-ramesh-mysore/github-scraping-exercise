import React from 'react';
import Form from 'react-bootstrap/Form'
import Button from 'react-bootstrap/Button';

export default function UserRepositoriesSearchForm({ username, setUsername, onSearch, onRefresh }) {
  return (
    <Form className="mb-4">
        <Form.Group controlId="formUsername">
            <p>Find public repositories by typing in a github username.</p>
            <Form.Control
            type="text"
            placeholder="Enter GitHub username here"
            value={username}
            onChange={(e) => setUsername(e.target.value)}
            />
        </Form.Group>
        <Button variant="success" onClick={onSearch} className="mt-2">
            Search
        </Button>
        <Button variant="secondary" onClick={onRefresh} className="mt-2 ms-2">
            Refresh
        </Button>
    </Form>
  );
}

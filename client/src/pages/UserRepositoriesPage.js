import React, { useEffect, useState } from 'react';
import axios from "../api"
import Form from "react-bootstrap/Form"
import Button from 'react-bootstrap/Button';
import Pagination from 'react-bootstrap/Pagination'
import Table from 'react-bootstrap/Table'

export default function UserRepositoriesPage() {

  const [username, setUsername] = useState('');
  const [repositories, setRepositories] = useState([]);
  const [page, setPage] = useState(1);

  useEffect(() => {
    if (username) {
      fetchRepositories();
    }
  }, [page]);

  const fetchRepositories = async (refresh = false) => {
    const refreshParam = refresh ? '&refresh=true' : '';
    try {
      const response = await axios.get(`v1/users/${username}/repositories?page=${page}${refreshParam}`);
      console.log(response.data)
      setRepositories(response.data);
    } catch (error) {
      console.error('Error fetching repositories:', error);
    }
  };

  const handleSearch = async () => {
    setPage(1);
    fetchRepositories();
  };

  const handleRefresh = async () => {
    fetchRepositories(true);
  };


  return (
    <div className="d-flex flex-column justify-content-between" style={{ height: 'calc(100vh - 30px)' }}>
      <div>
        <h2 style={{ color: '#218838' }} className="display-6">User Repositories</h2>
        <Form className="mb-4">
          <Form.Group controlId="formUsername">
            <p>Find public repositories by typing in a github username.</p>
            <Form.Control
              type="text"
              placeholder="Enter GitHub username"
              value={username}
              onChange={(e) => setUsername(e.target.value)}
            />
          </Form.Group>
          <Button variant="success" onClick={handleSearch} className="mt-2">
            Search
          </Button>
          <Button variant="secondary" onClick={handleRefresh} className="mt-2 ms-2">
            Refresh
          </Button>
        </Form>
        {repositories.length > 0 && (
          <Table striped bordered responsive className="mt-6">
            <thead>
              <tr>
                <th style={{width: 200}}>Repository Name</th>
                <th style={{width: 400}}>Description</th>
                <th style={{width: 100}}>Stars</th>
                <th style={{width: 100}}>Forks</th>
              </tr>
            </thead>
            <tbody>
              {repositories.map((repo) => (
                <tr key={repo.id}>
                  <td>{repo.repository_name}</td>
                  <td>{repo.description || '-'}</td>
                  <td>{repo.stars || 0}</td>
                  <td>{repo.forks || 0}</td>
                </tr>
              ))}
            </tbody>
          </Table>
        )}
      </div>
      <div className="mt-auto">
        <Pagination className="mt-4 d-flex justify-content-center">
          <Pagination.Prev onClick={() => setPage(page - 1)} disabled={page === 1} />
          <Pagination.Item>{page}</Pagination.Item>
          <Pagination.Next onClick={() => setPage(page + 1)} disabled={repositories.length < 10} />
        </Pagination>
      </div>
    </div>
  );
}

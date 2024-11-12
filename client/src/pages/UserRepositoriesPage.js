import React, { useEffect, useState } from 'react';
import axios from "../api"
import Form from "react-bootstrap/Form"
import Button from 'react-bootstrap/Button';
import Pagination from 'react-bootstrap/Pagination'
import RepositoriesTable from '../components/RepositoriesTable';

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
    if(page == 1){
      fetchRepositories();
    }
    else{
      setPage(1);
    }
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
        <RepositoriesTable repositories={repositories} />
      </div>
      <div className="mt-auto">
        <Pagination className="mt-4 d-flex justify-content-center">
          <Pagination.Prev onClick={() => setPage(page => page - 1)} disabled={page === 1} />
          <Pagination.Item>{page}</Pagination.Item>
          <Pagination.Next onClick={() => setPage(page => page + 1)} disabled={repositories.length < 10} />
        </Pagination>
      </div>
    </div>
  );
}

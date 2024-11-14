import React, { useEffect, useState } from 'react';
import RepositoriesTable from '../components/RepositoriesTable';
import SearchForm from '../components/SearchForm';
import PaginationComponent from '../components/PaginationComponent';
import useApi from '../hooks/useApi';
import Col from 'react-bootstrap/esm/Col';

// Page to display repositories of a particular github user
export default function UserRepositoriesPage() {

  const [username, setUsername] = useState('');
  const [repositories, setRepositories] = useState([]);
  const [page, setPage] = useState(1);
  const callApi = useApi()

  useEffect(() => {
    if (username) {
      fetchRepositories();
    }
  }, [page]);

  const fetchRepositories = async (refresh = false) => {
    const refreshParam = refresh ? '&refresh=true' : '';
    try {
      const data = await callApi(`v1/users/${username}/repositories?page=${page}${refreshParam}`);      
      setRepositories(data);
    } catch (error) {
      setUsername('')
      setRepositories([])
    }
  };

  // if page number is 1, manually call handleFetch, else useEffect will automatically call handleFetch
  const handleSearch = async () => {
    if(page === 1){
      fetchRepositories();
    }
    else{
      setPage(1);
    }
  };

  // Set refresh to true to get most recent data
  const handleRefresh = async () => {
    fetchRepositories(true);
  };


  return (
    <div className="d-flex flex-column justify-content-between" style={{ height: 'calc(100vh - 30px)' }}>
      <div>
        <h2 style={{ color: '#218838' }} className="display-6">User Repositories</h2>
        <Col lg={{ span: 6, offset: 3 }}>
          <SearchForm 
            title={"Find github repositories by searching for their usernames."}
            searchField={username}
            setSearchField={setUsername}
            onSearch={handleSearch}
            onRefresh={handleRefresh}
            placeholder={"Enter a Github username here."}
          />
        </Col>
        <Col lg={{ span: 8, offset: 2 }}>
          <RepositoriesTable repositories={repositories} />
        </Col>
      </div>
      <div className="mt-auto">
        <PaginationComponent 
          page={page}
          setPage={setPage}
          hasMore={repositories?.length === 10}
        />
      </div>
    </div>
  );
}

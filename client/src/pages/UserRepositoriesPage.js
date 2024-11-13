import React, { useEffect, useState } from 'react';
import axios from "../api"
import Form from "react-bootstrap/Form"
import Button from 'react-bootstrap/Button';
import Pagination from 'react-bootstrap/Pagination'
import RepositoriesTable from '../components/RepositoriesTable';
import { useAlert } from '../hooks/useAlert';
import SearchForm from '../components/SearchForm';
import PaginationComponent from '../components/PaginationComponent';
import useApi from '../hooks/useApi';

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
        <SearchForm 
          title={"Find github repositories by searching for their usernames."}
          searchField={username}
          setSearchField={setUsername}
          onSearch={handleSearch}
          onRefresh={handleRefresh}
          placeholder={"Enter a Github username here."}
        />
        <RepositoriesTable repositories={repositories} />
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
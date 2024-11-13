import React, { useEffect, useState } from 'react';
import axios from "../api"
import Form from "react-bootstrap/Form"
import Button from 'react-bootstrap/Button';
import Pagination from 'react-bootstrap/Pagination'
import RepositoriesTable from '../components/RepositoriesTable';
import { useAlert } from '../hooks/useAlert';
import UserRepositoriesSearchForm from '../components/UserRepositoriesSearchForm';
import PaginationComponent from '../components/PaginationComponent';

export default function UserRepositoriesPage() {

  const [username, setUsername] = useState('');
  const [repositories, setRepositories] = useState([]);
  const [page, setPage] = useState(1);
  const showAlert = useAlert()

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
      if(error.status == 404){
        showAlert("User not found.")
      }
      else if(error.status == 429){
        showAlert('Too many requests, Please try again later.')
      }
      else{
        showAlert('Some error occurred on our end. Please try again later')
        
      }
      setUsername('')
      setRepositories([])
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
        <UserRepositoriesSearchForm 
          username={username}
          setUsername={setUsername}
          onSearch={handleSearch}
          onRefresh={handleRefresh}
        />
        <RepositoriesTable repositories={repositories} />
      </div>
      <div className="mt-auto">
        <PaginationComponent 
          page={page}
          setPage={setPage}
          hasMore={repositories.length === 10}
        />
      </div>
    </div>
  );
}

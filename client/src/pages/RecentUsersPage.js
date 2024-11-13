import React, { useEffect, useState } from 'react';
import UsersTable from '../components/UsersTable';
import axios from '../api'
import Form from 'react-bootstrap/Form'
import { useAlert } from '../hooks/useAlert';
import Button from 'react-bootstrap/Button';
import PaginationComponent from '../components/PaginationComponent';
import SearchForm from '../components/SearchForm';

export default function RecentUsersPage() {
  const [n, setN] = useState(1);
  const [users, setUsers] = useState([]);
  const [page, setPage] = useState(1);
  const showAlert = useAlert();

  useEffect(() => {
    handleFetch();
  }, [page]);

  const handleFetch = async () => {
    try {
      const response = await axios.get(`/v1/users?recent=${n}&page=${page}`);
      setUsers(response.data);
    } catch (error) {
      showAlert('Error fetching users. Please try again later.');
      console.error('Error fetching users:', error);
    }
  };

  const handleSearch = async () => {
    if(page == 1){
      handleFetch()
    }
    else{
      setPage(1)
    }
  }

  return (
    <div className="d-flex flex-column justify-content-between" style={{ height: 'calc(100vh - 30px)' }}>
      
      <div>
      <h2 style={{ color: '#218838' }} className="display-6">Recent Users</h2>
      <SearchForm 
        title={"Enter N to get most recent users"}
        searchField={n}
        setSearchField={setN}
        onSearch={handleSearch}
        onRefresh={null}
        placeholder={"Enter a number N"}
      />
      </div>
    
      <UsersTable users={users} />
      <div className="mt-auto">
        <PaginationComponent 
          page={page}
          setPage={setPage}
          hasMore={users.length === 10}
        />
      </div>
    </div>
  );
}

import React, { useEffect, useState } from 'react';
import UsersTable from '../components/UsersTable';
import { useAlert } from '../hooks/useAlert';
import Button from 'react-bootstrap/Button';
import PaginationComponent from '../components/PaginationComponent';
import SearchForm from '../components/SearchForm';
import useApi from '../hooks/useApi';
import Col from 'react-bootstrap/esm/Col';

export default function RecentUsersPage() {
  const [input, setInput] = useState('');
  const [users, setUsers] = useState([]);
  const [page, setPage] = useState(1);
  const callApi = useApi();

  useEffect(() => {
    if(input){
      handleFetch();
    }
  }, [page]);

  const handleFetch = async () => {
    try {
      const data = await callApi(`/v1/users?recent=${input}&page=${page}`);
      setUsers(data);
    } catch (error) {
      setUsers([])
    }
  };

  const handleSearch = async () => {
    if(page == 1){
      handleFetch();
    }
    else{
      setPage(1);
    }
  }

  return (
    <div className="d-flex flex-column justify-content-between" style={{ height: 'calc(100vh - 30px)' }}>
      
      <div>
      <h2 style={{ color: '#218838' }} className="display-6">Recent Users</h2>
      <Col lg={{ span: 6, offset: 3 }}>
        <SearchForm 
          title={"Enter a number to get N most recent users"}
          searchField={input}
          setSearchField={setInput}
          onSearch={handleSearch}
          onRefresh={null}
          placeholder={"Enter a number N"}
        />
      </Col>
      </div>
      <Col lg={{ span: 8, offset: 2 }}>
        <UsersTable users={users} />
      </Col>
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

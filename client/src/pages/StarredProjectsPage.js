import React, { useEffect, useState } from 'react';
import RepositoriesTable from '../components/RepositoriesTable';
import SearchForm from '../components/SearchForm';
import PaginationComponent from '../components/PaginationComponent';
import useApi from '../hooks/useApi';
import Col from 'react-bootstrap/esm/Col';

// Page to display most starred repositories
export default function StarredProjectsPage() {
  const [input, setInput] = useState('');
  const [repositories, setRepositories] = useState([]);
  const [page, setPage] = useState(1);
  const callApi = useApi()

  useEffect(() => {
    if(input){
      handleFetch();
    }
  }, [page]);

  const handleFetch = async () => {
    try {
      const data = await callApi(`/v1/repositories?most_starred=${input}&page=${page}`);
      setRepositories(data);
    } catch (error) {
      setRepositories([]);
    }
  };

  // if page number is 1, manually call handleFetch, else useEffect will automatically call handleFetch
  const handleSearch = async () => {
    if(page === 1){
      handleFetch()
    }
    else{
      setPage(1)
    }
  }

  return (
    <div className="d-flex flex-column justify-content-between" style={{ height: 'calc(100vh - 30px)' }}>
      <div>
      <h2 style={{ color: '#218838' }} className="display-6">Most starred repositories.</h2>
      <Col lg={{ span: 6, offset: 3 }}>
        <SearchForm 
          title={"Enter a number to get N most starred repositories"}
          searchField={input}
          setSearchField={setInput}
          onSearch={handleSearch}
          onRefresh={null}
          placeholder={"Enter a number N"}
        />
      </Col>
      </div>
      <Col lg={{ span: 8, offset: 2 }}>
        <RepositoriesTable repositories={repositories} />
      </Col>
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

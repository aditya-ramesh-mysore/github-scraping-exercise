import React, { useEffect, useState } from 'react';
import RepositoriesTable from '../components/RepositoriesTable';
import axios from "../api"
import SearchForm from '../components/SearchForm';
import PaginationComponent from '../components/PaginationComponent';
import { useAlert } from '../hooks/useAlert';


export default function StarredProjectsPage() {
  const [n, setN] = useState(null);
  const [repositories, setRepositories] = useState([]);
  const [page, setPage] = useState(1);
  const showAlert = useAlert();

  useEffect(() => {
    if(n){
      handleFetch();
    }
  }, [page]);

  const handleFetch = async () => {
    try {
      const response = await axios.get(`/v1/repositories?recent=${n}&page=${page}`);
      setRepositories(response.data);
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
      <h2 style={{ color: '#218838' }} className="display-6">Most starred repositories.</h2>
      <SearchForm 
        title={"Enter a number to get N most starred repositories"}
        searchField={n}
        setSearchField={setN}
        onSearch={handleSearch}
        onRefresh={null}
        placeholder={"Enter a number N"}
      />
      </div>
    
      <RepositoriesTable repositories={repositories} />
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

import React from 'react';
import Pagination from 'react-bootstrap/Pagination'

export default function PaginationComponent({page, setPage, hasMore}) {
  return (
    <Pagination className="mt-4 d-flex justify-content-center">
        <Pagination.Prev onClick={() => setPage(page => page - 1)} disabled={page === 1} />
        <Pagination.Item>{page}</Pagination.Item>
        <Pagination.Next onClick={() => setPage(page => page + 1)} disabled={!hasMore} />
    </Pagination>
  );
}
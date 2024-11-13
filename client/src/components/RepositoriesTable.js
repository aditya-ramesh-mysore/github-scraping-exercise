import React from 'react';
import Table from 'react-bootstrap/Table'

export default function RepositoriesTable({repositories}) {
  return (
    <React.Fragment>
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
                  <td>{repo.description || <em>{"(Description unavailable)"}</em>}</td>
                  <td>{repo.stars || 0}</td>
                  <td>{repo.forks || 0}</td>
                </tr>
              ))}
            </tbody>
          </Table>
        )}
    </React.Fragment>
  );
}

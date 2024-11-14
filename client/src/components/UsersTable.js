import React from 'react';
import Table from 'react-bootstrap/Table';

export default function UsersTable({users}) {
    return (
        <React.Fragment>
            {users.length > 0 && (
              <Table striped bordered responsive className="mt-6">
                <thead>
                  <tr>
                    <th style={{width: 200}}>Most Recent Users</th>
                  </tr>
                </thead>
                <tbody>
                  {users.map((user, index) => (
                    <tr key={index}>
                      <td>{user.username}</td>
                    </tr>
                  ))}
                </tbody>
              </Table>
            )}
        </React.Fragment>
    );
}

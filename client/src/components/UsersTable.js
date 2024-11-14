import React from 'react';
import Table from 'react-bootstrap/Table';
import { formatTime } from '../utils/formatTime';

export default function UsersTable({users}) {
    return (
        <React.Fragment>
            {users.length > 0 && (
              <Table striped bordered responsive className="mt-6">
                <thead>
                  <tr>
                    <th style={{width: 200}}>Most Recent Users</th>
                    <th style={{width: 140}}>Saved At</th>
                  </tr>
                </thead>
                <tbody>
                  {users.map((user, index) => (
                    <tr key={index}>
                      <td>{user.username}</td>
                      <td>{formatTime(user.created_at)}</td>
                    </tr>
                  ))}
                </tbody>
              </Table>
            )}
        </React.Fragment>
    );
}

import React from 'react';
import Form from 'react-bootstrap/Form'
import Button from 'react-bootstrap/Button';

// Form has three components: Input field, search button, optionally refresh button
export default function SearchForm({
    title,
    searchField,
    setSearchField,
    onSearch,
    onRefresh,
    placeholder
}) {
    return (
        <Form className="mb-4">
            <p>{title}</p>
            <Form.Group controlId="formUsername" className='d-flex justify-content-center'>
                <Form.Control
                    type="text"
                    placeholder={placeholder}
                    value={searchField}
                    required
                    onChange={(e) => setSearchField(e.target.value)}/>
            </Form.Group>
            <Button variant="success" onClick={onSearch} className="mt-2">
                Search
            </Button>
            {onRefresh
                ? <Button variant="secondary" onClick={onRefresh} className="mt-2 ms-2">
                        Refresh
                    </Button>
                : null}

        </Form>
    );
}

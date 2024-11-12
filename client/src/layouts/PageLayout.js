import Button from 'react-bootstrap/Button';
import React from 'react'; 
import Container from 'react-bootstrap/Container'
import Row from 'react-bootstrap/Row'
import Col from 'react-bootstrap/Col'

export default function PageLayout({children}) {
  return (
    <>
      <div
        className="landing-page text-center d-flex align-items-center justify-content-center"
        style={{
          backgroundImage: `url('/Background.jpg')`,
          backgroundSize: 'cover',
          backgroundPosition: 'center',
          height: '100vh',
          color: '#fff',
        }}
      >
        <Container>
          <Row>
            <Col lg={{ span: 6, offset: 3 }}>
              {children}
            </Col>
          </Row>
        </Container>
      </div>
    </>
  );
}
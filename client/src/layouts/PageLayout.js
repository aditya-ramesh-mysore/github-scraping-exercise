import Button from 'react-bootstrap/Button';
import React from 'react'; 
import Container from 'react-bootstrap/Container'
import Row from 'react-bootstrap/Row'
import Col from 'react-bootstrap/Col'
import { useLocation } from 'react-router-dom';

export default function PageLayout({children}) {
  const location = useLocation()

  let style = {
      backgroundImage: `url('/Background.jpg')`,
      backgroundSize: 'cover',
      backgroundPosition: 'center',
      backgroundRepeat: 'no-repeat',
      height: '100vh',
      width: '100vw',
      margin: 0,
      padding: 0,
      color: '#fff',
  }
  
  if(location.pathname != "/"){
    style = {
      backgroundColor: 'rgb(210, 218, 210)',
      backgroundSize: 'cover',
      backgroundPosition: 'center',
      backgroundRepeat: 'no-repeat',
      height: '100vh',
      width: '100vw',
      margin: 0,
      padding: 0,
      color: '#fff',
    }
  }
  
  return (
    <>
      <div
        className="landing-page text-center d-flex align-items-center justify-content-center"
        style={style}
      >
        <Container>
          <Row>
            <Col lg={{ span: 8, offset: 2 }}>
              {children}
            </Col>
          </Row>
        </Container>
      </div>
    </>
  );
}

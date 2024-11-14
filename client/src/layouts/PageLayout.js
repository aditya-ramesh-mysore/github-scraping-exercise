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
      backgroundRepeat: 'repeat',
      overflow: 'auto',
      height: '100vh',
      width: '100vw',
      margin: 0,
      padding: 0,
      color: '#fff',
  }
  
  if(location.pathname !== "/"){
    style = {
      backgroundImage: `url('/Background2.jpg')`,
      backgroundSize: 'cover',
      backgroundPosition: 'center',
      overflow: 'auto',
      backgroundRepeat: 'repeat',
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
            <Col>
              {children}
            </Col>
          </Row>
        </Container>
      </div>
    </>
  );
}

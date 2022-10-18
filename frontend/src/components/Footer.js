import React from 'react'
import {Navbar, Nav, Container, NavDropdown} from 'react-bootstrap'
import {LinkContainer} from 'react-router-bootstrap'


function Footer() {
    return (
      <Navbar fixed='bottom' bg="primary" variant="dark">
      <Container>
        <Nav className="me-auto">
          <Nav.Link href="/">Home</Nav.Link>
          <Nav.Link >Features</Nav.Link>
          <Nav.Link >Pricing</Nav.Link>
        </Nav>
      </Container>
      </Navbar>
    )
}

export default Footer

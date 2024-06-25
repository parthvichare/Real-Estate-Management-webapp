// src/components/Navbar.js
import React from 'react';
import styled from 'styled-components';
import { Link } from 'react-router-dom';
import '../App.css';


const NavbarContainer = styled.div`
  background-color: red;
  padding: 10px 20px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  border-bottom: 1px solid #ddd;
`;

const Log = styled.div`
  font-size: 24px;
  font-weight: bold;
  color: white;
`;

const NavLinks = styled.div`
  display: flex;
  gap: 15px;
`;

const NavLink = styled.div`
  text-decoration: none;
  color: white;
  font-weight: 500;
  padding: 10px;
  cursor: pointer;
  &:hover {
    color: #ff5a5f;
  }
`;

const Dropdown = styled.div`
  position: relative;
  display: inline-block;
`;

const DropdownContent = styled.div`
  display: none;
  position: absolute;
  background-color: #f9f9f9;
  min-width: 160px;
  box-shadow: 0px 8px 16px 0px rgba(0,0,0,0.2);
  z-index: 1;
  
  ${Dropdown}:hover & {
    display: block;
  }
`;

const DropdownLink = styled.div`
  color: black;
  padding: 12px 16px;
  text-decoration: none;
  display: block;
  cursor: pointer;

  &:hover {
    background-color: #f1f1f1;
  }
`;


const Navbar = () => {
  return (
    <NavbarContainer>
      <Log>MagicBricks</Log>
      <NavLinks>
        <NavLink>
        <Link to="/home" class='nav'>Home</Link>
        </NavLink>
        <NavLink>
        <Link to="/DataFrame" class='nav'>DataFrame</Link>
        </NavLink>
        <NavLink>
          <Link to="/Pricefilter" class='nav'>Pricefilter</Link>
        </NavLink>
        {/* <NavLink>Contact</NavLink> */}
      </NavLinks>
    </NavbarContainer>
  );
};

export default Navbar;

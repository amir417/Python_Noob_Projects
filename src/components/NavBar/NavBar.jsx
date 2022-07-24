import React, { useState } from 'react';
import './Navbar.css';
import { NavLink } from 'react-router-dom';
import { logo, MenuBar, MenuX } from './imports.js';

const Menu = () => (
  <>
    <p><NavLink to="/" className="navbar__links">Home</NavLink></p>
    <p><NavLink to="/projects" className="navbar__links">Projects</NavLink></p>
    <p><NavLink to="/apply" className="navbar__links">Apply</NavLink></p>
  </>
)

const NavBar = () => {
  const [toggleMobileMenu, updateToggleStatus] = useState(false);

  return (
    <>
      <div className="navbar">
        <div className="navbar__logo">
          <NavLink to="/">
            <img src={logo} alt="" />
          </NavLink>
        </div>
        
        <div className="navbar__desktop">
          <Menu />
        </div>

        <div className="navbar__mobile_menu">
          {toggleMobileMenu 
            ? <img src={MenuX} alt="" onClick={() => updateToggleStatus(false)} />
            : <img src={MenuBar} alt="" onClick={() => updateToggleStatus(true)}/>
          }
          
          {toggleMobileMenu && (
            <div className="navbar__mobile_menu-box swirl-in-fwd">
              <Menu />
            </div>
          )}
        </div>
      </div>
    </>
  )
}

export default NavBar
import React from "react";
import logo from "../Assets/logo.jpeg";

const Navbar = () => {

  return (
    <nav className="navbar navbar-expand-lg navbar-light bg-light">
      <div className="container-fluid d-flex justify-content-between align-items-center">
        <div className="navbar-brand">
          <img
            src={logo}
            alt="Logo"
            style={{ width: "70px", height: "60px" }}
          />
        </div>

        <button className="btn btn-primary" >
          Get Started
        </button>
      </div>
    </nav>
  );
};

export default Navbar;

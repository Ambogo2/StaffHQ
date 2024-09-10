import React from "react";
import emp from "../Assets/emp.jpg";
import axios from "axios"
import { useState } from "react";

const Hero = () => {
  return (
    <div className="jumbotron jumbotron-fluid" id="hero">
      <div className="container">
        <div className="row align-items-center">
          {/* Left Column: Image */}
          <div className="col-md-6">
            <img
              src={emp}
              alt="Hero"
              className="img-fluid"
              style={{ maxHeight: "400px", objectFit: "cover" }}
            />
          </div>

          {/* Right Column: Heading, Text, Button */}
          <div className="col-md-6">
            <h1 className="display-4">
              A Streamlined Workplace all in One Space
            </h1>
            <p className="lead">
              An employee management system with all work operations centralized in one hub. A system built to improve 
              productivity and increase efficiency.
            </p>
            <a href="#features" className="btn btn-primary btn-lg mt-3">
              Learn More
            </a>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Hero;

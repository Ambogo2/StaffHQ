import React from "react";
import team from "../Assets/teamwork.jpg";

const About= () => {
  return (
    <div className="jumbotron jumbotron-fluid" id="hero">
      <div className="container">
        <div className="row align-items-center">
          {/* Left Column: Image */}
          <div className="col-md-6">
            <img
              src={team}
              alt="Hero"
              className="img-fluid"
              style={{ maxHeight: "400px", objectFit: "cover" }}
            />
          </div>

          {/* Right Column: Heading, Text, Button */}
          <div className="col-md-6">
            <h2 className="display-4">
              Our Story
            </h2>
            <p className="lead">
              Juggling different tools can be daunting especiaaly for organizations that relies
              on different tools and traditional filing systems to store their reports.With StaffHQ,the
              hassle is gone. We believe in efficiency and optimized workflows for a better work experience.
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

export default About;

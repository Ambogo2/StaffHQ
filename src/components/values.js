import React from "react";
import video from "../Assets/vid.mp4"

const Values = () => {
  return (
    <div className="jumbotron jumbotron-fluid" id="values">
      <div className="container">
        <div className="row align-items-center">
          {/* Left Column: Heading and Bullet List */}
          <div className="col-md-6">
            <h1 className="display-4">Our Core Values</h1>
            <ul className="list-unstyled mt-4">
              <li>
                <i className="bi bi-check-circle-fill"></i> Efficiency
              </li>
              <li>
                <i className="bi bi-check-circle-fill"></i> Automation
              </li>
              <li>
                <i className="bi bi-check-circle-fill"></i> Productivity
              </li>
              <li>
                <i className="bi bi-check-circle-fill"></i> Effectiveness
              </li>
            </ul>
          </div>

          {/* Right Column: Video */}
          <div className="col-md-6">
            <div className="embed-responsive embed-responsive-16by9">
              <iframe
                className="embed-responsive-item"
                src={video}
                allowFullScreen
                title="Values Video"
              ></iframe>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Values;

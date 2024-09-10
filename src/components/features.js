import React from "react";

const Features = () => {
  return (
    <section id="features" className="py-5 bg-light">
      <div className="container">
        <h1 className="text-center mb-4">Features</h1>
        <div className="row">
          <div className="col-md-3">
            <div className="card">
              <div className="card-body text-center">
                <h5 className="card-title">Employee Tracking</h5>
                <p className="card-text">
                  Manage employees efficiently with our intuitive dashboard.
                </p>
              </div>
            </div>
          </div>
          <div className="col-md-3">
            <div className="card">
              <div className="card-body text-center">
                <h5 className="card-title">Centralized Reporting</h5>
                <p className="card-text">
                  Monitor the status and performance of various departments.
                </p>
              </div>
            </div>
          </div>
          <div className="col-md-3">
            <div className="card">
              <div className="card-body text-center">
                <h5 className="card-title">Leave Requests Management</h5>
                <p className="card-text">
                  Monitor the status and performance of various departments.
                </p>
              </div>
            </div>
          </div>
          <div className="col-md-3">
            <div className="card">
              <div className="card-body text-center">
                <h5 className="card-title">Appointment Booking</h5>
                <p className="card-text">
                  Assign and manage tasks for employees in real-time.
                </p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
  );
};

export default Features;

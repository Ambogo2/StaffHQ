import React from "react";
import { FaTwitter, FaFacebook } from "react-icons/fa"; // Import icons from react-icons

const Footer = () => {
  return (
    <footer className="bg-dark text-white text-center py-4">
      <div className="container">
        <div className="row justify-content-center mb-3">
          {/* Social Media Icons */}
          <div className="col-auto">
            <a
              href="https://twitter.com"
              className="text-white mx-2"
              aria-label="Twitter"
            >
              <FaTwitter size={24} />
            </a>
            <a
              href="https://facebook.com"
              className="text-white mx-2"
              aria-label="Facebook"
            >
              <FaFacebook size={24} />
            </a>
          </div>
        </div>
        {/* Company Name */}
        <div className="row">
          <div className="col">
            <p className="mb-0">
              &copy; 2024 <strong>StaffHQ</strong>. All Rights Reserved.
            </p>
          </div>
        </div>
      </div>
    </footer>
  );
};

export default Footer;

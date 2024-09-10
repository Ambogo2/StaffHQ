import React from "react";
import Navbar from "../navbar";
import Hero from "../hero";
import Values from "../values";
import Features from "../features";
import About from "../about";
import Footer from "../footer";

const Home = () => {
  return (
    <div className="home-container">
      <Navbar />
      <Hero />
      <Values />
      <Features />
      <About />
      <Footer />
    </div>
  );
};

export default Home;

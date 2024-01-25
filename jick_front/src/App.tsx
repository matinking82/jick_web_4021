import SignIn from "./pages/Signin";
import "./App.css";
import AfterLogin from "./pages/AfterLogin";
import { useState } from "react";
import { Link } from "react-router-dom";

function App() {
  let isAuthenticated = false;

  if (localStorage.getItem("token")) {
    isAuthenticated = true;
  }

  if (isAuthenticated) {
    return (
      <>
        <AfterLogin />
      </>
    );
  } else {
    return <SignIn />;
  }
}

export default App;

import { RouterProvider, createBrowserRouter } from "react-router-dom";
import "./Signin.css";
import React, { useState } from "react";
import { Link } from "react-router-dom";
import { login, register } from "../Api/Authentication";

const SignIn = () => {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  return (
    <>
      <section className="signin--instruction">
        <h1>Welcome Back!</h1>
        <p>sign in to your account</p>
      </section>

      <section className="signin--information">
        <input
          type="text"
          value={email}
          onChange={(e) => {
            setEmail(e.target.value);
          }}
          placeholder="Enter your email address"
        />
        <input
          type="password"
          value={password}
          onChange={(e) => {
            setPassword(e.target.value);
          }}
          placeholder="Enter your password"
        />
        <button
          onClick={(e) => {
            if (email === "" || password === "") {
              alert("Please fill in all fields");
              return;
            }
            login(email, password).then((res) => {
              if (res) {
                localStorage.setItem("token", res.token);
                window.location.reload();
              } else {
                alert("Wrong email or password");
              }
            });
          }}
        >
          Sign in
        </button>
      </section>

      <section className="signin--switch">
        <p>Dont have an account? Let's</p>
        <Link to={"/signup"}>Sign up</Link>
      </section>
    </>
  );
};

const Signup = () => {
    const [email, setEmail] = useState("");
    const [password, setPassword] = useState("");
  return (
    <>
      <section className="signin--instruction">
        <h1>Create an account</h1>
        <p>Sign up to get started</p>
      </section>

      <section className="signin--information">
        <input type="text" value={email} onChange={
            e=>{
                setEmail(e.target.value);
            }
        } placeholder="Enter your email address" />
        <input type="password" value={password} onChange={
            e=>{
                setPassword(e.target.value);
            }
        } placeholder="Enter your password" />
        <button onClick={e=>{
            if(email==="" || password===""){
                alert("Please fill in all fields");
                return;
            }
            register(email, password).then(res=>{
                if(res){
                    alert("Sign up successfully");
                }else{
                    alert("Something went wrong");
                }
            })
        }}>Sign up</button>
      </section>

      <section className="signin--switch">
        <p>Already have an account? Let's</p>
        <Link to={"/"}>Sign in</Link>
      </section>
    </>
  );
};

const Sign = () => {
  let router = createBrowserRouter([
    {
      path: "/",
      element: <SignIn />,
    },
    {
      path: "/signup",
      element: <Signup />,
    },
  ]);

  return (
    <React.StrictMode>
      <RouterProvider router={router} />
    </React.StrictMode>
  );
};

export default Sign;

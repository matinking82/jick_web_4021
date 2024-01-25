import React from "react";
import { createBrowserRouter, RouterProvider } from "react-router-dom";
import Logout from "./Logout";
import Home from "./Home";
import Profile from "./Profile";

const AfterLogin = () => {
  let router = createBrowserRouter([
    {
      path: "/",
      element: <Home />,
      //   loader: HomeLoader,
    },
    {
      path: "/logout",
      element: <Logout />,
    },
    {
      path: "*",
      element: <div>Not Found</div>,
    },
    {
      path: "/profile",
      element: <Profile />,
    },
  ]);

  return (
    <React.StrictMode>
      <RouterProvider router={router} />
    </React.StrictMode>
  );
};

export default AfterLogin;

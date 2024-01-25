import SignIn from "./pages/Signin";
import "./App.css";
import AfterLogin from "./pages/AfterLogin";

function App() {
  let isAuthenticated = false;

  if (localStorage.getItem("token")) {
    isAuthenticated = true;
  }

  if (isAuthenticated) {
    return (
      <AfterLogin />
    );
  } else {
    return (
      <SignIn />
    );
  }
}

export default App;

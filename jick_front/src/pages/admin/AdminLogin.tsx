import { useState } from "react";
import '../Signin.css';
import { AdminLoginService } from "../../Api/admin/adminAuth";

const AdminLogin = () => {
  if (localStorage.getItem("admintoken") !== null) {
    window.location.href = "/admin";
  }
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  return (
    <>
      <section className="signin--instruction">
        <h1>Admin Login</h1>
        <p>login to your account</p>
      </section>

      <section className="signin--information">
        <input
          type="text"
          value={username}
          onChange={(e) => {
            setUsername(e.target.value);
          }}
          placeholder="Enter your username"
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
            if (username === "" || password === "") {
              alert("Please fill in all fields");
              return;
            }
            AdminLoginService(username, password).then((res) => {
                if (res) {
                    alert("Login Successful");
                    localStorage.setItem("admintoken", res.token);
                    window.location.href = "/admin";
                } else {
                    alert("Login Failed");
                }
            });
            //TODO
          }}
        >
          login
        </button>
      </section>
    </>
  );
};

export default AdminLogin;

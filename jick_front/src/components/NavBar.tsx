import { useEffect, useState } from "react";
import { Link } from "react-router-dom";
import { profile } from "../interfaces/user";
import { getUserProfile } from "../Api/User";

const NavBar = () => {
  const [search, setSearch]: [string, any] = useState("");
  const [profile, setProfile]: [profile, any] = useState(null);
  useEffect(() => {
    getUserProfile().then((res) => {
      setProfile(res);
      console.log(res);
    });
  }, []);

  let prof = <>profile</>;

  if (profile) {
    prof = <>profile: {profile.email}</>;
  }

  return (
    <nav className="main-nav navbar navbar-expand-lg navbar-light bg-light">
      <div className="container-fluid">
        <Link className="navbar-brand" to={"/"}>
          Jick Web
        </Link>
        <button
          className="navbar-toggler"
          type="button"
          data-bs-toggle="collapse"
          data-bs-target="#navbarSupportedContent"
          aria-controls="navbarSupportedContent"
          aria-expanded="false"
          aria-label="Toggle navigation"
        >
          <span className="navbar-toggler-icon"></span>
        </button>
        <div className="collapse navbar-collapse" id="navbarSupportedContent">
          <ul className="navbar-nav me-auto mb-2 mb-lg-0">
            <li className="nav-item">
              <Link
                className="nav-link active"
                aria-current="page"
                to={"/profile"}
              >
                {prof}
              </Link>
            </li>
            <li className="nav-item">
              <Link className="nav-link" to={"/post"}>
                Create Post
              </Link>
            </li>
            <li className="nav-item">
              <Link className="nav-link" to={"/explore"}>
                Explore
              </Link>
            </li>
            <li className="nav-item">
              <Link className="nav-link" to={"/logout"}>
                Log out
              </Link>
            </li>
          </ul>
          <div className="d-flex">
            <input
              className="form-control me-2"
              type="search"
              placeholder="Search For People"
              aria-label="Search"
              value={search}
              onChange={(e) => {
                setSearch(e.target.value);
              }}
            ></input>
            <button
              className="btn btn-outline-success"
              onClick={(e) => {
                if (search === "") {
                  alert("Please enter a search term");
                  return;
                }
                window.location.href = `/search/${search}`;
              }}
            >
              Search
            </button>
          </div>
        </div>
      </div>
    </nav>
  );
};

export default NavBar;

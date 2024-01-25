import { Link } from "react-router-dom";

const AdminNavBar = () => {
  return (
    <nav className="main-nav navbar navbar-expand-lg navbar-light bg-light">
      <div className="container-fluid">
        <Link className="navbar-brand" to={"/admin"}>
          Jick Web Admin
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
            {/* <li className="nav-item">
              <Link
                className="nav-link active"
                aria-current="page"
                to={"/profile"}
              >
                Profile
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
            </li> */}
            <li className="nav-item">
              <Link className="nav-link" to={"/admin/posts/0"}>
                posts
              </Link>
            </li>

            <li className="nav-item">
              <Link className="nav-link" to={"/admin/users/0"}>
                users
              </Link>
            </li>

            <li className="nav-item">
              <Link className="nav-link" to={"/admin/logout"}>
                Log out
              </Link>
            </li>
          </ul>
        </div>
      </div>
    </nav>
  );
};

export default AdminNavBar;

import { Link } from "react-router-dom";
import { followUser, unfollowUser } from "../Api/User";
import { searchUserResponse } from "../interfaces/user";

const SearchUserCard = (props) => {
  let { result }: { result: searchUserResponse } = props;
  let follow = (
    <button
      className="btn btn-outline-primary"
      onClick={() => {
        followUser(result.username).then((res) => {
          if (res) {
            window.location.reload();
          }
        });
      }}
    >
      Follow
    </button>
  );
  if (result.isFollowing) {
    follow = (
      <button
        className="btn btn-primary"
        onClick={() => {
          unfollowUser(result.username).then((res) => {
            if (res) {
              window.location.reload();
            }
          });
        }}
      >
        Unfollow
      </button>
    );
  }
  return (
    <div className="row search-user-card">
      <div className="col-9">
        <p>{result.full_name}</p>
        <Link to={"/posts/" + result.email}>
          <h5>username :{result.username}</h5>
        </Link>
        <p>email :{result.email}</p>
        <span>joined at: {result.create_date}</span>
      </div>
      <div className="col-3">{follow}</div>
    </div>
  );
};

export default SearchUserCard;

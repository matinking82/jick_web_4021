import { Link } from "react-router-dom";
import { LikePost } from "../Api/Posts";
import { Post } from "../interfaces/post";

const PostCard = (props) => {
  let { post }: { post: Post } = props;
  return (
    <div>
      <div className="post-main-card" key={post.id}>
        <Link to={'/posts/'+post.senderEmail}>
          <h5 className="text-primary">Sender: {post.senderEmail}</h5>
        </Link>
        <h3 className="p-3 my-5 border">{post.text}</h3>
        <p className="text-muted">Posted on: {post.create_date}</p>
        <button
          className="btn btn-lg btn-primary"
          onClick={() => {
            LikePost(post.id).then((res) => {
              console.log(res);
              if (res) {
                window.location.reload();
              }
            });
          }}
        >
          Like
        </button>
        <span className="boreer p-2 rounded">Likes:{post.likes}</span>
      </div>
    </div>
  );
};

export default PostCard;

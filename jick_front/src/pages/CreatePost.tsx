import React, { useState } from "react";
import NavBar from "../components/NavBar";
import { SendPost } from "../Api/Posts";

const CreatePost: React.FC = () => {
  const [text, setText] = useState("" as string);
  return (
    <>
      <NavBar />
      <div className="center-item">
        <div className="create-post-form">
          <h3>Write your post :</h3>
          <textarea
            className="form-control"
            placeholder="Write your post here"
            rows={3}
            value={text}
            onChange={(e) => setText(e.target.value)}
          />
          <button
            className="btn btn-success my-3 width-100"
            onClick={() => {
              console.log(text);
              SendPost(text).then((res) => {
                console.log(res);
                if (res) {
                  alert("Post sent successfully");
                  window.location.href = "/";
                }
              });
            }}
          >
            Send
          </button>
        </div>
      </div>
    </>
  );
};

export default CreatePost;

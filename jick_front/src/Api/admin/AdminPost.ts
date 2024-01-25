import { Post } from "../../interfaces/post";
import { API_URL } from "../Vars";

export const getAllPosts = async (page: number) => {
  let url = API_URL + "/admin/post/get/" + page;
  let token = localStorage.getItem("admintoken");
  let response = await fetch(url, {
    method: "GET",
    headers: {
      "Content-Type": "application/json",
      Authorization: `Bearer ${token}`,
    },
  });

  if (response.ok) {
    return (await response.json()) as Post[];
  }
};

export const deletePost = async (postId: number) => {
  let url = API_URL + "/admin/post/delete/" + postId;
  let token = localStorage.getItem("admintoken");
  let response = await fetch(url, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      Authorization: `Bearer ${token}`,
    },
  });

  if (response.ok) {
    return true;
  }
};

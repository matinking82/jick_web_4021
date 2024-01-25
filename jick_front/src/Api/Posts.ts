import { API_URL } from "./Vars";
import { Post } from "../interfaces/post";

export const GetHomePosts = async () => {
  let url = API_URL + "/post/all";
  let token = localStorage.getItem("token");
  let response = await fetch(url, {
    method: "GET",
    headers: {
      "Content-Type": "application/json",
      Authorization: `Bearer ${token}`,
    },
  });

  if (response.ok) {
    let res = (await response.json()) as Post[];
    console.log(res);

    return res;
  }
};

export const LikePost = async (postId: number) => {
  let url = API_URL + "/post/react/" + postId;
  let token = localStorage.getItem("token");
  let response = await fetch(url, {
    method: "GET",
    headers: {
      "Content-Type": "application/json",
      Authorization: `Bearer ${token}`,
    },
  });

  if (response.ok) {
    let res = (await response.json()) as boolean;
    console.log(res);

    return res;
  }
};

export const SendPost = async (text: string) => {
  let url = API_URL + "/post/create";
  let token = localStorage.getItem("token");
  let data = {
    text: text,
    senderId: 0,
  };

  console.log(data);
  
  let response = await fetch(url, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      Authorization: `Bearer ${token}`,
    },
    body: JSON.stringify(data),
  });

  if (response.ok) {
    let res = (await response.json()) as boolean;
    console.log(res);

    return res;
  }
};

export const GetMyPosts = async () => {
  let url = API_URL + "/post/get";
  let token = localStorage.getItem("token");

  let response = await fetch(url, {
    method: "GET",
    headers: {
      "Content-Type": "application/json",
      Authorization: `Bearer ${token}`,
    },
  });

  if (response.ok) {
    let res = (await response.json()) as Post[];
    console.log(res);

    return res;
  }
};

export const GetPostsForUser = async (email: string) => {
  let url = API_URL + "/post/get/" + email;
  let token = localStorage.getItem("token");

  let response = await fetch(url, {
    method: "GET",
    headers: {
      "Content-Type": "application/json",
      Authorization: `Bearer ${token}`,
    },
  });

  if (response.ok) {
    let res = (await response.json()) as Post[];
    console.log(res);

    return res;
  }
};

export const GetExplorePosts = async () => {
  let url = API_URL + "/post/explore";
  let token = localStorage.getItem("token");

  let response = await fetch(url, {
    method: "GET",
    headers: {
      "Content-Type": "application/json",
      Authorization: `Bearer ${token}`,
    },
  });

  if (response.ok) {
    let res = (await response.json()) as Post[];
    console.log(res);

    return res;
  }
};

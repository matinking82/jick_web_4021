import { user } from "../../interfaces/user";
import { API_URL } from "../Vars";

export const getAllUsers = async (page: number) => {
  let url = API_URL + "/admin/user/get/" + page;
  let token = localStorage.getItem("admintoken");
  let response = await fetch(url, {
    method: "GET",
    headers: {
      "Content-Type": "application/json",
      Authorization: `Bearer ${token}`,
    },
  });

  if (response.ok) {
    return (await response.json()) as user[];
  }
};

export const ActivateUser = async (userId: number) => {
  let url = API_URL + "/admin/user/Activate/" + userId;
  let token = localStorage.getItem("admintoken");
  let response = await fetch(url, {
    method: "GET",
    headers: {
      "Content-Type": "application/json",
      Authorization: `Bearer ${token}`,
    },
  });

  if (response.ok) {
    return true;
  }
};

export const DeactivateUser = async (userId: number) => {
  let url = API_URL + "/admin/user/DeActivate/" + userId;
  let token = localStorage.getItem("admintoken");
  let response = await fetch(url, {
    method: "GET",
    headers: {
      "Content-Type": "application/json",
      Authorization: `Bearer ${token}`,
    },
  });

  if (response.ok) {
    return true;
  }
};

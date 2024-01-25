import { stats } from "../../interfaces/stats";
import { API_URL } from "../Vars";

export const getStatistics = async () => {
  let url = API_URL + "/admin/stats/get";
  let token = localStorage.getItem("admintoken");
  let response = await fetch(url, {
    method: "GET",
    headers: {
      "Content-Type": "application/json",
      Authorization: `Bearer ${token}`,
    },
  });

  if (response.ok) {
    return (await response.json()) as stats;
  }
};

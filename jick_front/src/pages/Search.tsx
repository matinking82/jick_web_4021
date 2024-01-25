import { useParams } from "react-router-dom";
import NavBar from "../components/NavBar";
import { searchUserResponse } from "../interfaces/user";
import { useEffect, useState } from "react";
import { searchUsers } from "../Api/User";
import SearchUserCard from "../components/SearchUserCard";

const Search = () => {
  const { search } = useParams<{ search: string }>();
  const [results, setResults]: [searchUserResponse[], any] = useState([]);

  useEffect(() => {
    searchUsers(search).then((res) => {
      setResults(res);
      console.log(res);
    });
  }, []);
  return (
    <>
      <NavBar />
      <div>
        {/* Your search component code goes here */}
        <p>Search key: {search}</p>

        <span>
          {results?.map((result: searchUserResponse) => {
            return <SearchUserCard result={result} />;
          })}
        </span>
      </div>
    </>
  );
};

export default Search;

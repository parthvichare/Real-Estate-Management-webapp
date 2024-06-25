// import axios from 'axios';
// import React, { useEffect, useState } from 'react';
// import './App.css';

// const PostList = () => {
//   const [posts, setPosts] = useState([]);  // Initial state is an empty array

//   useEffect(() => {
//     axios.get('http://localhost:8000/api/posts/')
//       .then(response => {
//         console.log(response.data);  // Log the response data
//         setPosts(response.data);  // Ensure this is an array
//       })
//       .catch(error => {
//         console.error('There was an error fetching the posts!', error);
//       });
//   }, []);

//   return (
//     <div className="post-list">  {/* Apply CSS class */}
//       <h1>Post List</h1>
//       <ul>
//         {Array.isArray(posts) && posts.map(post => (  // Ensure posts is an array before mapping
//           <li key={post.id}>  {/* Add a unique key */}
//             <strong>{post.name}</strong>
//             <p>{post.price}</p>
//             <br></br>
//             <p>{post.create_at}</p>
//             <p>{post.updated_at}</p>
//           </li>
//         ))}
//       </ul>
//     </div>
//   );
// };

// export default PostList;

// Here we Route all the Pages and Fetch the content from the database

import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Navbar from './components/Navbar';
import DataFrame from './DataFrame';
import Home from './Home';
import PriceFilter from './Pricefilter';

const App = () => {
  return (
    <Router>
      <div>
        <Navbar/>
        <Routes>
          <Route path="/home" element={<Home />} />
          <Route path="/DataFrame" element={<DataFrame />} />
          <Route path="/Pricefilter" element={<PriceFilter />} />
        </Routes>
      </div>
    </Router>
  );
};

export default App;

// src/App.js
// import React from 'react';
// import Navbar from './components/Navbar';
// import Navbar from './components/home';

// function App() {
//   return (
//     <div>
//       <Navbar />
//       <home/>
//       {/* Other components go here */}
//     </div>
//   );
// }

// export default App;

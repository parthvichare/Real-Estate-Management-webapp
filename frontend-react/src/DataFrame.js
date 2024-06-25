import React, { useState, useEffect } from 'react';
import axios from 'axios';
import './App.css';
import * as XLSX from 'xlsx';
import downloadlogo from './images.png'

const DataFrame = () => {
  const [context, setContext] = useState(null);
  const [posts, setPosts] = useState([]);
  const [loading, setLoading] = useState(true);
  const [updatingPost, setUpdatingPost] = useState(null);
  const [error, setError] = useState(null);

  useEffect(() => {
    // Fetch context and posts data from APIs
    const fetchContext = axios.get('http://127.0.0.1:8000/api/my_context/');
    const fetchPosts = axios.get('http://127.0.0.1:8000/api/posts/');

    Promise.all([fetchContext, fetchPosts])
      .then(([contextResponse, postsResponse]) => {
        setContext(contextResponse.data);
        setPosts(postsResponse.data);
        setLoading(false);
      })
      .catch(error => {
        setError(error);
        setLoading(false);
      });
  }, []);

  const handleDelete = (id) => {
    // Simulating deletion (replace with actual deletion logic)
    setPosts(posts.filter(post => post.id !== id));
  };

  const handleUpdate = (post) => {
    setUpdatingPost(post); // Set the post to be updated
  };

  const handleChange = (e) => {
    const { name, value } = e.target;
    setUpdatingPost({
      ...updatingPost,
      [name]: value
    });
  };
  const handleDownload = () => {
    // Convert posts data to Excel format
    const worksheet = XLSX.utils.json_to_sheet(posts);

    // Create a workbook
    const workbook = XLSX.utils.book_new();
    XLSX.utils.book_append_sheet(workbook, worksheet, 'Posts');

    // Save workbook to a file
    XLSX.writeFile(workbook, 'posts.xlsx');
  };

  const handleSubmitUpdate = () => {
    // Simulate update locally (replace with actual update logic)
    const updatedPosts = posts.map(post =>
      post.id === updatingPost.id ? updatingPost : post
    );
    setPosts(updatedPosts);
    setUpdatingPost(null); // Clear updatingPost state after update
  };

  if (loading) return <div>Loading...</div>;
  if (error) return <div>Error: {error.message}</div>;

  return (
    <div>
      <h1>Your Houselisting Dash-Board</h1>
      <button onClick={handleDownload} className="download-btn">
        Download
      </button>
      {context && <p className="title">{context.my_title}</p>}
      {Array.isArray(posts) && posts.length > 0 && (
        <table className="dataframe">
          <thead>
            <tr>
              <th>Name</th>
              <th>Beds</th>
              <th>Floor</th>
              <th>Image</th>
              <th>Furnishing</th>
              <th>Super Areas</th>
              <th>Area Sqft</th>
              <th>Delete</th>
              <th>Update</th>
            </tr>
          </thead>
          <tbody>
            {posts.map(post => (
              <tr key={post.id}>
                <td>{updatingPost && updatingPost.id === post.id ? (
                  <input type="text" name="name" value={updatingPost.name} onChange={handleChange} />
                ) : (
                  post.name
                )}</td>
                <td>{updatingPost && updatingPost.id === post.id ? (
                  <input type="text" name="beds" value={updatingPost.beds} onChange={handleChange} />
                ) : (
                  post.beds
                )}</td>
                <td>{updatingPost && updatingPost.id === post.id ? (
                  <input type="text" name="floor" value={updatingPost.floor} onChange={handleChange} />
                ) : (
                  post.floor
                )}</td>
                <td>
                  <img src={post.Image_url} className="image"/>
                </td>
                <td>{updatingPost && updatingPost.id === post.id ? (
                  <input type="text" name="furnishing" value={updatingPost.furnishing} onChange={handleChange} />
                ) : (
                  post.furnishing
                )}</td>
                <td>{updatingPost && updatingPost.id === post.id ? (
                  <input type="text" name="super_areas" value={updatingPost.super_areas} onChange={handleChange} />
                ) : (
                  post.super_areas
                )}</td>
                <td>{updatingPost && updatingPost.id === post.id ? (
                  <input type="text" name="area_sqft" value={updatingPost.area_sqft} onChange={handleChange} />
                ) : (
                  post.area_sqft
                )}</td>
                <td>
                  <button type='button' onClick={() => handleDelete(post.id)}>Delete</button>
                </td>
                <td>
                  {updatingPost && updatingPost.id === post.id ? (
                    <button type="button" onClick={handleSubmitUpdate}>Save</button>
                  ) : (
                    <button type="button" onClick={() => handleUpdate(post)}>Edit</button>
                  )}
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      )}
      {context && context.my_number && (
        <ul>
          {context.my_number.map((num, index) => (
            <li key={index}>{num}</li>
          ))}
        </ul>
      )}
    </div>
  );
};

export default DataFrame;
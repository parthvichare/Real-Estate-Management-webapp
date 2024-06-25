import React, { useState, useEffect } from 'react';
import axios from 'axios';
import './App.css';

const Pricefilter = () => {
  const [filteredPosts, setFilteredPosts] = useState([]);
  const [posts, setPosts] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [priceFilter, setPriceFilter] = useState('lac'); // Default filter is 'lac'

  useEffect(() => {
    const fetchFilteredPosts = async () => {
      try {
        setLoading(true);
        const response = await axios.get('http://127.0.0.1:8000/price_category/', {
          params: { price_filter: priceFilter }
        });
        setFilteredPosts(response.data.posts);
        setPosts([]); // Clear all posts when fetching filtered posts
        setLoading(false);
      } catch (error) {
        setError(error);
        setLoading(false);
      }
    };

    fetchFilteredPosts();
  }, [priceFilter]);

  const handleFilterChange = (filter) => {
    setPriceFilter(filter);
  };

  const fetchAllPosts = async () => {
    try {
      setLoading(true);
      const response = await axios.get('http://127.0.0.1:8000/price_category/');
      setPosts(response.data.posts);
      setFilteredPosts([]); // Clear filtered posts when fetching all posts
      setLoading(false);
    } catch (error) {
      setError(error);
      setLoading(false);
    }
  };

  if (loading) return <div>Loading...</div>;
  if (error) return <div>Error: {error.message}</div>;

  return (
    <div>
      <div>
        <button onClick={() => handleFilterChange('lac')}>Filter by Lac</button>
        <button onClick={() => handleFilterChange('cr')}>Filter by Crore</button>
        <button onClick={fetchAllPosts}>Show all</button>
      </div>
    <div>
    {filteredPosts.length > 0 ? (
          filteredPosts.map(post => (
            <ul key={post.property_id}>
              <h3>{post.name}</h3>
              <img src={post.Image_url} alt={post.name} className='image'/>
              <h4>{post.price}</h4>
              <h4>{post.beds}</h4>
              <h4>{post.super_areas}</h4>
              <h4>{post.furnishing}</h4>
            </ul>
          ))
        ) : (
          posts.map(post => (
            <ul key={post.property_id}>
              <h3>{post.name}</h3>
              <img src={post.Image_url} alt={post.name} className='image'/>
              <h4>{post.price}</h4>
              <h4>{post.beds}</h4>
              <h4>{post.super_areas}</h4>
              <h4>{post.furnishing}</h4>
            </ul>
          ))
        )}
      </div>
    </div>
  );
};

export default Pricefilter;
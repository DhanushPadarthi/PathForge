import React from 'react';

const ResourceCard = ({ title, description }) => {
  return (
    <div className="resource-card">
      <h3>{title}</h3>
      <p>{description}</p>
    </div>
  );
};

export default ResourceCard;

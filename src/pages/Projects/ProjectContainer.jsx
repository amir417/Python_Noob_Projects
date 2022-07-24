import React from 'react';
import './projects.css';

const ProjectContainer = ({name, type, founder, duration, role, complexity, commitment, description}) => {
  return (
    <>
      <div className="project__container-title">
        <p>
          {name}
        </p>
      </div>

      <div className="project__container-identifier">
        <p>
          Type: 
          <h1>
            {type}
          </h1>
        </p>

        <p>
          Founder: 
          <h1>
            {founder}
          </h1>
        </p>

        <p>
          Proposed Duration: 
          <h1>
            {duration}
          </h1>
        </p>

        <p>
          Role in Project: 
          <h1>
            {role}
          </h1>
        </p>

        <p>
          Complexity:
          <h1>
            {complexity}
          </h1>
        </p>

        <p>
          Commitment:
          <h1>
            {commitment}
          </h1>
        </p>
      </div>

      <div className="project__container-description">
        <p>
          Project Description:
          <br /><br />
          <h1>
            {description}
          </h1>
        </p>
      </div>
    </>
  )
}

export default ProjectContainer
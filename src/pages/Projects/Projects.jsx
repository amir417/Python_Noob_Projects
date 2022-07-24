import React from 'react';
import './projects.css';
import { Footer } from '../../components';
import ProjectContainer from './ProjectContainer';

const Projects = () => {
  return (
    <>
      <div className="projects section__padding">

        <h2>
          Projects
        </h2>

        <p>
          This page lists out all of the projects that are in demand and is looking 
          for suitable people to pair up with. If you think you are qualified to take
          on such projects, please reach out to the founder of the project OR fill out
          a Google Forms in the Apply section. Also, if your project has successfully
          taken place, please contact Codelaboration to remove your project
          so that this page is up to date. 
        </p>

        <ProjectContainer 
          name = {"Project #1"}
          type = {"Website Development for Professional Club"}
          founder = {"Sean Kim - Engineering Student"}
          duration = {"Approx. 1-3 years"}
          role = {"Backend developer"}
          complexity = {"Extremely difficult (PhD level)"}
          commitment = {"Equivalent of full-time job"}
          description = {
            <>
              This project is meant to develop a fully responsive and a complex website.
              Its main purpose is to develop another search engine that uses cutting-edge
              AI to deliver the best search results. Its minimum threshold is to be as
              efficient as Microsoft Bing, if not better. A underperformed solution will
              be rejected and the solution may not be cloned from elsewhere such 
              as Google.
              <br /><br />
              Add more description...
            </>
          }
        />
      </div>
      <Footer />
    </>
  )
}

export default Projects
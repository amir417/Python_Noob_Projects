import React from 'react';
import './home.css';
import { Footer } from '../../components';
import { logo } from './imports.js';

const HomeTitle = (props) => {
  return(
    <div className="home__title">
      <h1>
        {props.children}
      </h1>
    </div>
  );
}

const HomeDescription = (props) => {
  return (
    <div className="home__description">
      <p>
        {props.children}
      </p>
    </div>
  );
}

const HomeDescriptionTeam = (props) => {
  return(
    <div className="home__description-team">
      {props.children}
    </div>
  );
}

const Home = () => {
  return (
    <>
      <div className="home section__padding">
        <HomeTitle>
          CODELABORATION
        </HomeTitle>

        <HomeDescription>
            Codelaboration is a society dedicated to supporting developers
            with a huge interest in starting a project yet experiencing
            idea or member limitations. [write
            a paragraph explaining what is the purpose of this website]
        </HomeDescription>

        <HomeDescriptionTeam>
          <h1>
            To know more about Codelaboration, this is the team that designed, developed, 
            and maintained this website:
          </h1>

          <p>
            Sean Kim <br />
            <img src={logo} alt=""/> <br />
            Founder and Frontend Lead 
          </p>   

          <p>
            Charles Hsieh <br />
            <img src={logo} alt=""/> <br />
            Frontend Developer
          </p> 

          <p>
            Amirreza Aazam<br />
            <img src={logo} alt=""/> <br />
            Frontend Developer
          </p>     

          <p>
            Leo Li <br />
            <img src={logo} alt=""/> <br />
            Frontend Developer
          </p>  

          <p>
            Aiden Chow <br />
            <img src={logo} alt=""/> <br />
            Frontend Developer
          </p>      

          <p>
            Shannon Jones<br />
            <img src={logo} alt=""/> <br />
            Design Lead
          </p>      
        </HomeDescriptionTeam>
      </div>

      <Footer />
    </>
  )
}

export default Home
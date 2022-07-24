import React from 'react';
import './apply.css';
import { Footer } from '../../components';

const ApplyHeader = (props) => {
  return(
    <div className="apply__header">
      <h1>
        {props.children}
      </h1>
    </div>
  );
}

const ApplyDescription = (props) => {
  return(
    <div className="apply__description">
      <p>
        {props.children}
      </p>
    </div>
  );
}

const Apply = () => {
  return (
    <>
      <div className="apply section__padding">
        <ApplyHeader>
          Apply Section
        </ApplyHeader>
        <ApplyDescription>
          The following Google Form (SOMEONE PLEASE ADD THIS FEATURE)
          is used for one of the two situations. <br /><br />
          The first situation occurs if you happen to have a programming project in mind
          but you happen to have insufficient/inadequate members to turn your project into reality. 
          If that is the case, you can submit a posting to add your project to the "Projects"
          page where it increases your opportunity for you to be pair up with another 
          programming developer.
          <br /><br />
          The second situation occurs if you are a developer and you have found a project of
          interest. If you do not know the founder of the project itself, Codelaboration Executive
          will contact the founder for you and you can get started on the project.
        </ApplyDescription>
        {/* 
          Add the Google Forms here! Create your own className and the format should be
          fine.
        */}
      </div>
      <Footer />
    </>
  )
}

export default Apply
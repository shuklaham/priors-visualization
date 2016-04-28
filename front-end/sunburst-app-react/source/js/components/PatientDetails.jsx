var React = require('react');

var PatientDetails = React.createClass({

  render: function () {
      return (
        <div>
          <div className="col-md-4">
              <div className="centerBlock">
                <h3><span className="label label-info">Patient name</span></h3>
                <h5 className="centerBlock">Xyz</h5>
              </div>
          </div>
          <div className="col-md-4">
              <div className="centerBlock">
                <h3><span className="label label-info">Clinical statement</span></h3>
                <h5 className="centerBlock">Gastric metastatic cancer</h5>
              </div>
          </div>
          <div className="col-md-4">
              <div className="centerBlock">
                <h3><span className="label label-info">MRN number</span></h3>
                <h5 className="centerBlock">H1234</h5>
              </div>
          </div>
        </div>
      );
    }
});

module.exports = PatientDetails;


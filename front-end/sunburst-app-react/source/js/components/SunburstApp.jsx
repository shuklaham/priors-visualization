var React = require('react');
var Navbar = require('./Navbar.jsx');
var PatientDetails = require('./PatientDetails.jsx');
var Chart = require('./Chart.jsx');

var SunburstApp = React.createClass({
  
  getInitialState: function () {
    return {
      list: {}
    };
  },

  updateList: function (newList) {
    this.setState({
      list: newList
    });
  },

  addListItem: function (item) {
    var list = this.state.list;

    list[item.id] = item;

    this.updateList(list);
  },

  removeListItem: function (itemId) {
    var list = this.state.list;

    delete list[itemId];

    this.updateList(list);
  },

  removeAllListItems: function () {
    this.updateList({});
  },

  render: function () {
    var items = this.state.list;

    return (
      <div className="container">
        <div className="navRow">
          <Navbar />
        </div>
        <div className="patientRow">
          <PatientDetails />            
        </div>
        <div className="chartRow">
          <div id="centergraph">
            <Chart />
          </div>     
        </div>
      </div>
    );
  }
});

module.exports = SunburstApp;
var React = require('react');

var Chart = React.createClass({
    getInitialState: function() {
      return {
      	datesreps: [],
      	legendArray: [],
      	colorArray:{},
        findings:[],
      	rect: {}, 
        data: [],
        absentdata: [],
        svg: "",
        ranges:{},
        axes: {},
        display: { width: 800, height: 800, margin: {top: 100, right: 30, bottom: 30, left: 150 }}
      };
    },
    componentDidMount: function() {
    	var datesreps = ["June-02-2015","Aug-02-2015","Oct-02-2015"]

      datesreps.splice(0, 0, " ");
      datesreps.push("   ");

		  var colorArray = {"neg":"#313E4D","pos":"#F7D24A"};

  	  var rectw = 96
		  var recth = 22

		  var legendArray = ["Absence", "Presence","No mention"]
      var findings = ["    ",
                  "Hepatic Lesions",
                  "Lymphadenopathy",
                  "Adrenal Nodules",
                  "Retroperitoneal Edema",
                  "Small Volume Ascites",
                  "Soft Tissue Thickening",
                  "Vertebral Body",
                  "Metastasis",
                  "Hepatic Metastases",
                  "Adrenal Metastasis",
                  "     "]
	
      var state = this.state,
          margin = state.display.margin,  
          width = state.display.width ,
          height = state.display.height ;

           // draw the x axis
      // define the x and y scale
      var xRange = d3.scale.ordinal()
          .domain(datesreps)
          .rangePoints([0, (width/2)-20]);

      var yRange = d3.scale.ordinal()
          .domain(findings)
          .rangePoints([0, height-550 ]);

      // define the x axis
      var xAxis = d3.svg.axis()
          .scale(xRange)
          .orient("top");

      // define the y axis
      var yAxis = d3.svg.axis()
          .scale(yRange)
          .orient("right");

      var that = this;
       var absentdata = [{
    "x": "Oct-02-2015",
    "y": "Hepatic Lesions",
    "z":0,
    "s":""
  }, {
    "x": "Oct-02-2015",
    "y": "Lymphadenopathy",
    "z":0,
    "s":""
  },{
    "x": "Oct-02-2015",
    "y": "Hepatic Metastases",
    "z":0,
    "s":""
  },{
    "x": "Oct-02-2015",
    "y": "Adrenal Metastasis",
    "z":0,
    "s":""
  },{
    "x": "Aug-02-2015",
    "y": "Adrenal Nodules",
    "z":0,
    "s":""
  },{
    "x": "Aug-02-2015",
    "y": "Retroperitoneal Edema",
    "z":0,
    "s":""
  }, {
    "x": "Aug-02-2015",
    "y": "Small Volume Ascites",
    "z":0,
    "s":"New small-volume ascites"
  }, {
    "x": "Aug-02-2015",
    "y": "Soft Tissue Thickening",
    "z":0,
    "s": ""
  }, {
    "x": "Aug-02-2015",
    "y": "Vertebral Body",
    "z":0,
    "s":""
  }, {
    "x": "Aug-02-2015",
    "y": "Metastasis",
    "z":0,
    "s":""
  },
  {
    "x": "June-02-2015",
    "y": "Adrenal Nodules",
    "z":0,
    "s":""
  }, {
    "x": "June-02-2015",
    "y": "Retroperitoneal Edema",
    "z":0,
    "s":""
  }, {
    "x": "June-02-2015",
    "y": "Small Volume Ascites",
    "z":0,
    "s":"New small-volume ascites"
  }, {
    "x": "June-02-2015",
    "y": "Soft Tissue Thickening",
    "z":0,
    "s": ""
  }, {
    "x": "June-02-2015",
    "y": "Vertebral Body",
    "z":0,
    "s":""
  }, {
    "x": "June-02-2015",
    "y": "Metastasis",
    "z":0,
    "s":""
  }];

    
      var data = [{
    "x": "Oct-02-2015",
    "y": "Adrenal Nodules",
    "z":"pos",
    "s":"Progression of disease with increase in lymphadenopathy and bilateral adrenal nodules"
  }, {
    "x": "Oct-02-2015",
    "y": "Retroperitoneal Edema",
    "z":"pos",
    "s":"Increased mesenteric/retroperitoneal edema"
  }, {
    "x": "Oct-02-2015",
    "y": "Small Volume Ascites",
    "z":"pos",
    "s":"New small-volume ascites"
  }, {
    "x": "Oct-02-2015",
    "y": "Soft Tissue Thickening",
    "z":"pos",
    "s": "Soft tissue thickening along the undersurface of the left diaphragm is stable from the recent exam but increased from older studies and suspicious for peritoneal tumor"
  }, {
    "x": "Oct-02-2015",
    "y": "Vertebral Body",
    "z":"pos",
    "s":"Increase in subtle sclerosis in the superior half of the L2 vertebral body suspicious for metastasis"
  }, {
    "x": "Oct-02-2015",
    "y": "Metastasis",
    "z":"pos",
    "s":"Increase in subtle sclerosis in the superior half of the L2 vertebral body suspicious for metastasis"
  },{
    "x": "Aug-02-2015",
    "y": "Hepatic Lesions",
    "z":"neg",
    "s":"No new hepatic lesions identified"
  }, {
    "x": "Aug-02-2015",
    "y": "Lymphadenopathy",
    "z":"pos",
    "s":"Stable mild abdominopelvic lymphadenopathy"
  }, {
    "x": "Aug-02-2015",
    "y": "Hepatic Metastases",
    "z":"pos",
    "s":"Hepatic metastasis stable"
  }, {
    "x": "Aug-02-2015",
    "y": "Adrenal Metastasis",
    "z":"pos",
    "s":"Stable right adrenal metastatic lesion"
  },{
    "x": "June-02-2015",
    "y": "Hepatic Lesions",
    "z":"neg",
    "s":"No new suspicious hepatic lesions"
  },{
    "x": "June-02-2015",
    "y": "Lymphadenopathy",
    "z":"pos",
    "s":"Mild abdominopelvic lymphadenopathy, with nodes stable or slightly decreased in size"
  },{
    "x": "June-02-2015",
    "y": "Hepatic Metastases",
    "z":"pos",
    "s":"Stable hepatic metastasis"
  },{
    "x": "June-02-2015",
    "y": "Adrenal Metastasis",
    "z":"pos",
    "s":"Mild interval decrease in size of bilateral adrenal metastases"
  }
    ];

        that.setState({
          data: data,
          absentdata:absentdata,
          datesreps: datesreps,
          legendArray: legendArray,
          colorArray: colorArray,
          findings: findings,
          rect: {rectw:rectw, recth:recth}, 
          svg: d3.select("#graph").append("svg")
                 .attr("height", height)
                 .attr("width", width)
                 .attr("class", "svgMain"),
          ranges:{xRange:xRange, yRange:yRange },
          axes: { xAxis: xAxis, yAxis: yAxis }
        });
    },

    render: function() {
      var state = this.state,
          data = state.data,
          absentdata = state.absentdata,
          datesreps = state.datesreps,
          legendArray = state.legendArray,
          colorArray = state.colorArray,
          findings = state.findings,
          rect = state.rect,
          svg = state.svg || false,
          width = state.display.width,
          height = state.display.height,
          xRange = state.ranges.xRange,
          yRange = state.ranges.yRange,
          xAxis = state.axes.xAxis,
          yAxis = state.axes.yAxis,
          margin = state.display.margin

      if (svg) {
          var priorsChart = svg.append("g")
            .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

          priorsChart.selectAll("rect")
             .data(data)
             .enter()
             .append("rect")
             .attr("class", "repdata")
             .attr("x", function(d, i) {
                  return xRange(d.x);
             })
             .attr("y", function(d, i) {
                  return yRange(d.y);
             })
             .attr("width", rect.rectw)
             .attr("height", rect.recth)
             .attr("transform", "translate(" + rect.rectw*(-1)/2 + "," + rect.recth*(-1)/2 + ")")
             .attr("fill", function(d) {
                  return colorArray[d.z]})
             .on("click", function(d) { 
                  alertify
                    .defaultValue("Fill in your feedback")
                    .prompt("Is there anything wrong?",
                      function (val, ev) {
                        // The click event is in the event variable, so you can use it here.
                        ev.preventDefault();
                        // The value entered is availble in the val variable.
                        alertify.success("We have received your feedback. Charts would be updated accordingly");
                      }, function(ev) {
                        // The click event is in the event variable, so you can use it here.
                        ev.preventDefault();
                        alertify.error("Seems its okay");
                      });
              })
             .on("mouseover", function(d) {
                    d3.select(this)
                    .style('opacity',0.5)
                    //Get this bar's x/y values, then augment for the tooltip
                    // Increasing moves to right and bottom
                    var xPosition = parseFloat(d3.select(this).attr("x")) + 150;
                    var yPosition = parseFloat(d3.select(this).attr("y")) + 180;
                    //Update the tooltip position and value
                    d3.select("#tooltip")
                      .style("left", xPosition + "px")
                      .style("top", yPosition + "px")
                      .select("#value")
                      .text(d.s);
                    //Show the tooltip
                    d3.select("#tooltip").classed("hidden", false);
              })
           .on("mouseout", function() {
                  d3.select(this)
                    .style('opacity',1.0)
            //Hide the tooltip
                  d3.select("#tooltip").classed("hidden", true);
           }); 
          
              // draw the x axis 
          priorsChart.append("g")
              .attr("class", "fontxaxis")
              .call(xAxis)
              //.attr("transform", "translate(0,"+75+")")
              .selectAll(".tick text")
              .style("font-size","13px")
              .attr("transform", "translate(0,"+-20+")");

          // draw the y axis
          priorsChart.append("g")
              .attr("class", "fontyaxis")
              .attr("transform", "translate(" + 340 + ","+0+")")
              .call(yAxis)
              .selectAll(".tick text")
              .style("font-size","13px");

          priorsChart.append("text")
            .attr("text-anchor", "middle")  // this makes it easy to centre the text as the transform is applied to the anchor
            .attr("transform", "translate("+ 520 +","+130+")rotate(90)")  // text is drawn off the screen top left, move down and out and rotate
            .text("FINDINGS")
            .attr("font-family", "Helvetica Neue")
            .attr("font-size", "16px")
            .attr("font-weight","bold")
            .attr("fill", "black");

          priorsChart.selectAll("rect.legend")
             .data(["neg","pos"])
             .enter()
             .append("rect")
             .attr("class", "legend") 
             .attr("x", function(d, i) {
                  return 45 + i*90
             })
             .attr("y", function(d, i) {
                  return 275
             })
             .attr("width", rect.rectw)
             .attr("height", rect.recth)
             .attr("fill", function(d,i) {
                  return colorArray[d]});

          priorsChart.selectAll("rect.nomention")
             .data([0])
             .enter()
             .append("rect")
             .attr("class", "nomention") 
             .attr("x", function(d, i) {
                  return 225
             })
             .attr("y", function(d, i) {
                  return 275
             })
             .attr("width", rect.rectw)
             .attr("height", rect.recth)
             .attr("fill", function(d,i) {
                  return "none"})
             .style("fill","white")
             .style("stroke","gray")
             .style("stroke-dasharray", ("3, 3"))
             .style("stroke-opacity", 2.0);


          priorsChart.selectAll("text.legendText")
             .data(legendArray)
             .enter()
             .append("text")
             .attr("class","legendText")
             .text(function(d){
                  return d;
             })
             .attr("text-anchor", "left")
             .attr("x", function(d, i){
                  return 55 + i*90})
             .attr("y", function(d, i) {
                  return 310;
              })
             .attr("font-family", "Helvetica Neue")
             .attr("font-size", "15px")
             //.attr("font-weight","bold")
             .attr("fill", "black");

           oldiesdata = [{"t":"10-months-old","x":datesreps[1],"y":findings[0]},{"t":"8-months-old","x":datesreps[2],"y":findings[0]},{"t":"6-months-old","x":datesreps[3],"y":findings[0]}];

          priorsChart.selectAll("oldies")
             .data(oldiesdata)
             .enter()
             .append("text")
             .text(function(d){
                    return (d.t);
               })
             .attr("x", function(d, i) {
                  return xRange(d.x);
             })
             .attr("y", function(d, i) {
                  return yRange(d.y)-10;})
             .attr("font-size", "13.5px")
             .attr("fill", "black")
             .attr("text-anchor", "middle");

          priorsChart.selectAll("rect.absentdata")
                 .data(absentdata)
                 .enter()
                 .append("rect")
                 .attr("class", "absentdata")
                 .attr("x", function(d, i) {
                      return xRange(d.x);
                 })
                 .attr("y", function(d, i) {
                      return yRange(d.y);
                 })
                 .attr("width", rect.rectw)
                 .attr("height", rect.recth)
                 .attr("transform", "translate(" + rect.rectw*(-1)/2 + "," + rect.recth*(-1)/2 + ")")
                 .style("fill","none")
                 .style("stroke","gray")
                 .style("stroke-dasharray", ("3, 3"))
                 .style("stroke-opacity", .5);

      }
              
      return (
        <div id="graph"></div>
      );
    }
  });

module.exports = Chart;
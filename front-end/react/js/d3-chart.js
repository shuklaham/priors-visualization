var datesreps = ["June-02-2015","Aug-02-2015","Oct-02-2015"]
var newdates = [];
var colorArray = {};
colorArray[-1] = "#313E4D"
colorArray[1] = "#F7D24A"
 var rectw = 100
 var recth = 25
var legendArray = ["Absence", "Presence","No mention"]

for (var d in datesreps){
  var months;
  d1 = new Date(datesreps[d]);
  d2 = new Date();
  months = (d2.getFullYear() - d1.getFullYear()) * 12;
  months -= d1.getMonth() ;
  months += d2.getMonth();
  months = months <= 0 ? 0 : months;
  if(months < 1){
              newdates.push(datesreps[d] + ' ' + " <-one-month");
          }
          else{
              newdates.push(datesreps[d] + ' ' + months + "-months-old");
          }
  }

datesreps.splice(0, 0, " ");

datesreps.push("   ");

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

//margins and width
var margin = {top: 100  , right:0, bottom: 100, left: 100},
    width = 800,// - margin.left - margin.right,
    height = 800, //- margin.top - margin.bottom;
    historywidth = 600,
    historyheight = 100
// create an svg container for text history of patient
/*var svgtext = d3.select("body").append("svg")
    //.attr("width", (width + margin.left + margin.right))
    //.attr("height", (height + margin.top + margin.bottom))
    .attr("width", (historywidth))
    .attr("height", (historyheight))
  .append("g")
    .attr("transform", "translate(" + margin.left + "," + 10 + ")");
svgtext.append("rect")
    .attr("width", "100%")
    .attr("height", "100%")
    .attr("fill", "teal");
*/
// create an svg container for chart
var svgchart = d3.select("body").append("svg")
    //.attr("width", (width + margin.left + margin.right))
    //.attr("height", (height + margin.top + margin.bottom))
    .attr("width", (width))
    .attr("height", (height))
    .attr("class","svgMain")
  .append("g")
    .attr("transform", "translate(" + margin.left + "," + margin.top + ")");
//placing a rectangle around text
/*svgchart.append("rect")
  .attr("class", "patienthistory")
  .attr("width", 480)
  .attr("height", 30)
  .style("stroke", "black")    // set the line colour
  .style("fill", "1279C0")
  .style("stroke-width","0.5")
  .attr("transform", "translate(" + 1+ "," + -99 + ")");*/
//patient history text
history = ['CLINICAL STATEMENT: Metastatic gastric cancer', 
            'TECHNIQUE: CT of the chest, abdomen and pelvis with intravenous contrast'
          ]
//Insert logo
d3.select("svg")
  .append("image")
  .attr("xlink:href", "./images/hippo.png")
  .attr("x", "220px")
  .attr("y", "-35px")
  .attr("width", "200px")
  .attr("height", "200px");
//Insert Attribution
d3.select("svg")
  .append("text")
  .text("Logo designed using Logo Generator created by Elijah Zapien")
  .attr("x", function(d,i){return width/4;})
  .attr("y", function(d,i){return height-20;})
  .attr("fill", "black")
  .attr("font-size", "12px");
  
//Title sunburst
svgchart.append("text")
      .attr("class", "title")
      .attr("x", 10)
      .attr("y", 45)
      .text("PATIENT NAME: ABC")
      .attr("font-family", "Helvetica Neue")
      .attr("font-size", "16px")
      .attr("font-weight","bold")
      .attr("fill", "black");
svgchart.append("text")
      .attr("class", "title")
      .attr("x", 10)
      .attr("y", 70)
      .text("CLINICAL STATEMENT: Metastatic gastric cancer")
      .attr("font-family", "Helvetica Neue")
      .attr("font-size", "16px")
      .attr("font-weight","bold")
      .attr("fill", "black");
svgchart.append("text")
      .attr("class", "title")
      .attr("x", 10)
      .attr("y", 95)
      .text("TECHNIQUE: CT of the chest, abdomen and pelvis with intravenous contrast")
      .attr("font-family", "Helvetica Neue")
      .attr("font-size", "16px")
      .attr("font-weight","bold")
      .attr("fill", "black");
svgchart.append("text")
      .attr("text-anchor", "middle")  // this makes it easy to centre the text as the transform is applied to the anchor
      .attr("transform", "translate("+ 540 +","+280+")rotate(90)")  // text is drawn off the screen top left, move down and out and rotate
      .text("FINDINGS")
      .attr("font-family", "Helvetica Neue")
      .attr("font-size", "16px")
      .attr("font-weight","bold")
      .attr("fill", "black");

//legend      
var svg = d3.select("body").select("svg");

svg.selectAll("rect.legend")
               .data([-1,1])
               .enter()
               .append("rect")
               .attr("class", "legend") 
               .attr("x", function(d, i) {
                    return 145 + i*99
               })
               .attr("y", function(d, i) {
                    return 590
               })
               .attr("width", rectw)
               .attr("height", recth)
               .attr("fill", function(d,i) {
                    return colorArray[d]});

svg.selectAll("rect.nomention")
               .data([0])
               .enter()
               .append("rect")
               .attr("class", "nomention") 
               .attr("x", function(d, i) {
                    return 145 + 198
               })
               .attr("y", function(d, i) {
                    return 590
               })
               .attr("width", rectw)
               .attr("height", recth)
               .attr("fill", function(d,i) {
                    return "none"})
               .style("fill","white")
               .style("stroke","gray")
               .style("stroke-dasharray", ("3, 3"))
               .style("stroke-opacity", 2.0);

svg.selectAll("text.legendText")
               .data(legendArray)
               .enter()
               .append("text")
               .attr("class","legendText")
               .text(function(d){
                    return d;
               })
               .attr("text-anchor", "left")
               .attr("x", function(d, i){
                    return 155 + i*99})
               .attr("y", function(d, i) {
                    return 585;
                })
               .attr("font-family", "Helvetica Neue")
               .attr("font-size", "16px")
               .attr("font-weight","bold")
               .attr("fill", "black");
            svg.append("text")
               .attr("class","legendName")
               .text(function(d){
                    return 'Legend';
               })
               .attr("text-anchor", "left")
               .attr("x", 70)
               .attr("y", 610)
               .attr("font-family", "Helvetica Neue")
               .attr("font-size", "18px")
               .attr("font-weight","bold")
               .attr("fill", "black");

// draw the x axis
// define the x and y scale
var xRange = d3.scale.ordinal()
    .domain(datesreps)
    .rangePoints([0, width/2]);

var yRange = d3.scale.ordinal()
    .domain(findings)
    .rangePoints([0, height-510 ]);
// define the x axis
var xAxis = d3.svg.axis()
    .scale(xRange)
    .orient("top");
// define the y axis
var yAxis = d3.svg.axis()
    .scale(yRange)
    .orient("left");

// draw the x axis 
svgchart.append("g")
    .attr("class", "fontxaxis")
    .call(xAxis)
    .attr("transform", "translate(0,"+150+")")
    .selectAll(".tick text")
    .style("font-size","13px")
    .attr("transform", "translate(0,"+-20+")");

function wrap(text, width) {
  text.each(function() {
    var text = d3.select(this),
        words = text.text().split(/\s+/).reverse(),
        word,
        line = [],
        lineNumber = 0,
        lineHeight = 1.1, // ems
        y = text.attr("y"),
        dy = parseFloat(text.attr("dy")),
        tspan = text.text(null).append("tspan").attr("x", 0).attr("y", y).attr("dy", dy + "em");

    while (word = words.pop()) {
      line.push(word);
      tspan.text(line.join(" "));

      if (tspan.node().getComputedTextLength() > width) {
        line.pop();
        tspan.text(line.join(" "));
        line = [word];
        tspan = text.append("tspan").attr("x", 0).attr("y", y).attr("dy", ++lineNumber * lineHeight + dy + "em").text(word);
      }
    }
  });
}

// draw the y axis
svgchart.append("g")
    .attr("class", "fontyaxis")
    .attr("transform", "translate(" + 370 + ","+150+")")
    .call(yAxis)
    .selectAll(".tick text")
    .style("font-size","13px");

var repdata = [{
  "x": "Oct-02-2015",
  "y": "Adrenal Nodules",
  "z":1,
  "s":"Progression of disease with increase in lymphadenopathy and bilateral adrenal nodules"
}, {
  "x": "Oct-02-2015",
  "y": "Retroperitoneal Edema",
  "z":1,
  "s":"Increased mesenteric/retroperitoneal edema"
}, {
  "x": "Oct-02-2015",
  "y": "Small Volume Ascites",
  "z":1,
  "s":"New small-volume ascites"
}, {
  "x": "Oct-02-2015",
  "y": "Soft Tissue Thickening",
  "z":1,
  "s": "Soft tissue thickening along the undersurface of the left diaphragm is stable from the recent exam but increased from older studies and suspicious for peritoneal tumor"
}, {
  "x": "Oct-02-2015",
  "y": "Vertebral Body",
  "z":1,
  "s":"Increase in subtle sclerosis in the superior half of the L2 vertebral body suspicious for metastasis"
}, {
  "x": "Oct-02-2015",
  "y": "Metastasis",
  "z":1,
  "s":"Increase in subtle sclerosis in the superior half of the L2 vertebral body suspicious for metastasis"
},{
  "x": "Aug-02-2015",
  "y": "Hepatic Lesions",
  "z":-1,
  "s":"No new hepatic lesions identified"
}, {
  "x": "Aug-02-2015",
  "y": "Lymphadenopathy",
  "z":1,
  "s":"Stable mild abdominopelvic lymphadenopathy"
}, {
  "x": "Aug-02-2015",
  "y": "Hepatic Metastases",
  "z":1,
  "s":"Hepatic metastasis stable"
}, {
  "x": "Aug-02-2015",
  "y": "Adrenal Metastasis",
  "z":1,
  "s":"Stable right adrenal metastatic lesion"
},{
  "x": "June-02-2015",
  "y": "Hepatic Lesions",
  "z":-1,
  "s":"No new suspicious hepatic lesions"
},{
  "x": "June-02-2015",
  "y": "Lymphadenopathy",
  "z":1,
  "s":"Mild abdominopelvic lymphadenopathy, with nodes stable or slightly decreased in size"
},{
  "x": "June-02-2015",
  "y": "Hepatic Metastases",
  "z":1,
  "s":"Stable hepatic metastasis"
},{
  "x": "June-02-2015",
  "y": "Adrenal Metastasis",
  "z":1,
  "s":"Mild interval decrease in size of bilateral adrenal metastases"
}
  ];

svgchart.selectAll("rect")
       .data(repdata)
       .enter()
       .append("rect")
       .attr("class", "repdata")
       .attr("x", function(d, i) {
            return xRange(d.x);
       })
       .attr("y", function(d, i) {
            return yRange(d.y);
       })
       .attr("width", rectw)
       .attr("height", recth)
       .attr("transform", "translate(" + rectw*(-1)/2 + "," + 135 + ")")
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
            var xPosition = parseFloat(d3.select(this).attr("x")) + 100;
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
  "x": "Aug-02-2015",
  "y": "Adrenal Nodules",
  "z":0,
  "s":""
}, {
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
}
  ];

  svgchart.selectAll("rect.absentdata")
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
               .attr("width", rectw)
               .attr("height", recth)
               .attr("transform", "translate(" + rectw*(-1)/2 + "," + 135 + ")")
               .style("fill","none")
               .style("stroke","gray")
               .style("stroke-dasharray", ("3, 3"))
               .style("stroke-opacity", .5);
              
  oldiesdata = [{"t":"10-months-old","x":datesreps[0],"y":findings[0]},{"t":"8-months-old","x":datesreps[1],"y":findings[0]},{"t":"6-months-old","x":datesreps[2],"y":findings[0]}];
  
  svgchart.selectAll("oldies")
             .data(oldiesdata)
             .enter()
             .append("text")
             .text(function(d){
                    return (d.t);
               })
             .attr("x", function(d, i) {
                  return xRange(d.x)+100;
             })
             .attr("y", function(d, i) {
                  return yRange(d.y)+138;})
             .attr("font-size", "13.5px")
             .attr("fill", "black")
             .attr("text-anchor", "middle");

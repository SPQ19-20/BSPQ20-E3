
var margin = {top: 50, right: 30, bottom: 30, left: 60},
    width = 1150 - margin.left - margin.right,
    height = 400 - margin.top - margin.bottom;

// svg stands for Scalable Vector Graphics, the svg is going to be what we draw 
var svg = d3.select("svg")
.attr("width", width + margin.left + margin.right)
.attr("height", height + margin.top + margin.bottom)

// Here we set the scale, center and position of the map.
var path = d3.geoPath();
var projection = d3.geoMercator()
  .scale(125)
  .center([0,40])
  .translate([width / 2-50, height / 2]);

// Data and color scale
var data = d3.map();
var colorScale = d3.scaleThreshold()
  .domain([0,5, 10, 100, 1000, 10000, 30000, 100000,200000])
  .range(d3.schemeReds[9]);

// Loading of the data form the repositories
d3.queue()
  .defer(d3.json, "https://raw.githubusercontent.com/holtzy/D3-graph-gallery/master/DATA/world.geojson")
  .defer(d3.csv, "https://raw.githubusercontent.com/datasets/covid-19/master/data/countries-aggregated.csv",  function(d){
     data.set(d.Country, +d.Confirmed); })
  .await(ready);

 
  //This variables are for the tooltip (when you pass through a country will show the name and confirmed cases.)
  var offsetL = document.getElementById('map').offsetLeft+10;
  var offsetT = document.getElementById('map').offsetTop+10;
  var tooltip = d3.select("#map")
       .append("div")
       .attr("class", "tooltip hidden");



function ready(error, topo) {

  // when the mouse is over a country the rest will fade alittle bit
  let mouseOver = function(d) {
    d3.selectAll(".Country")
      .transition()
      .duration(200)
      .style("opacity", .5)
    d3.select(this)
      .transition()
      .duration(200)
      .style("opacity", 1)
      .style("stroke", "transparent")
  
  }
// when the mouse leaves a country all of them will be in the same level of opacity
  let mouseLeave = function(d) {
    d3.selectAll(".Country")
      .transition()
      .duration(200)
      .style("opacity", .8)
    d3.select(this)
      .transition()
      .duration(200)
      .style("stroke", "transparent")
  }

  // Draw the map
  svg.append("g")
    .selectAll("path")
    .data(topo.features)
    .enter()
    .append("path")
      // draw each country
      .attr("d", d3.geoPath()
        .projection(projection)
      )
      // set the color of each country
      .attr("fill", function (d) {
       
        if(d.properties.name == "England"){
          d.total = "United Kingdom"
        }else if(d.properties.name == "USA"){
          d.total = data.get("US") || 0;
        }else if(d.properties.name == "Democratic Republic of the Congo"){
          d.total = data.get("Congo (Kinshasa)") || 0;
        }else if(d.properties.name == "Republic of the Congo"){
          d.total = data.get("Congo (Brazzaville)") || 0;
        }else if(d.properties.name == "United Republic of Tanzania"){
          d.total = data.get("Tanzania") || 0;
        }else if(d.properties.name == "Greenland"){
          d.total = 11 || 0;
        }else {
          d.total = data.get(d.properties.name) || 0;
        }
        
        
        return colorScale(d.total)
      })
      .style("stroke", "transparent")
      .attr("class", function(d){ return "Country" } )
      .style("opacity", .8)
      // Add the functions
      .on("mouseover", mouseOver )  
      .on("mouseleave", mouseLeave )
      // add the tooltip
      .on("mousemove",   function (d) {
        if(d.properties.name == "England"){
          d.total = "United Kingdom"
        }else if(d.properties.name == "USA"){
          d.total = data.get("US") || 0;
        }else if(d.properties.name == "Democratic Republic of the Congo"){
          d.total = data.get("Congo (Kinshasa)") || 0;
        }else if(d.properties.name == "Republic of the Congo"){
          d.total = data.get("Congo (Brazzaville)") || 0;
        }else if(d.properties.name == "United Republic of Tanzania"){
          d.total = data.get("Tanzania") || 0;
        }else if(d.properties.name == "Greenland"){
          d.total = 11 || 0;
        }else {
          d.total = data.get(d.properties.name) || 0;
        }
        label = d.properties.name+ ": "+d.total+ " confirmed cases";
        var mouse = d3.mouse(svg.node())
          .map( function(d) { return parseInt(d); } );
        tooltip.classed("hidden", false)
          .attr("style", "left:"+(mouse[0]+offsetL)+"px;top:"+(mouse[1]+offsetT)+"px")
          .html(label);}
      // hide the tooltip
      ).on("mouseout", function(d) {   
        tooltip.transition()    
        .duration(0)    
        .style("opacity", 0); 
      });
    }

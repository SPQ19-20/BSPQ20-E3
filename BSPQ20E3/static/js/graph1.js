


// set the dimensions and margins of the graph
var margin = {top: 50, right: 30, bottom: 30, left: 60},
    width = 460 - margin.left - margin.right,
    height = 400 - margin.top - margin.bottom;

// append the svg object to the body of the page
var svg2 = d3.select("#my_data")
  .append("svg")
    .attr("width", width + margin.left + margin.right)
    .attr("height", height + margin.top + margin.bottom)
  .append("g")
    .attr("transform",
          "translate(" + margin.left + "," + margin.top + ")");

//Read the data
d3.csv("https://raw.githubusercontent.com/datasets/covid-19/master/data/countries-aggregated.csv", function(data) {

  data = data.filter(function(row) {
    return (row['Country'] == 'Spain' || row['Country'] == 'Italy'|| row['Country'] == 'China'|| row['Country'] == 'US'
    || row['Country'] == 'France'|| row['Country'] == 'United Kingdom') 
   ;
})
  // group the data: I want to draw one line per group
  var sumstat = d3.nest() // nest function allows to group the calculation per level of a factor
    .key(function(d) { return d.Country;})
    .entries(data);

  // Add X axis --> it is a date format
  var x = d3.scaleLinear()
    .domain(d3.extent(data, function(d) { return Date.parse(d.Date); }))
    .range([ 0, width ]);
  svg2.append("g")
    .attr("transform", "translate(0," + height + ")")
    .call(d3.axisBottom(x).ticks(6));

    
svg2.append("text")
.attr("x", (width / 2))             
.attr("y", 0 - (margin.top / 2))
.attr("text-anchor", "middle")  
.style("font-size", "16px") 
.style("text-decoration", "underline")  
.text("CONFIRMED CASES THROUGH TIME");

  // Add Y axis
  var y = d3.scaleLinear()
    .domain([0, d3.max(data, function(d) { return +d.Confirmed; })])
    .range([ height, 0 ]);
  svg2.append("g")
    .call(d3.axisLeft(y));

  // color palette
  var res = sumstat.map(function(d){ return d.key }) // list of group names
  var color = d3.scaleOrdinal()
    .domain(res)
    .range(['#e41a1c','#377eb8','#4daf4a','#f781bf','#ff7f00','#ffff33'])

    svg2.append("rect").attr("x", -20).attr("y",315).attr("height",20).attr("width",500).style("fill", '#FFF');
    svg2.append("circle").attr("cx",10).attr("cy",30).attr("r", 6).style("fill", "#e41a1c")
    svg2.append("circle").attr("cx",10).attr("cy",60).attr("r", 6).style("fill", "#377eb8")
    svg2.append("circle").attr("cx",10).attr("cy",90).attr("r", 6).style("fill", "#4daf4a")
    svg2.append("circle").attr("cx",10).attr("cy",120).attr("r", 6).style("fill", '#f781bf')
    svg2.append("circle").attr("cx",10).attr("cy",150).attr("r", 6).style("fill", '#ff7f00')
    svg2.append("circle").attr("cx",10).attr("cy",180).attr("r", 6).style("fill", '#ffff33')
    svg2.append("text").attr("x", 30).attr("y", 30).text("China").style("font-size", "15px").attr("alignment-baseline","middle")
    svg2.append("text").attr("x", 30).attr("y", 60).text("France").style("font-size", "15px").attr("alignment-baseline","middle")
    svg2.append("text").attr("x", 30).attr("y", 90).text("Italy").style("font-size", "15px").attr("alignment-baseline","middle")
    svg2.append("text").attr("x", 30).attr("y", 120).text("Spain").style("font-size", "15px").attr("alignment-baseline","middle")
    svg2.append("text").attr("x", 30).attr("y", 150).text("US").style("font-size", "15px").attr("alignment-baseline","middle")
    svg2.append("text").attr("x", 30).attr("y", 180).text("Unite Kingdom").style("font-size", "15px").attr("alignment-baseline","middle")
    svg2.append("text").attr("x", -7).attr("y", 325).text("22/01/2020").style("font-size", "10px").attr("alignment-baseline","middle")
    svg2.append("text").attr("x", 55).attr("y", 325).text("04/02/2020").style("font-size", "10px").attr("alignment-baseline","middle")
    svg2.append("text").attr("x", 117).attr("y", 325).text("17/02/2020").style("font-size", "10px").attr("alignment-baseline","middle")
    svg2.append("text").attr("x", 180).attr("y", 325).text("31/02/2020").style("font-size", "10px").attr("alignment-baseline","middle")
    svg2.append("text").attr("x", 240).attr("y", 325).text("13/03/2020").style("font-size", "10px").attr("alignment-baseline","middle")
    svg2.append("text").attr("x", 304).attr("y", 325).text("26/03/2020").style("font-size", "10px").attr("alignment-baseline","middle")
    svg2.append("text").attr("x", 380).attr("y", 325).text("now").style("font-size", "10px").attr("alignment-baseline","middle")

  // Draw the line
  svg2.selectAll(".line")
      .data(sumstat)
      .enter()
      .append("path")
        .attr("fill", "none")
        .attr("stroke", function(d){ return color(d.key) })
        .attr("stroke-width", 1.5)
        .attr("d", function(d){
          return d3.line()
            .x(function(d) { return x(Date.parse(d.Date)); })
            .y(function(d) { return y(+d.Confirmed); })
            (d.values)
        })

})

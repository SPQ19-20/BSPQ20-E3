
var margin = {top: 50, right: 30, bottom: 90, left: 40},
width = 460 - margin.left - margin.right,
height = 450 - margin.top - margin.bottom;

//append the svg object to the body of the page
var svg4= d3.select("#my_data2")
.append("svg")
.attr("width", width + margin.left + margin.right)
.attr("height", height + margin.top + margin.bottom)
.append("g")
.attr("transform",
      "translate(" + margin.left + "," + margin.top + ")");

var tooltip2 = d3.select("#my_data2").append("div").attr("class", "tooltip ");
// Load the data from github
d3.csv("https://raw.githubusercontent.com/datasets/covid-19/master/data/countries-aggregated.csv", function(data) {

//create a variable today -2 days beacause the github does not have instantaneous results.


function calculateDate(date, days){
  date.setDate(date.getDate() - days);
  return date;
}

var today = new Date();
var yest = calculateDate(today,2);
var dd = String(yest.getDate()).padStart(2, '0');
var mm = String(yest.getMonth() + 1).padStart(2, '0'); //January is 0
var yyyy = yest.getFullYear();
today = yyyy + '-' + mm + '-' + dd;

//filter rows of the csv so we only get the most recent cases 


  data = data.filter(function(row) {
    return row['Deaths'] > 300 && row['Date'] == today ;
})

// title
svg4.append("text")
        .attr("x", (width / 2))             
        .attr("y", 0 - (margin.top / 2))
        .attr("text-anchor", "middle")  
        .style("font-size", "16px") 
        .style("text-decoration", "underline")  
//        .text("DEATH NUMBER COMPARATIVE " + today);

// X axis
var x = d3.scaleBand()
.range([ 0, width ])
.domain(data.map(function(d) { return d.Country; }))
.padding(0.2);
svg4.append("g")
.attr("transform", "translate(0," + height + ")")
.call(d3.axisBottom(x))
.selectAll("text")
.attr("transform", "translate(-10,0)rotate(-45)")
.style("text-anchor", "end");


// Y axis
var y = d3.scaleLinear()
.domain([0, d3.max(data, function(d) { return +d.Deaths; })])
.range([ height, 0]);
svg4.append("g")
.call(d3.axisLeft(y));


// tooltip



// Bars
svg4.selectAll(".bar")
.data(data)
.enter()
.append("rect")
.attr("x", function(d) { return x(d.Country); })
.attr("width", x.bandwidth())
.attr("fill", "#69b3a2")
// no bar at the beginning thus:
.attr("height", function(d) { return height - y(0); }) // always equal to 0
.attr("y", function(d) { return y(0); })
.on('mouseover', (d) => {
  tooltip2.transition().duration(100).style('opacity', 0.9);
  tooltip2.html(`<span>${d.Deaths}</span> deaths in <span>${d.Country}</span> `)
    .style('left', `${d3.event.layerX}px`)
    .style('top', `${(d3.event.layerY - 28)}px`);
})
.on('mouseout', () => tooltip2.transition().duration(100).style('opacity', 0));
// Animation
svg4.selectAll("rect")
.transition()
.duration(800)
.attr("y", function(d) { return y(d.Deaths); })
.attr("height", function(d) { return height - y(d.Deaths); })
.delay(function(d,i){console.log(i) ; return(i*100)})

})
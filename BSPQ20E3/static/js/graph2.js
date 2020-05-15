
var margin = {top: 50, right: 30, bottom: 90, left:70},
width = 700 - margin.left - margin.right,
height = 320

//append the svg object to the body of the page
var svg4= d3.select("#my_data2")
.append("svg")
.attr("width", width + margin.left + margin.right)
.attr("height", height + margin.top + margin.bottom)
.append("g")
.attr("transform",
      "translate(" + margin.left + "," + margin.top + ")");

var y = d3.scaleLinear()
  .range([ height, 0]);
var yAxis = svg4.append("g")
  .attr("class", "myYaxis")

var x = d3.scaleBand()
  .range([ 0, width ])
  .padding(0.2);
var xAxis = svg4.append("g")
  .attr("transform", "translate(0," + height + ")")

  

function update(selectedVar) {
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
    return row['Deaths'] > 500 && row['Date'] == today ;
})

x.domain(data.map(function(d) { return d.Country; }))
.padding(0.2);
svg4.append("g")
.attr("transform", "translate(0," + height + ")")
.call(d3.axisBottom(x))
.selectAll("text")
.attr("transform", "translate(-10,0)rotate(-45)")
.style("text-anchor", "end");

// Y axis
y.domain([0, d3.max(data, function(d) { return +d[selectedVar] }) ]);
yAxis.transition().duration(1000).call(d3.axisLeft(y));






// Bars
var u = svg4.selectAll("rect")
      .data(data)

    // update bars
    u
    .enter()
    .append("rect")
    .merge(u)
    .transition()
    .duration(1000)
    .attr("x", function(d) { return x(d.Country); })
    .attr("y", function(d) { return y(d[selectedVar]); })
    .attr("width", x.bandwidth())
    .attr("height", function(d) { return height - y(d[selectedVar]); })
    .attr("fill", "#69b3a2")
    

 


})
}

// Initialize plot
update('Deaths')


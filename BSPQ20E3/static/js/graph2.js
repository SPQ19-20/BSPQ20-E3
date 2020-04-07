
var margin = {top: 50, right: 30, bottom: 90, left: 40},
width = 460 - margin.left - margin.right,
height = 450 - margin.top - margin.bottom;

//append the svg object to the body of the page
var svg3= d3.select("#my_data2")
.append("svg")
.attr("width", width + margin.left + margin.right)
.attr("height", height + margin.top + margin.bottom)
.append("g")
.attr("transform",
      "translate(" + margin.left + "," + margin.top + ")");

// Load the data from github
d3.csv("https://raw.githubusercontent.com/datasets/covid-19/master/data/countries-aggregated.csv", function(data) {

//create a variable today -2 days beacause the github does not have instantaneous results.
var today = new Date();
if(today.getDate()>2){
var dd = String(today.getDate()-2).padStart(2, '0');
var mm = String(today.getMonth() + 1).padStart(2, '0'); //January is 0
var yyyy = today.getFullYear();
}else if(today.getDate()<=2 && today.getMonth()!=0){
var dd = String(30);
var mm = String(today.getMonth()).padStart(2, '0');
var yyyy = today.getFullYear();
}else{
  var dd = String(30);
  var mm = String(12);
  var yyyy = today.getFullYear()-1;
}


//filter rows of the csv so we only get the most recent cases 
today = yyyy + '-' + mm + '-' + dd;

  data = data.filter(function(row) {
    return row['Deaths'] > 300 && row['Date'] == today ;
})

// title
svg3.append("text")
        .attr("x", (width / 2))             
        .attr("y", 0 - (margin.top / 2))
        .attr("text-anchor", "middle")  
        .style("font-size", "16px") 
        .style("text-decoration", "underline")  
        .text("DEATH NUMBER COMPARATIVE ");

// X axis
var x = d3.scaleBand()
.range([ 0, width ])
.domain(data.map(function(d) { return d.Country; }))
.padding(0.2);
svg3.append("g")
.attr("transform", "translate(0," + height + ")")
.call(d3.axisBottom(x))
.selectAll("text")
.attr("transform", "translate(-10,0)rotate(-45)")
.style("text-anchor", "end");


// Y axis
var y = d3.scaleLinear()
.domain([0, 20000])
.range([ height, 0]);
svg3.append("g")
.call(d3.axisLeft(y));

// Bars
svg3.selectAll("mybar")
.data(data)
.enter()
.append("rect")
.attr("x", function(d) { return x(d.Country); })
.attr("width", x.bandwidth())
.attr("fill", "#69b3a2")
// no bar at the beginning thus:
.attr("height", function(d) { return height - y(0); }) // always equal to 0
.attr("y", function(d) { return y(0); })

// Animation
svg3.selectAll("rect")
.transition()
.duration(800)
.attr("y", function(d) { return y(d.Deaths); })
.attr("height", function(d) { return height - y(d.Deaths); })
.delay(function(d,i){console.log(i) ; return(i*100)})

})
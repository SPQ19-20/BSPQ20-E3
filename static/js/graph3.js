
// set the dimensions and margins of the graph
var margin = {top: 50, right: 30, bottom: 30, left: 60},
width = 700 - margin.left - margin.right,
    height = 400 - margin.top - margin.bottom;

// append the svg object to the body of the page
var svg3 = d3.select("#my_data3")
  .append("svg")
    .attr("width", width + margin.left + margin.right)
    .attr("height", height + margin.top + margin.bottom)
  .append("g")
    .attr("transform",
          "translate(" + margin.left + "," + margin.top + ")");

//Loading the data
d3.csv("https://raw.githubusercontent.com/datasets/covid-19/master/data/countries-aggregated.csv", function(data) {

//filter the countries we have chosen (the most infected ones)
  data = data.filter(function(row) {
    return (row['Country'] == 'Spain' || row['Country'] == 'Italy'|| row['Country'] == 'China'|| row['Country'] == 'US'
    || row['Country'] == 'France'|| row['Country'] == 'United Kingdom') 
   ;
})

  // group the data: I want to draw one line per group
  var sumstat = d3.nest() // nest function allows to group the calculation per level of a factor
    .key(function(d) { return d.Country;})
    .entries(data);

    // title
    svg3.append("text")
    .attr("x", (width / 2))             
    .attr("y", 0 - (margin.top / 2))
    .attr("text-anchor", "middle")  
    .style("font-size", "16px") 
    .style("text-decoration", "underline")  
  //  .text("CONFIRMED CASES THROUGH TIME");

  //X axis ( the date)
  var x = d3.scaleLinear()
    .domain(d3.extent(data, function(d) { return Date.parse(d.Date); }))
    .range([ 0, width ]);
  svg3.append("g")
    .attr("transform", "translate(0," + height + ")")
    .call(d3.axisBottom(x).ticks(4));


  anterior=0
  //Y axis
  var y = d3.scaleLinear()
    .domain([0,33000])
    .range([ height, 0 ]);
  svg3.append("g")
    .call(d3.axisLeft(y));

  // color palette
  var res = sumstat.map(function(d){ return d.key }) // list of group names
  var color = d3.scaleOrdinal()
    .domain(res)
    .range(['#e41a1c','#377eb8','#4daf4a','#f781bf','#ff7f00','#ffff33'])

    //legend circles, and names of the countries
    svg3.append("rect").attr("x", -30).attr("y",height+5).attr("height",20).attr("width",680).style("fill", '#FFF');
    svg3.append("circle").attr("cx",10).attr("cy",30).attr("r", 6).style("fill", "#e41a1c")
    svg3.append("circle").attr("cx",10).attr("cy",60).attr("r", 6).style("fill", "#377eb8")
    svg3.append("circle").attr("cx",10).attr("cy",90).attr("r", 6).style("fill", "#4daf4a")
    svg3.append("circle").attr("cx",10).attr("cy",120).attr("r", 6).style("fill", '#f781bf')
    svg3.append("circle").attr("cx",10).attr("cy",150).attr("r", 6).style("fill", '#ff7f00')
    svg3.append("circle").attr("cx",10).attr("cy",180).attr("r", 6).style("fill", '#ffff33')
    svg3.append("text").attr("x", 30).attr("y", 30).text("China").style("font-size", "15px").attr("alignment-baseline","middle")
    svg3.append("text").attr("x", 30).attr("y", 60).text("France").style("font-size", "15px").attr("alignment-baseline","middle")
    svg3.append("text").attr("x", 30).attr("y", 90).text("Italy").style("font-size", "15px").attr("alignment-baseline","middle")
    svg3.append("text").attr("x", 30).attr("y", 120).text("Spain").style("font-size", "15px").attr("alignment-baseline","middle")
    svg3.append("text").attr("x", 30).attr("y", 150).text("US").style("font-size", "15px").attr("alignment-baseline","middle")
    svg3.append("text").attr("x", 30).attr("y", 180).text("Unite Kingdom").style("font-size", "15px").attr("alignment-baseline","middle")


    // as i couldn't figure how to put the dates in the graph in a legible way, i created this method,
    // that calculates the time that has passed since the first data is registred till now, and writes
    // 6 dates in the bottom of the graph
    let date1 = new Date('2020/01/22');
    let date2 = new Date()
    let resta = date2.getTime() - date1.getTime()
    var days = Math.round(resta/5)
    
     function setdays(date, days){
      let suma = date.getTime()+days
      var date3 = new Date(suma);
      var dd = String(date3.getDate()).padStart(2, '0');
      var mm = String(date3.getMonth() + 1).padStart(2, '0'); //January is 0
      var yyyy = date3.getFullYear();

      var sfecha = dd + '/' + mm + '/' + yyyy;
      
      return sfecha;
    }
    
    
    svg3.append("text").attr("x", 0).attr("y", height+15).text(setdays(date1,0)).style("font-size", "10px").attr("alignment-baseline","middle")
    svg3.append("text").attr("x", 130).attr("y", height+15).text(setdays(date1,days)).style("font-size", "10px").attr("alignment-baseline","middle")
    svg3.append("text").attr("x", 260).attr("y", height+15).text(setdays(date1,2*days)).style("font-size", "10px").attr("alignment-baseline","middle")
    svg3.append("text").attr("x", 385).attr("y", height+15).text(setdays(date1,3*days)).style("font-size", "10px").attr("alignment-baseline","middle")
    svg3.append("text").attr("x", 520).attr("y", height+15).text(setdays(date1,4*days)).style("font-size", "10px").attr("alignment-baseline","middle")
    svg3.append("text").attr("x", 600).attr("y", height+15).text("now").style("font-size", "10px").attr("alignment-baseline","middle")


  // Draw the line
  svg3.selectAll(".line")
      .data(sumstat)
      .enter()
      .append("path")
        .attr("fill", "none")
        .attr("stroke", function(d){ return color(d.key) })
        .attr("stroke-width",1.5)
        .attr("d", function(d){
          anterior = 0;
            ayer = 0;
            antesdeayer=0;
            return d3.line()
              .x(function(d) { return x(Date.parse(d.Date)); })
              .y(function(d) { 
              hoy = (d.Confirmed-anterior+ayer+antesdeayer)/3
              anterior = d.Confirmed
              antesdeayer=ayer
              ayer = hoy
              return y(hoy)
             
            })
              (d.values)
             
          })

})
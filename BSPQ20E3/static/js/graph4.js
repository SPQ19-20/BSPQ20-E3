
// set the dimensions and margins of the graph
var margin = {top: 50, right: 30, bottom: 30, left: 60},
    width = 460 - margin.left - margin.right,
    height = 400 - margin.top - margin.bottom;

// append the svg object to the body of the page
var svg5 = d3.select("#my_data4")
  .append("svg")
    .attr("width", width + margin.left + margin.right)
    .attr("height", height + margin.top + margin.bottom)
  .append("g")
    .attr("transform",
          "translate(" + margin.left + "," + margin.top + ")");

    var y = d3.scaleLinear()
    .range([ height, 0]);
var yAxis2 = svg5.append("g")
    .attr("class", "myYaxis")

var x = d3.scaleBand()
    .range([ 0, width ])
    .padding(0.2);
var xAxis = svg4.append("g")
    .attr("transform", "translate(0," + height + ")")

          

//Loading the data

function update2(selectedVar2) {
    
svg5.append("rect").attr("x", -50).attr("y",-50).attr("height",500).attr("width",500).style("fill", '#FFF');

d3.csv("https://raw.githubusercontent.com/datasets/covid-19/master/data/countries-aggregated.csv", function(data) {

//filter the countries we have chosen (the most infected ones)
  data = data.filter(function(row) {
    return (row['Country'] == selectedVar2) 
   ;
})

  // group the data: I want to draw one line per group
  var sumstat = d3.nest() // nest function allows to group the calculation per level of a factor
    .key(function(d) { return d.Country;})
    .entries(data);

    // title
    svg5.append("text")
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
  svg5.append("g")
    .attr("transform", "translate(0," + height + ")")
    .call(d3.axisBottom(x).ticks(4));


    anterior = 0;
  //Y axis
  var y = d3.scaleLinear()
    .domain([0, d3.max(data, function(d){
        
          hoy = (d.Confirmed-anterior)
          anterior = d.Confirmed
          if(selectedVar2== "France"|| selectedVar2== "China"){
            return (hoy/2)
          }else{
            return (hoy)
          }
        
      }) ])
     .range([ height, 0 ]);


     yAxis2.transition().duration(1000).call(d3.axisLeft(y));


  svg5.append("g")
    .call(d3.axisLeft(y));

  // color palette
  var color = d3.scaleOrdinal()
    .range(['#e41a1c','#377eb8','#4daf4a'])

    //legend circles, and names of the countries
    svg5.append("rect").attr("x", -30).attr("y",height+5).attr("height",20).attr("width",500).style("fill", '#FFF');
    svg5.append("circle").attr("cx",10).attr("cy",90).attr("r", 6).style("fill", "#e41a1c")
    svg5.append("circle").attr("cx",10).attr("cy",30).attr("r", 6).style("fill", "#377eb8")
    svg5.append("circle").attr("cx",10).attr("cy",60).attr("r", 6).style("fill", "#4daf4a")
    svg5.append("text").attr("x", 30).attr("y", 30).text("Confirmed").style("font-size", "15px").attr("alignment-baseline","middle")
    svg5.append("text").attr("x", 30).attr("y", 60).text("Recovered").style("font-size", "15px").attr("alignment-baseline","middle")
    svg5.append("text").attr("x", 30).attr("y", 90).text("Deaths").style("font-size", "15px").attr("alignment-baseline","middle")
  


    // as i couldn't figure how to put the dates in the graph in a legible way, i created this method,
    // that calculates the time that has passed since the first data is registred till now, and writes
    // 6 dates in the bottom of the graph
    let date1 = new Date('2020/01/22');
    let date2 = new Date()
    let resta = date2.getTime() - date1.getTime()
    var days = Math.round(resta/4)
    
     function setdays(date, days){
      let suma = date.getTime()+days
      var date3 = new Date(suma);
      var dd = String(date3.getDate()).padStart(2, '0');
      var mm = String(date3.getMonth() + 1).padStart(2, '0'); //January is 0
      var yyyy = date3.getFullYear();

      var sfecha = dd + '/' + mm + '/' + yyyy;
      
      return sfecha;
    }
    
    
    svg5.append("text").attr("x", 0).attr("y", height+15).text(setdays(date1,0)).style("font-size", "10px").attr("alignment-baseline","middle")
    svg5.append("text").attr("x", 90).attr("y", height+15).text(setdays(date1,days)).style("font-size", "10px").attr("alignment-baseline","middle")
    svg5.append("text").attr("x", 190).attr("y", height+15).text(setdays(date1,2*days)).style("font-size", "10px").attr("alignment-baseline","middle")
    svg5.append("text").attr("x", 285).attr("y", height+15).text(setdays(date1,3*days)).style("font-size", "10px").attr("alignment-baseline","middle")
    svg5.append("text").attr("x", 360).attr("y", height+15).text("now").style("font-size", "10px").attr("alignment-baseline","middle")


  // Draw the line


  svg5.selectAll(".line")
      .data(sumstat)
      .enter()
      .append("path")
        .attr("fill", "none")
        .attr("stroke", function(d){ return color("#4daf4a") })
        .attr("stroke-width",1.5)
        .attr("d", function(d){
          anterior = 0;
          return d3.line()
            .x(function(d) { return x(Date.parse(d.Date)); })
            .y(function(d) { 
            hoy = d.Deaths-anterior
            anterior = d.Deaths
           
            return y(hoy)
           
          })
            (d.values)
           
        })

        svg5.selectAll(".line")
        .data(sumstat)
        .enter()
        .append("path")
          .attr("fill", "none")
          .attr("stroke", function(d){ return color("#e41a1c") })
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

          svg5.selectAll(".line")
          .data(sumstat)
          .enter()
          .append("path")
            .attr("fill", "none")
            .attr("stroke", function(d){ return color("#377eb8") })
            .attr("stroke-width",1.5)
            .attr("d", function(d){
                anterior = 0;
                ayer = 0;
                antesdeayer=0;
                return d3.line()
                  .x(function(d) { return x(Date.parse(d.Date)); })
                  .y(function(d) { 
                  hoy = (d.Recovered-anterior+ayer+antesdeayer)/3
                  anterior = d.Recovered
                  antesdeayer=ayer
                  ayer = hoy
                  return y(hoy)
                 
                })
                  (d.values)
                 
              })

})
}
// Initialize plot
update2('Spain')

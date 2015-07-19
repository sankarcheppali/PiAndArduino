      
      google.load("visualization", "1", {packages:["gauge"]});
      google.setOnLoadCallback(drawChart);
      function drawChart() {

        var data = google.visualization.arrayToDataTable([
          ['Label', 'Value'],
          ['Temperature', 0],
          ['HeaterPower',0]
        ]);

        var options = {
          width: 400, height: 120,
          redFrom: 90, redTo: 100,
          yellowFrom:75, yellowTo: 90,
          minorTicks: 5
        };

        var chart = new google.visualization.Gauge(document.getElementById('chart_div'));

        chart.draw(data, options);

        setInterval(function() {
          $.get("T",function(resp){
             data.setValue(0, 1, parseInt(resp));
          chart.draw(data, options);
          });
        }, 7000);
         setInterval(function() {
          $.get("heaterState",function(resp){
             data.setValue(1, 1, parseInt(resp)*100);
          chart.draw(data, options);
          });
        }, 7000);
        
      }
      $( document ).ready(function() {
    $('#minTeb').click(function(){
      $.post('minT',{minT:$('#minTe').val()},function(resp){
        $('#minT').val(resp)
      });
    });
    $('#maxTeb').click(function(){
      $.post('maxT',{maxT:$('#maxTe').val()},function(resp){
        $('#maxT').val(resp)
      });
    });
});

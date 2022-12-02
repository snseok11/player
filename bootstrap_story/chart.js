src ="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/4.0.1/chart.min.js";
const labels = Utils.months({count:7})
const data = {
    labels: labels,
    datasets: [{
        label : labels,
        data:[],
        fill: false,
        borderColor : 'rgb(75,75,75)',
        tension:0.1
    }]
}


const config = {
    type:'line',
    data : data
}